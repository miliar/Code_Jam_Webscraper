#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
typedef __int64 ll;
const int maxn=5010;

ll R,K,n,g[1010];
ll dp[1010];
ll beg[1010],cc[1010];
ll min(ll a,ll b) {return a<b?a:b;}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca,ct=1;
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%I64d%I64d%I64d",&R,&K,&n);
		for(i=0;i<n;i++) scanf("%I64d",&g[i]);
		memset(beg,0,sizeof(beg));
		memset(dp,0,sizeof(dp));
		memset(cc,0,sizeof(cc));
		ll now=0,flag=0;
		ll ans=0,cnt;
		beg[0]=1;
		for(i=0;i<min(R,n+2);i++) 
		{
			j=now;
			flag=0,cnt=0;
			while(flag==0||j!=now) 
			{
				if(cnt+g[j]>K) break;
				cnt+=g[j];
				j=(j+1)%n;
				flag=1;
			}
			if(flag==0) break;
			beg[j]++;
			ans+=cnt;
			if(beg[j]>1) break;
			dp[j]=dp[now]+cnt;
			cc[j]=cc[now]+1;
			now=j;
		}
		printf("Case #%d: ",ct++);
		if(g[now]>K||i==R) {printf("%I64d\n",ans);continue;}
		ans=ans-cnt+(R-i)/(i-cc[j]+1)*(ans-dp[j]);
		ll has=(R-i)%(i-cc[j]+1);
		for(i=0;i<has;i++) 
		{	
			j=now;
			flag=0,cnt=0;
			while(flag==0||j!=now) 
			{
				if(cnt+g[j]>K) break;
				cnt+=g[j];
				j=(j+1)%n;
				flag=1;
			}
			if(flag==0) break;
			ans+=cnt;
			now=j;
		}
		printf("%I64d\n",ans);
	}
	return 0;
}