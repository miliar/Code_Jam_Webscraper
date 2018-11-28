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
const int MX=10010;
int cnt[MX];
int main(int argc, char *argv[])
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int test_case;
	int n,v;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		CLR(cnt,0); scanf("%d", &n); REP(i,n) scanf("%d", &v), ++cnt[v];
		VI q;
		int first=0;
		REP(i,MX) {
			while (q.size()-first<cnt[i]) q.push_back(0);
			while (q.size()-first>cnt[i]) {
				++first;
			}
			REP(j,cnt[i]) ++q[j+first];
		}
		printf("Case #%d: %d\n", test_case_id, q.empty()?0:*min_element(ALL(q)));
	}
}
