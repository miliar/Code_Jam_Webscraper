#include <queue>
#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
using namespace std;

long long g[1010],nxt[1010],take[1010],len,vst[1010];

int main()
{
	long long T,cas,i,j,N,R,k;

	scanf("%lld",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%lld%lld%lld",&R,&k,&N);
		for (i=0;i<N;i++) scanf("%lld",&g[i]);
		for (i=0;i<N;i++) nxt[i]=i;
		for (i=0;i<N;i++)
		{
			long long sum=0;
			for (j=0;j<N;j++)
			{
				if (sum+g[(i+j)%N]>k)
				{
					nxt[i]=(i+j)%N;
					break;
				}
				sum+=g[(i+j)%N];
			}
			take[i]=sum;
		}
		long long cur=0,res=0,s,take1=0;
		memset(vst,0,sizeof(vst));
		while (!vst[cur])
		{
			vst[cur]=1;
			res+=take[cur];
			R--;
			if (R==0) break;
			cur=nxt[cur];
		}
		s=cur;
		len=0;
		memset(vst,0,sizeof(vst));
		while (!vst[cur])
		{
			vst[cur]=1;
			take1+=take[cur];
			len++;
			cur=nxt[cur];
		}
		res+=take1*(R/len);
		R%=len;
		cur=s;
		while (R!=0)
		{
			R--;
			res+=take[cur];
			cur=nxt[cur];
		}
		printf("Case #%lld: %lld\n",cas,res);
	}
	return 0;
}