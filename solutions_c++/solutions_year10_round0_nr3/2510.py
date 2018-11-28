#include<iostream>
using namespace std;
int main()
{
	freopen("D:\\C-small-attempt0.in","r",stdin);
	freopen("D:\\C-small-attempt0.out","w",stdout);

	int T,cas,R,K,N,i,begin,cycle,g[2005],p[1005],pay[1005];
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for(i=1;i<=N;i++)
		{
			scanf("%d",g+i);
			g[i+N]=g[i];
			p[i]=-1;
		}
		p[0]=-1;
		printf("Case #%d: ",cas);
		int cur=0,step=0;
		pay[0]=0;
		while(1)
		{
			int left=K;
			for(i=1;i<=N;i++)
			{
				if(left<g[cur+i])
					break;
				else
					left-=g[cur+i];
			}
			cur+=i-1;if(cur>=N)cur-=N;
			//printf("new cur=%d\n",cur);
			step++;
			pay[step]=pay[step-1]+K-left;
			if(p[cur]>=0)
			{
				//found cycle
				cycle=step-p[cur];
				begin=p[cur];
				break;
			}
			else
				p[cur]=step;
		}
		//printf("%d %d\n",begin,cycle);
		if(R<=begin)
			printf("%d\n",pay[R]);
		else
		{
			int cpay=pay[cycle+begin]-pay[begin];
			int ans=pay[begin];
			R-=begin;
			ans+=cpay*(R/cycle);
			R%=cycle;
			ans+=pay[begin+R]-pay[begin];
			printf("%d\n",ans);
		}
	}
}