#include <iostream>
#define clr(x,y) memset(x,y,sizeof x);
using namespace std;

bool g[200][200],y[200];
int pre[200],p[200][200],n,k,i,j,l,res,T,tt;

bool find(int x){
	for (int i=1;i<=n;++i)if (g[x][i]){
		if (!y[i]){
			y[i]=true;
			if ((!pre[i]) || find(pre[i])){
				pre[i]=x;return true;
			};
		};
	};
	return false;
};

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	//freopen("stock.in","r",stdin);
	//freopen("stock.out","w",stdout);

	cin>>T;
	for (tt=1;tt<=T;++tt){
		clr(g,0);clr(y,0);clr(pre,0);clr(p,0);
		cin>>n>>k;
		for (i=1;i<=n;++i)
			for (j=1;j<=k;++j)cin>>p[i][j];

		for (i=1;i<=n;++i)
			for (j=1;j<=n;++j){
				bool orz = true ; 
				for (l=1;l<=k;++l)
					if (p[i][l]<=p[j][l])orz=false;
				g[i][j]=orz;
			};
		res=0;
		for (i=1;i<=n;++i){
			clr(y,0);
			if (find(i))++res;
		};
		printf("Case #%d: %d\n",tt,n-res);
	};
};