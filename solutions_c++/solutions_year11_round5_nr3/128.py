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
int r, c, n;
char g[128][128];
int p[128*128][2], t[128*128];
bool check() {
	bool v[n]; CLR(v,0);
	REP(i,n) if (!v[i]) {
		int j=i;
		while (!v[j]) {
			v[j]=true;
			j=t[j];
		}
		if (j!=i) return false;
	}
	return true;
}
int main(int argc, char *argv[])
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	char ps[]="|-/\\";
	int dx[]={1,0,1,1};
	int dy[]={0,1,-1,1};
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		//fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		scanf("%d%d", &r, &c);
		REP(i,r) scanf("%s", g[i]);
		REP(i,r) REP(j,c) {
			int d=0; while (g[i][j]!=ps[d]) ++d;
			REP(k,2) {
				int nx=(i+dx[d]*(k?1:-1)+r)%r, ny=(j+dy[d]*(k?1:-1)+c)%c;
				p[i*c+j][k]=nx*c+ny;
			}
		}
		n=r*c;
		int N=1<<n;
		int ans=0;
		REP(mask,N) {
			REP(i,n) {
				t[i]=((1<<i)&mask)?p[i][1]:p[i][0];
			}
			if (check()) ++ans;
		}
		printf("Case #%d: %d\n", test_case_id, ans);
	}
}
