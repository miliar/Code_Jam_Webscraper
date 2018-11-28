#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

long long N, P, Q;

inline int mygcd(int a, int b) {
	return (b == 0 ? a : mygcd(b, a % b));
}

inline bool test(int m, int c, int d) {
	//cout << m << " " << c << " " << d << endl;
	if (m == 0) {return true;}
	if (m > 0) {
		if (d == c) {return false;}
		for(int i = 0 ; i < d ; i++) {
			if (((m + c * i) % d == 0)) {
				return true;
			}
		}
		return false;
	}	else {
		if (c == 0) {return false;}
		for(int i = 0 ; i < d ; i++) {
			if (((m + c * i) % d == 0)) {
				return true;
			}
		}
		return false;
	}
}
int T;
int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		bool good = true;
		cin >> N >> P >> Q;
		int g1 = mygcd(P, 100);
		int a = P / g1;
		int b = 100 / g1;
		
		if (b > N) {good = false;}
		
		int g2 = mygcd(Q, 100);
		int c = Q / g2;
		int d = 100 / g2;
		//cout << a << " " << b << " " << c << " " << d << endl;
		int mult = b * c - a * d;
		if (good) {
			good = false;
			for(int i = 1 ; i < 10000 ; i++) {
				if (i * b > N) {break;}
				if (test(mult * i, c, d)) {
					good = true;
					break;
				}
			}
		}
		cout << "Case #" << t << ": " << (good ? "Possible" : "Broken") << endl;
	}
	return 0;
}
