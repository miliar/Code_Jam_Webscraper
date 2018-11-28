#include<cstdio>
#include<cstring>
/*double g[1010],h[1010];
double f[1010][1010];
double ans[1010];
int main(){
	g[0]=1;g[1]=0;g[2]=1;
	for (int i=3;i<=1000;i++)g[i]=(i-1)*(g[i-1]+g[i-2]);
	h[0]=1;h[1]=1;
	for (int i=2;i<=1000;i++)h[i]=h[i-1]*i;
	for (int i=0;i<=1000;i++)
		for (int j=0;j<=i;j++)f[i][j]=g[j]/h[j]/h[i-j];
	ans[0]=0;
	ans[1]=0;
	for (int i=2;i<=1000;i++){
		ans[i]=f[i][i]/(1-f[i][i]);
		for (int j=0;j<i;j++)ans[i]+=ans[j]*f[i][j]/(1-f[i][i]);
		ans[i]=ans[i]+1;
	}
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
//	for (int i=0;i<=1000;i++)printf("%lf ",ans[i]);printf("\n");
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		int n,m=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			int x;
			scanf("%d",&x);
			if (x!=i)m++;
		}
		printf("Case #%d: %lf\n",TT,ans[m]);
	}
//	for (int i=0;i<=4;i++)printf("%lf\n",f[4][i]);
	return 0;
}*/
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		int n,m=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			int x;
			scanf("%d",&x);
			if (x!=i)m++;
		}
		printf("Case #%d: %d.000000\n",TT,m);
	}
	return 0;
}
