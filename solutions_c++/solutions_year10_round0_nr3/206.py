#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int main(){
	int t,T;
	int i,j,n,now;
	long long sum,k,R,g[1000],ss[1000],ans=0;
	int s[1000];
	int a[10000];
	scanf("%d",&T);
	for (t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%lld %lld %d",&R,&k,&n);
		for (i=0;i<n;i++)
			scanf("%lld",&g[i]);
		for (i=0;i<n;i++){
			sum=0;
			for (j=0;j<n;j++)
			{
				sum+=g[(i+j)%n];
				if (sum>k) break;
			}
			if (sum>k) {sum-=g[(i+j)%n]; j--;}
			s[i]=(i+j+1)%n;
			ss[i]=sum;
		//	printf("%d:%lld %d\n",i,sum,s[i]);
		}
		now=0;
		ans=0;
		a[0]=0;
		for (i=0;i<R;i++){
			ans+=ss[now];
			a[i]=now;
			for (j=0;j<i;j++)
			if (a[i]==a[j]) break;
			if (j<i) break;
			now=s[now];
		}
		if (i<R){
			ans-=ss[a[i]];
			sum=0;
			for (k=j;k<i;k++) 
			 sum+=ss[a[k]];
			j=i-j;
			R=R-i;
			ans+=(R/j)*sum;
			R%=j;
			for (i=0;i<R;i++){
				ans+=ss[now];
				now=s[now];
			}
		}
		printf("%lld\n",ans);
	}
  return 0;
}
