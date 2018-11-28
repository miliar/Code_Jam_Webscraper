#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

#include <cmath>
#include <cstdio>

using namespace std;

bool g(int a, int b) {
	if (a<b) swap(a,b);
	
	if (a == b) return false;
	if (a % b == 0) return true;
	if ((float)a/b >= 2) return true;
	return !g(a-b, b);
}

void w() {
	int a1, a2, b1, b2;
	cin >> a1 >> a2 >> b1 >> b2;
	int c = 0;
	for (int i = a1; i <= a2; i++) {
		for (int j = b1; j <= b2; j++) {
			if (g(i, j)) {
				//cout << endl << i << " " << j;
				c++;
			}
		}
	}
	cout << c;
}

int main()
{
	freopen("c.in", "r", stdin); freopen("c.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << (i+1) << ": ";
		w();
		cout << endl;
	}
	return 0;
}