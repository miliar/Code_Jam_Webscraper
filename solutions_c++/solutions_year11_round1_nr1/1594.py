#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long int lli;

void printtt(int i, bool b) {
	cout << "Case #" << (i+1) << ": ";
	if (b) {
		cout << "Possible";
	} else {
		cout << "Broken";
	}
	cout << endl;

}


lli gcd(lli a, lli b) {
//	cout << "gcd: " << a << ", " << b << endl;
	lli sw;
	if (a > b) {
		sw = b;
		b = a;
		a = sw;
	}
	lli tmp;
	lli times;
	lli can = b / a;
	times = can;
	tmp = times * a;
	sw = b - tmp;
	if (sw == 0) return a;
	else {
		if (sw == 1) { return 1; }
		return gcd(sw, a);    
	}
}

lli lcm(lli a, lli b) {
	return a * b / gcd(a, b);  
}

int main(void) { 
	int t;
	cin >> t;
	lli n, pd, pg;

	bool flg=false;
	bool done = false;
	//	cout << "t: " << t << endl;
	for (int i=0; i<t; i++) {
		cin >> n >> pd >> pg;
//		cout << "n: " << n << ", pd: " << pd << ", pg: " << pg << endl;
		flg = false;
		done = false;

		if (pg == 100 && pd < 100) {
			flg = false;
			done = true;
		}
		if (pg == 0) {
			flg = (pd == 0);
			done = true;
		}

		if (!done) {
			lli llccdd = lcm(pd, 100);
			lli d = llccdd / pd;
			lli wd = llccdd / 100;

			if (d > n) {
				flg = false;
			} else {
				lli x = gcd(pd, pg);
				lli g = d * pd / x;
				lli wg = wd * pg / x;

				if (d > g || wg > g || (g-d) < (wg-wd)) {
					flg = false;
				} else {
					flg = true;
				}
			}

//			cout << "hoge "<< endl;
			// int wg = g * pg / 100;
			// d <= g, wd <= wg
			// wg * 100 / pg = g >= d
			// wd <= wg = g * pg / 100
		} else {
		}
		printtt(i, flg);
	}

}
