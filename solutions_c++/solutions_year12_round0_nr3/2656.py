#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int pow10(int s) {
  int ret = 1;
  for (int i=0; i<s; i++) {
	  ret *= 10;
  }
  return ret;
}


int lcalc(int a, int b, int l) {
	int ret = 0;
	vector<int> v(l);
	for (int t=a; t<=b; t++) {
		int c=0;
		for (int j=0; j<l; j++) {
			int s = pow10(j+1);
			int ss = pow10(l - j);
			int tt =  (t % ss) * s + t / ss;
			if (t < tt && a <= tt && b >= tt) {
				bool b = true;
				for (int cc=0; cc<c; cc++) {
					if (tt == v[cc]) {
						b = false;
						break;
					}
				}
				if (b) {
//					cout << "(" << t << "," << tt << ")" << endl;
					ret++;
					v[c++] = tt;
				}

			}

		}

	}
	return ret;
}


int calc(int a, int b) {
	int loga, logb;
	loga = (int)log10(a);
	logb = (int)log10(b);
	int ret = 0;
	for (int l = loga; l <= logb; l++) {
		if (l == 0) continue;
		int la, lb;
		if (l == loga) la = a;
		else  la = pow10(l);
		if (l == logb) lb = b;
		else lb = pow10(l+1)-1;
		ret += lcalc(la, lb, l);
	}
	return ret;
}

int main(void) {
	int t;

	cin >> t;
	for (int i=0; i<t; i++) {
		int a,b;

		cin >> a >> b;
		cout << "Case #" << (i+1) << ": " << calc(a, b) << endl;
	}

}
