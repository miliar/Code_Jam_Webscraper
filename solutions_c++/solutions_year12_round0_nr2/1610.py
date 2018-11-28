#include <iostream>
using namespace std;


int run() {
	int n, s, p, g;
	int r = 0;
	cin >> n;
	cin >> s;
	cin >> p;
	
	for(int i=0; i<n; i++) {
		cin >> g;
		if(g >= 3*p-2) {
			r++;
		} else if (g >= 3*p-4 && g >= p && s) {
			s--;
			r++;
		}
	}
	
	return r;
}




int main() {
	int n;
	cin >> n;
	for(int i=0; i<n; i++) {
		cout << "Case #" << i+1 << ": " << run() << endl;
	}
	return 0;
}