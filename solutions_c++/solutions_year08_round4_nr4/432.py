#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

int k, len;
char s[1010], s2[1010];

int main()
{
	int t; scanf("%d", &t);
	FOR(tC,1,t) {
		scanf("%d %s", &k, &s);
		len=strlen(s);
		VI p; REP(i,k) p.PB(i);
		int res=1000000;
		do {
			REP(i,len) s2[i]=s[i-i%k+p[i%k]];
			int akt=0; char last='.';
			REP(i,len) if (s2[i]!=last) last=s2[i], akt++;
			res=min(res,akt);
		} while (next_permutation(ALL(p)));
		printf("Case #%d: %d\n", tC, res);
	}
	return 0;
}
