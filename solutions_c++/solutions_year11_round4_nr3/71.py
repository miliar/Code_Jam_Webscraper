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
const int MX=1<<20;
bool p[1<<20];
int main(int argc, char *argv[])
{
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	CLR(p,true); p[0]=p[1]=false;
	long n, t;
	for (int i=2; i*i<MX; ++i) if (p[i]) for (int j=i*i; j<MX; j+=i) p[j]=false;
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		cin>>n;
		long ans=0;
		if (n>=2) ++ans;
		for (t=2; t<MX&&t*t<=n; ++t) if (p[t]) {
			long s=t;
			while (n/t>=s) s*=t, ++ans;
		}
		printf("Case #%d: %ld\n", test_case_id, ans);
	}
}
