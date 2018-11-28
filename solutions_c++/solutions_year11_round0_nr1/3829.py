/**
 * Author        : Sowrov <sowrov@gmail.com>
 * Problem Name  : codejam_A_Bot Trust
 * Algorithm     : 
 * Date          : Saturday, May 07, 2011
 * Time          : 1:52 PM
 */
#pragma warning ( disable : 4786)
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cstring>
#include <climits>
using namespace std;

#define All(X) X.begin(),X.end()
#define co continue
#define re return
#define sf scanf
#define pf printf
#define SS stringstream
#define ox 2147483647
struct robot {
	int cp;
	int mi;
	vector<int> mov;
};
vector<int>orig;

int main() {
	freopen("codejam_A_Bot Trust.in", "r", stdin);
	freopen("codejam_A_Bot Trust.out", "w", stdout);

	int tcase, n, v;
	robot orng, blue;
	char inp[10];
	sf("%d",&tcase);

	for(int tc=1; tc<=tcase; tc++) {
		sf ("%d",&n);
		orng.mov.clear(); orng.cp = 1; orng.mi = 0;
		blue.mov.clear(); blue.cp = 1; blue.mi = 0;
		orig.clear();
		for (int i=0; i<n; i++) {
			sf("%s %d", inp, &v);

			if (inp[0]=='O') {
				orng.mov.push_back(v);
				orig.push_back(v);
			} else {
				blue.mov.push_back(v);
				orig.push_back(-v);
			}
		}
		int totaltime = 0, time=0, other;

		for (int i=0; i<n; i++) {
			if(orig[i]>0) {
				time = abs(orng.cp - orng.mov[orng.mi]) + 1;
				orng.cp = orng.mov[orng.mi];

				if (blue.mi<blue.mov.size()) {
					other = abs(blue.cp - blue.mov[blue.mi]);
					if (other<=time) {
						if (blue.mov[blue.mi]>blue.cp) {
							blue.cp += other;
						} else if (blue.mov[blue.mi]<blue.cp) {
							blue.cp -= other;
						}
					} else {
						if (blue.mov[blue.mi]>blue.cp) {
							blue.cp += time;
						} else if (blue.mov[blue.mi]<blue.cp) {
							blue.cp -= time;
						}
					}
				}
				orng.mi++;
			} else {
				time = abs(blue.cp - blue.mov[blue.mi]) +1;
				blue.cp = blue.mov[blue.mi];

				if (orng.mi < orng.mov.size()) {
					other = abs(orng.cp - orng.mov[orng.mi]);

					if (other <= time) {
						if (orng.mov[orng.mi]>orng.cp) {
							orng.cp += other;
						} else if (orng.mov[orng.mi]<orng.cp) {
							orng.cp -= other;
						}
					} else {
						if (orng.mov[orng.mi]>orng.cp) {
							orng.cp += time;
						} else if (orng.mov[orng.mi]<orng.cp) {
							orng.cp -= time;
						}
					}
				}
				blue.mi++;
			}
			totaltime += time;
		}

		pf ("Case #%d: %d\n",tc, totaltime);
	}
	return 0;
}
