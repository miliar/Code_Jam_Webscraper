#include <iostream>
#include <algorithm>
using namespace std;

bool ssgcd(int a, int b, int d) {
	if(b == 0) return (d % 2 == 0);
	else {
		if(d % 2 == 1) {
			int k = a/b;
			bool cur = false;
			while(k > 0 && !cur) cur = ssgcd(b, a - b * (k--), d+1);
			return cur;
		}
		else {
			int k = a/b;
			bool cur = true;
			while(k > 0 && cur) cur = ssgcd(b, a - b * (k--), d+1);
			return cur;
		}
	}
}

int main() {
	int t;
	cin >> t;
	for(int kase = 1; kase <= t; kase++) {
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int count = 0;
		for(int i = a1; i <= a2; i++) {
			for(int j = b1; j <= b2; j++) {
				if(ssgcd(max(i, j), min(i, j), 1) && i != j) {
					count++;
					//cout << "Winning Game: " << i << ',' << j << endl;
				}
			}
		}
		cout << "Case #" << kase << ": " << count << endl;
	}
}
