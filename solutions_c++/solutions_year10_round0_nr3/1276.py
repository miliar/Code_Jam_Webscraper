#include <iostream>
using namespace std;
typedef long long LL;
int g[1010];
int start[5010];
int times[5010];
LL sum[1010];
int main()
{
	int t;
	int cas=0;
	int R,k,N,i;
	int cnt;
	int rec;
	LL total,x;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		cas++;
		scanf("%d %d %d",&R,&k,&N);
		x=0;
		for(i=0;i<N;i++){
			scanf("%d",&g[i]);
			x+=g[i];
		}
		printf("Case #%d: ",cas);
		if(x<=k)
		{
			printf("%lld\n",R*x);
			continue;
		}
		memset(start,0,sizeof(start));
		memset(times,0,sizeof(times));
		start[0] = 1;
		total = 0;
		LL tmp = 0;
		cnt = 0;
		for(i=0;;i=(i+1)%N)
		{
			if(tmp+g[i]<=k){
					tmp+=g[i];
					total+=g[i];
			}
			else
			{
				if(start[i]){++cnt;rec = i;break;}
				start[i] = 1;
				times[i] = ++cnt;
				sum[i] = total;
				tmp = g[i];
				total+=g[i];
			}
		}
		int loop=cnt-times[rec];
		LL ans = 0;
		if(R<=times[rec])
		{
			for(i=0;;i++)if(times[i]==R)break;
			continue;
		}
		else
		{
			R-=times[rec];
			ans+=sum[rec];
			ans+=R/loop*(total-sum[rec]);
			R=R%loop;
			LL tmp = 0;
			if(R){
				for(i=rec;;i=(i+1)%N)
				{
					if(tmp+g[i]<=k)tmp+=g[i];
					else
					{
						ans+=tmp;
						tmp = g[i];
						R--;
						if(!R)break;
					}
				}
			}
			printf("%lld\n",ans);
		}
	}
	return 0;
}

