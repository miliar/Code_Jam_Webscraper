#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int N=2020;
int a[N],c[N],next[N];
long long ans,r[N],sum[N],s[N];

int main(){
	int T,cas,R,k,n,i;
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++){
		scanf("%d%d%d",&R,&k,&n);
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for (i=1;i<=n;i++)
			a[i+n]=a[i];
		for (i=1;i<=n+n;i++)
			s[i]=s[i-1]+a[i];
		int p=0,t;
		for (i=1;i<=n;i++){
			while (p-i<n&&s[p]-s[i-1]<=k) p++;
			sum[i]=s[p-1]-s[i-1];
			next[i]=(p<=n?p:p-n);
		}
		memset(r,0,sizeof(r));
		memset(c,0,sizeof(c));
		for (p=1,t=1;c[p]==0;t++){
			c[p]=t;
			r[t]=r[t-1]+sum[p];
			p=next[p];
		}
		int loop=t-c[p];
		t--;
		if (R<=t) ans=r[R];
		else{
			ans=r[t-loop];
			R-=(t-loop);
			ans+=R/loop*(r[t]-r[t-loop])+r[t-loop+R%loop]-r[t-loop];
		}
		printf("Case #%d: ",cas);
		cout<<ans<<endl;
	}
	return 0;
}
