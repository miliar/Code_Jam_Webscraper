#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a-1); i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
typedef long long LG;

int M, V;
int leaf[33], inter[33], change[33];
int ppp[33];

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%d%d", &M, &V);
		FOR(i,1,(M-1)/2+1) {
			scanf("%d%d", inter + i, change + i);
		}
		FOR(i,(M-1)/2+1, M+1) scanf("%d", leaf + i);
		FOR(i,1,(M-1)/2+1) ppp[i] = 1;
		int res = 99999;
		FOR(i,1,(M-1)/2+1) {
			do {
				int cnt = 0;
				FOR(j,1,(M-1)/2+1) {
					if(change[j] == 1 && ppp[j] == 1)
						++cnt, inter[j] = 1 - inter[j];
				}
				FORD(j,(M-1)/2+1,1) {
				  if(inter[j] == 1)
					leaf[j] = leaf[2*j] & leaf[2*j+1];
				  else
					leaf[j] = leaf[2*j] | leaf[2*j+1];
				}
				if(leaf[1] == V)
					res = min(res, cnt);
				FOR(j,1,(M-1)/2+1) {
					if(change[j] == 1 && ppp[j] == 1)
						inter[j] = 1 - inter[j];
				}
			} while(next_permutation(ppp + 1, ppp + (M-1)/2+1));
			ppp[i] = 0;
		}
		if(res == 99999) printf("Case #%d: IMPOSSIBLE\n", z);
		else printf("Case #%d: %d\n", z, res);
	}
	return 0;
}
