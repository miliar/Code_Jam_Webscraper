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

int P, K, L;
int tab[1007];

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%d%d%d", &P, &K, &L);
		FOR(i,0,L) scanf("%d", tab + i);
		sort(tab, tab + L, greater<int>());
		LG res = 0;
		LG cz = 1;
		int cnt = 0;
		FOR(i,0,L) {
			res += cz * tab[i];
			++cnt;
			if(cnt == K) cnt = 0, ++cz;
		}
		printf("Case #%d: %lld\n", z, res);
	}
	return 0;
}
