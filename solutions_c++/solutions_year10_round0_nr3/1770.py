#include<stdio.h>
#include<string.h>

int N;
long long k,R;
long long g[1000];
long long vis[1000];
long long ccc[1000];
int main()
{
	int t;
	scanf("%d",&t);
	for(int q=1;q<=t;q++)
	{
		scanf("%lld%lld%d",&R,&k,&N);
		memset(vis,0,sizeof(vis));
		for(int i=0;i<N;i++)
			scanf("%lld",g+i);
		long long T,Tn;
		long long first;
                int las=-1;
		long long tmp=0;
		int cnt=0;
		T=0;
		Tn=0;
                while(true)
		{
			tmp=0,cnt=0;
			while(tmp<=k&&cnt<=N)
			{
				las=(las+1)%N;
				tmp+=g[las];
				cnt++;
			}
	//		if(tmp>k)
			{
				tmp-=g[las];
				las--;
				if(las==-1) las=N-1;
			}
			Tn+=tmp;
			T++;
		        if(vis[las]) break;
			vis[las]=Tn;ccc[las]=T;
	//		printf(" %lld %d T, las\n",T,las);
		}
	//	printf("Tn %lld T %lld\n",Tn,T);
                long long ans,rem;
	        if(R>=T) ans=Tn,ans+=(R-T)/(T-ccc[las])*(Tn-vis[las]),rem=(R-T)%(T-ccc[las]);
		else rem=R,las=-1,ans=0;
                T=0,Tn=0;
                while(T<rem)
		{
			tmp=cnt=0;
			while(tmp<=k&&cnt<=N)
			{
				las=(las+1)%N;
				tmp+=g[las];
				cnt++;
			}
		//	if(tmp>k)
			{
				tmp-=g[las];
				las--;
				if(las==-1) las=N-1;
			}
			Tn+=tmp;
			T++;
		}
                ans+=Tn;
		printf("Case #%d: ",q);
                printf("%lld\n",ans);
	}
	return 0;
}
