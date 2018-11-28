#include <vector> 
#include <map> 
#include <set> 
#include <stack> 
#include <algorithm> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <string> 
#include <queue> 
#include <cctype> 
#include <cstring>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

int n,m;
int dt[128][128];
int go[128][128];
int hy[4]={-1,0,0,1};
int hx[4]={0,-1,1,0};
char dp[128][128];
bool chk[128][128];

void dfs(int y,int x,char c)
{
	chk[y][x]=true;
	dp[y][x]=c;

	REP(i,4) if (go[y][x]&(1<<i)) {
		int py,px;
		py=y+hy[i];
		px=x+hx[i];
		if (!chk[py][px])
			dfs(py,px,c);
	}
}

int main()
{
	int tn,qq=1;

	cin>>tn;
	while(tn--) {
		scanf("%d%d",&n,&m);
		REP(i,n) REP(j,m) cin>>dt[i][j];
		
		memset(go,0,sizeof(go));
		memset(chk,0,sizeof(chk));
		REP(i,n) REP(j,m) {
			int py,px,mn=dt[i][j],b=-1;
			REP(k,4) {
				py=i+hy[k];
				px=j+hx[k];
				if (py<0 || py>=n || px<0 || px>=m) continue;

				if (mn>dt[py][px]) {
					mn=dt[py][px];
					b=k;
				}
			}
			if (b>=0) {
				go[i][j] |= 1<<b;
				go[i+hy[b]][j+hx[b]] |= 1<<(3-b);
			}
		}

		char alp='a';
		REP(i,n) REP(j,m) if (!chk[i][j])
			dfs(i,j,alp++);
		
		printf("Case #%d:\n",qq++);
		REP(i,n) {
			REP(j,m) cout<<dp[i][j]<<" ";
			cout<<endl;
		}
	}
	return 0;
}
