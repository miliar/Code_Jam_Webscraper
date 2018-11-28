#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

int T,ca=0;
const int N=2036;
int g[N][N];
int n,m;
bool vis[N][N];

int nReg=0;
int sz[N];
int reg[N][N];

void A(int x){
	reg[nReg][sz[nReg]++]=x;
}

int u[N], v[N];

int mx;
int a[N];
bool sol;

void gao(int k) {
	if (sol) return;
	if(k==n) {
		sol = 1;
		FOR(r,0,nReg) {
			bool mk[mx+1];
			CLR(mk);
			int cnt=0;
			FOR(i,0,sz[r]) {
				int u=reg[r][i];
				if(!mk[ a[u] ]) {
					cnt++;
					mk[ a[u] ]=1;
				}
			}
			sol &= (cnt==mx);
			if (!sol) {
//				printf("...%d\n", r);
				break;
			}
		}
		if(sol) {
			printf("%d\n", mx);
			FOR(i,0,n) printf("%d%c", a[i], (i==n-1)?'\n':' ');
		}
		return;
	}
	FOE(i,1,mx) {
		if(sol) return;
		a[k]=i;
		gao(k+1);
	}
}

int main() {
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++ca);
		scanf("%d%d", &n,&m);
		CLR(g);
		FOR(i,0,m) { scanf("%d", u+i); u[i]--; }
		FOR(i,0,m) { scanf("%d", v+i); v[i]--; }
		FOR(i,0,m) {
			g[u[i]][v[i]]=1;
			g[v[i]][u[i]]=1;
		}
		FOR(i,0,n) {
			int i2=(i+1)%n;
			g[i][i2]=g[i2][i]=1;
		}
		CLR(vis);
		CLR(sz);
		nReg=0;
		FOR(i,0,n) FOR(j,i+1,n) if(g[i][j]&&!vis[i][j]) {
			if(i==0 && j==n-1) continue;
			vis[i][j]=1;
			A(i);
			A(j);
			int lx=i;
			for(int x=j;x!=i;) {
				int k=(lx+n-1)%n;
				while (!g[x][k] || vis[x][k]) {
					k=(k+n-1)%n;
				}
				vis[x][k]=1;
				A(k);
				lx=x;
				x=k;
			}
			sz[nReg]--;
//			FOR(i,0,sz[nReg]) printf("%d ", reg[nReg][i]+1); puts("");
			nReg++;
		}
		int tot = N;
		FOR(i,0,nReg) tot = min(sz[i], tot);
		for(mx=tot,sol=0;!sol&&mx>=1;mx--) {
			gao(0);
//			printf("sol=%d %d\n", sol, mx);
		}
	}
	return 0;
}
