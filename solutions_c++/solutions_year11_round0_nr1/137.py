#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
typedef struct {
	char choice[10];
	int pos;
} node;
node seq[110];
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int bbb = 1;
	while (T--) {
		int n;
		scanf("%d", &n);
		int ret = 0, oo, bb;
		oo = 1, bb = 1;
		vector<int> OO, BB;
		for (int i = 0; i < n; ++i) {
			scanf("%s%d", seq[i].choice, &seq[i].pos);
			if (seq[i].choice[0] == 'O') {
				OO.push_back(seq[i].pos);
			} else {
				BB.push_back(seq[i].pos);
			}
		}
		int so = 0, sb = 0;
		int len = 0;
		while (1) {
			if (so == OO.size() && sb == BB.size()) {
				break;
			}
			if (seq[len].choice[0] == 'O') {
				if (sb < BB.size()) {
					if(BB[sb] < bb) {
						--bb;
					} else if (BB[sb] > bb){
						++bb;
					}
				}
				if(OO[so] < oo) {
					--oo;
				} else if (OO[so] > oo){
					++oo;
				} else {
					++len;
					++so;
				}
			} else {
				if (so < OO.size()) {
					if(OO[so] < oo) {
						--oo;
					} else if (OO[so] > oo){
						++oo;
					}
				}
				if(BB[sb] < bb) {
					--bb;
				} else if (BB[sb] > bb){
					++bb;
				} else {
					++len;
					++sb;
				}
			}
			++ret;
		}

		printf("Case #%d: %d\n", bbb++, ret);
	}

	return 0;
}

