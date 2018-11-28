/**
 * Author        : Sowrov <sowrov@gmail.com>
 * Problem Name  : codejam_B_Magicka
 * Algorithm     : 
 * Date          : Saturday, May 07, 2011
 * Time          : 5:50 PM
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
map<string, string> cMap;
map<string, bool> opMap;
int main() {
	freopen("codejam_B_Magicka.in", "r", stdin);
	freopen("codejam_B_Magicka.out", "w", stdout);
	int tcases, comb, oppo, n;
	string tmp;
	char inp[150], out[150];
	int cursor;
	sf("%d",&tcases);
	for (int tcase = 1; tcase<=tcases; tcase++) {
		cMap.clear();
		opMap.clear();
		sf("%d", &comb);
		for (int i=0; i<comb; i++) {
			sf("%s", inp);
			tmp = inp[0];
			tmp += inp[1];
			cMap[tmp] = inp[2];
			if (inp[0]!=inp[1]) {
				tmp = inp[1];
				tmp += inp[0];
				cMap[tmp] = inp[2];
			}
		}

		sf("%d", &oppo);

		for (int i=0; i<oppo; i++) {
			sf("%s", inp);
			tmp = inp[0];
			tmp += inp[1];
			opMap[tmp] = true;

			if (inp[0]!=inp[1]) {
				tmp = inp[1];
				tmp += inp[0];
				opMap[tmp] = true;
			}
		}

		sf("%d %s",&n, inp);
		cursor = 0;
		for (int i=0; i<n; i++) {
			if (cursor==0) {
				out[0] = inp[i];
				cursor = 1;
				co;
			}
			tmp = out[cursor-1];
			tmp += inp[i];

			if (cMap.find(tmp) != cMap.end()) {
				tmp = cMap[tmp];
				out[cursor-1] = tmp[0];
			} else {
				for (int j=0; j<cursor; j++) {
					tmp[0] = out[j];
					if (opMap.find(tmp) != opMap.end()) {
						cursor = -1;
						break;
					}
				}
				if (cursor == -1) {
					cursor = 0;
				} else {
					out[cursor++] = inp[i];
				}
			}
		}
		pf ("Case #%d: [", tcase);
		for (int i=0; i<cursor; i++) {
			if(i) {
				pf(", ");
			}
			pf("%c",out[i]);
		}
		pf("]\n");
	}
	return 0;
}