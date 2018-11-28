#include<cstdio>

using namespace std;

int a[2000];
double f[2000],opt[2000];
int i,n,T,I,tot,j;
double ans,s;
bool bt[2000];

int main(){
	f[1]=0;
	for (i=2;i<=1000;++i){
		f[i]=0;
		s=0;
		for (j=1;j<i;++j)
			s+=(f[j]+opt[i-j])/i;
		f[i]=(s+1)*i/(i-1);
		opt[i]=s+f[i]/i;
	}

	scanf("%d",&T);
	while (T--){
		scanf("%d",&n);
		for (i=1;i<=n;++i){
			scanf("%d",&a[i]);
			bt[i]=1;
		}
		ans=0;
		for (i=1;i<=n;++i)
			if (bt[i]){
				tot=0;
				for (j=i;bt[j];bt[j]=false,j=a[j],++tot);
				ans+=f[tot];
			}
		printf("Case #%d: %.10lf\n",++I,ans);
	}
}

