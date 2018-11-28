#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int r,k,test,n,testcase,t,i,j,step[1005],jump[1005];
long long g[2005],js[1005],a[1005],ans,s;
bool b[1005];
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for (int test=1; test<=testcase; ++test) {
		scanf("%d%d%d",&r,&k,&n);
		for (i=1; i<=n; ++i) {
			scanf("%lld",&g[i]);
			g[i+n]=g[i];
		}
		
		for (i=1; i<=n; ++i) {
			s=g[i];
			j=i;
			while (j<i+n && s<=k) {
				++j; 
				s+=g[j];
			}
			js[i]=s-g[j];
			jump[i]=j-1;
			if (jump[i]>n) jump[i]-=n;
		}
		
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		i=1; t=0;
		while (!b[i]) {
			step[i]=++t;
			a[t]=a[t-1]+js[i];
			b[i]=true;
			i=jump[i]+1;
			if (i==n+1) i=1;
		}
		ans=a[step[i]-1];
		ans+=((r-step[i]+1)/(t-step[i]+1))*(a[t]-a[step[i]-1]);
		ans+=a[step[i]+(r-step[i]+1)%(t-step[i]+1)-1]-a[step[i]-1];
		
		printf("Case #%d: %lld\n",test,ans);
	}
	return 0;
}