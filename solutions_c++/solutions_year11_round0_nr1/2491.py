#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

//#define in cin
//#define out cout

ifstream in("input.txt");
ofstream out("output.txt");

#define N 200

int t, n, x;
char c[N];
int a[N];

int main() {
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		out << "Case #" << tt + 1 << ": ";

		in >> n;
		for (int i = 0; i < n; ++i) {
			in >> c[i] >> a[i];
			a[i]--;
		}

		int xb = 0, xo = 0;
		int wait_b = 0, wait_o = 0;
		int ans = 0;

		for (int i = 0; i < n; ++i) {
			if (c[i] == 'B') {
				int dist = abs(xb - a[i]);
				if (wait_b < dist) {
					ans += dist - wait_b;
					wait_o += dist - wait_b;
				}
				ans++;
				wait_o++;

				xb = a[i];
				wait_b = 0;
			} else {
				int dist = abs(xo - a[i]);
				if (wait_o < dist) {
					ans += dist - wait_o;
					wait_b += dist - wait_o;
				}
				ans++;
				wait_b++;

				xo = a[i];
				wait_o = 0;
			}
		}

		out << ans << endl;
	}

	return 0;
}
