#include <cstdio>
#include <algorithm>
#include <queue>
#include <string>
#define N 1000005
using namespace std;
int tc,a[20],vis[N],mv[20][N];
char s[100];
int con(int x,int base){
	int ans=0,dig[100],len=0,xx=x,pr=1;
	while (pr<N) pr*=base;
	while (xx){
		dig[++len]=xx/pr;
		xx=xx-(xx/pr)*pr;
		pr/=base;
	}
	for (int i=1;i<=len;i++) ans+=dig[i]*dig[i];
	return ans;
}
int main(){
	scanf("%d\n",&tc);
	for (int C=1;C<=tc;C++){
		gets(s);
		int L=strlen(s),h=0;
		int n=(L+1)/2,ok=0;
		for (int i=1,hh=0;i<=(L+1)/2;i++)
			sscanf(s+hh,"%d%n",&a[i],&h),hh+=h;
		//for (int i=1;i<=n;i++) printf("%d ",a[i]);
		int AC=N;
		for (int k=2;k<=AC;k++){
			bool b=1;
			for (int j=1;j<=n&&b;j++)
				if (!mv[a[j]][k]){
					int p=k,r=con(p,a[j]);
					while (r!=1 && !vis[r])
						vis[r]=1,p=r,r=con(p,a[j]);
					if (r!=1) b=0;
					else mv[a[j]][k]=1;
					p=k,r=con(p,a[j]);
					while (r!=1 && vis[r])
						vis[r]=0,p=r,r=con(p,a[j]);
				}
			if (b){
				printf("Case #%d: %d\n",C,k);
				break;
			}
		}
	}
	scanf("\n");
	return 0;
}
