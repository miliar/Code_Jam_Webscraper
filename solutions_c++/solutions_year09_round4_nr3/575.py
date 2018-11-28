#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;i++)

typedef vector<int> vi;

vi p[200];
int g[100][100];
int ind[100];
int n,k;
bool used[100];

int leftn;
int mincnt;

void dfs(int cnt, int cnode, int qq, int qj)
{
	if (cnt>=mincnt) return;
	if (leftn==0) {
		mincnt=cnt;
		return;
	}
	if (cnode!=-1) {
		for (int i=0;i<n;i++)
			if ( g[cnode][i] && !used[i]) {
				leftn--;
				used[i]=true;
				dfs(cnt,i, qq, i+1);
				used[i]=false;
				leftn++;
			}
	}
	if (cnt+1>=mincnt) return;
	for (int i=qq;i<n;i++)
		if (!used[i]) {
			leftn--;
			used[i]=true;
			dfs(cnt+1,i, i+1, 0);
			leftn++;
			used[i]=false;
		}
}

int main()
{
	freopen("smb.in", "r", stdin);
	freopen("outb.txt", "w", stdout);
	int tno;
	scanf("%d", &tno);
	for (int tc=1;tc<=tno;tc++) {
		scanf("%d%d", &n,&k);


		mincnt=1000000;
		memset(g,0,sizeof(g));
		memset(used,0,sizeof(used));
		memset(ind,0,sizeof(ind));
		leftn=n;

		rep(i,n) {
			p[i].resize(k);
			rep(j,k)
				scanf("%d",&p[i][j]);
		}

		rep(i,n) rep(j,n) {
			bool fail=false;
			rep(l,k)
				if (p[i][l]>=p[j][l]) { fail=true; break; }
			if ( !fail ) g[i][j]=1, ind[j]++;
		}

		dfs(0,-1, 0, 0);

		printf("Case #%d: %d\n", tc, mincnt);
		fflush(stdout);
	
	}
	return 0;
}