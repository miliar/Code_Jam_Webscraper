#include<cmath>
#include<cstdio>
#include<cstring>
#define maxn (1005)
using namespace std;

double f[maxn],g[maxn][maxn],h[maxn],ans;
int n,test,testcase,a[maxn];
bool vis[maxn];

void prepare(){
	f[0]=0;
	f[2]=(double)1/2;
	for (int i=3;i<=1000;i++) f[i]=f[i-2]/(double)i+f[i-1]*(double)(i-1)/i;
	g[1][0]=0;g[1][1]=1;
	for (int i=2;i<=1000;i++){
		g[i][0]=f[i];
		for (int j=1;j<=i;j++) g[i][j]=g[i-1][j-1]/(double)j;
	}
	h[0]=0;
	h[1]=0;
	for (int i=2;i<=1000;i++){
		double totp=0,sum=1;
		for (int j=1;j<=i;j++){
			totp+=g[i][j];
			sum+=g[i][j]*h[i-j];
		}
		h[i]=sum/=totp;
	}
}
int main(){
	freopen("i.txt","r",stdin);
	prepare();
	testcase=1;
	for (scanf("%d",&test);test--;testcase++){
		printf("Case #%d: ",testcase);
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		ans=0;
		memset(vis,0,sizeof(vis));
		for (int i=1;i<=n;i++) if (!vis[i]){
			int len=0;
			for (int j=i;!vis[j];j=a[j]){
				len++;
				vis[j]=true;
			}
			ans+=h[len];
		}
		printf("%.6lf\n",ans);
	}
	return 0;
}
