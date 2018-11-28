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

int r,c,d,w[512][512], wx[512][512], wy[512][512];
long sx[512][512], sy[512][512], ss[512][512];
char s[512];
int main(int argc, char *argv[])
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		printf("Case #%d: ", test_case_id);
		scanf("%d%d%d", &r, &c, &d);
		REP(i,r) {
			scanf("%s", s);
			REP(j,c) w[i][j]=s[j]-'0';
		}
		REP(i,r) REP(j,c) wx[i][j]=w[i][j]*i, wy[i][j]=w[i][j]*j;
		CLR(sx,0); CLR(sy,0); CLR(ss,0);
		REP(i,r) REP(j,c) sx[i+1][j+1]=sx[i+1][j]+wx[i][j], sy[i+1][j+1]=sy[i+1][j]+wy[i][j], ss[i+1][j+1]=ss[i+1][j]+w[i][j];
		REP(i,r) REP(j,c) sx[i+1][j+1]+=sx[i][j+1], sy[i+1][j+1]+=sy[i][j+1], ss[i+1][j+1]+=ss[i][j+1];
		//FOR(i,0,r) {FOR(j,0,c) cerr << ss[i][j] << " "; cerr << endl;}
		int k=min(r,c);
		while (k>=3) {
			bool found=false;
			FOR(i,0,r-k) FOR(j,0,c-k) {
				long tx=sx[i+k][j+k]+sx[i][j]-sx[i][j+k]-sx[i+k][j]-wx[i][j]-wx[i+k-1][j+k-1]-wx[i][j+k-1]-wx[i+k-1][j];
				long ty=sy[i+k][j+k]+sy[i][j]-sy[i][j+k]-sy[i+k][j]-wy[i][j]-wy[i+k-1][j+k-1]-wy[i][j+k-1]-wy[i+k-1][j];
				long ts=ss[i+k][j+k]+ss[i][j]-ss[i][j+k]-ss[i+k][j]-w[i][j]-w[i+k-1][j+k-1]-w[i][j+k-1]-w[i+k-1][j];
				if (tx*2==ts*(i*2+k-1)&&ty*2==ts*(j*2+k-1)) {
					//cerr << i << " " << j << " " << k << " " << ts << " " << tx << " " << ty << endl;
					//cerr << ss[i][j] << " " << ss[i+k][j+k] << endl;
					found=true;
					break;
				}
			}
			if (found) break;
			--k;
		}
		if (k>=3) printf("%d\n", k);
		else printf("IMPOSSIBLE\n");
	}
}
