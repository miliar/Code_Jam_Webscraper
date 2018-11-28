#include<iostream>
using namespace std;
long long g[2505],p[2505],pay[2505];
int main()
{
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);

	int T,cas,i;
	long long R,K,N,begin,cycle;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%lld%lld%lld",&R,&K,&N);
		for(i=1;i<=N;i++)
		{
			scanf("%lld",g+i);
			g[i+N]=g[i];
			p[i]=-1;
		}
		p[0]=-1;
		printf("Case #%d: ",cas);
		long long cur=0,step=0;
		pay[0]=0;
		while(1)
		{
			long long left=K;
			for(i=1;i<=N;i++)
			{
				if(left<g[cur+i])
					break;
				else
					left-=g[cur+i];
			}
			cur+=i-1;if(cur>=N)cur-=N;
			step++;
			pay[step]=pay[step-1]+K-left;
			if(p[cur]>=0)
			{
				cycle=step-p[cur];
				begin=p[cur];
				break;
			}
			else
				p[cur]=step;
		}
		if(R<=begin)
			printf("%lld\n",pay[R]);
		else
		{
			long long cpay=pay[cycle+begin]-pay[begin];
			long long ans=pay[begin];
			R-=begin;
			ans+=cpay*(R/cycle);
			R%=cycle;
			ans+=pay[begin+R]-pay[begin];
			printf("%lld\n",ans);
		}
	}
}