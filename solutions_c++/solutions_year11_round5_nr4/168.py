#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define CLR(c,n) memset(c,n,sizeof(c))
#define MCPY(dest,src) memcpy(dest,src,sizeof(src))
template<class T> T checkmax(T &a, T b) {return a=max(a,b);}
template<class T> T checkmin(T &a, T b) {return a=min(a,b);}
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
const double EPS=1e-9;
const double PI=acos(-1);
const int INF=0x3F3F3F3F;

bool issqr(long n) {
	long p=sqrtl((long double)n+EPS);
	while (p*p>n) --p;
	while (p*p<n) ++p;
	return p*p==n;
}

int main(int argc, char *argv[])
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	char s[64];
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		//fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		scanf("%s", s);
		int n=strlen(s), m=0, g[20];
		long orig=0, ans;
		REP(i,n) {
			if (s[i]=='?') g[m++]=n-1-i;
			else if (s[i]=='1') orig|=(1LL<<(n-1-i));
		}
		int M=1<<m;
		REP(mask, M) {
			long cur=orig;
			REP(i,m) if (mask&(1<<i)) cur|=(1LL<<g[i]);
			if (issqr(cur)) {
				REP(i,m) s[n-1-g[i]]=(mask&(1<<i))?'1':'0';
			}
		}
		printf("Case #%d: %s\n", test_case_id, s);
	}
}
