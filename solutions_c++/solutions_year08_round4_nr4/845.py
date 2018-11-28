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

int k, n;
int t[5];
char S[1111], x[1111];

int main() {
	int T;
	scanf("%d", &T);
	for(int z=1; z<=T; ++z) {
		scanf("%d%s", &k, S);
		n = strlen(S);
		FOR(i,0,k) t[i] = i;
		int res = 999999;
		do {
			FOR(i,0,n) x[i] = S[(i-i%k) + t[i%k]];
			int cnt = 0;
			FOR(i,1,n) {
				if(x[i] != x[i-1]) ++cnt;
			}
			res = min(res, cnt);
		} while(next_permutation(t, t + k));
		printf("Case #%d: %d\n", z, res + 1);
	}
	return 0;
}
