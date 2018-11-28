#include <cstdio>
#include <map>
#include <string>

using namespace std;

const int maxn = 1024;
const int inf = 0x7f7f7f7f;

map<string,int> M;

int S,Q;
int g[maxn];

int opt[maxn][128];

void solve(int cas){
	int i,j,k;
	char str[256];
	M.clear();
	scanf("%d\n",&S);
	getchar();
	for (i=0;i<S;i++){
		gets(str);
		M[str]=i;
	}
	scanf("%d",&Q);
	getchar();
	for (i=1;i<=Q;i++){
		gets(str);
		g[i]=M[str];
	}
	memset(opt,0x7f,sizeof(opt));
	for (i=0;i<S;i++)
		opt[0][i]=0;
	for (i=1;i<=Q;i++){
		for (j=0;j<S;j++){
			for (k=0;k<S;k++){
				if (g[i]==k) continue;
				if (k==j) opt[i][k]=min(opt[i-1][k],opt[i][k]);
				else opt[i][k]=min(opt[i-1][j]+1,opt[i][k]);
			}
		}
	}
	k=inf;
	for (i=0;i<S;i++)
		k=min(k,opt[Q][i]);
	printf("Case #%d: %d\n",cas,k);
}

int main(){
	int t,cas;
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}
