#include <iostream>

using namespace std;

const int MAX = 1005;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int visit[MAX], group[MAX];
	__int64 income[MAX];
	int T, i, ncase;
	scanf("%d",&T);
	for(ncase=1; ncase<=T; ncase++)
	{
		int R,K,N;
		scanf("%d %d %d",&R,&K,&N);
		for(i=0;i<N;i++)
			scanf("%d",&group[i]);
		memset(visit,-1,sizeof(visit));
		memset(income,0,sizeof(income));
		visit[0]=0;
		int index = 0;
		__int64 ans = 0;
		__int64 sumgrp = 0;
		for(i=0;i<N;i++)
			sumgrp+=group[i];
		if(sumgrp<=K)
			ans = (__int64)sumgrp*R;
		else
		{
			for(int j=1;j<=N+1 && j<=R;j++)
			{
				int sum = 0;
				while(sum<=K)
				{
					sum+=group[index];
					if(sum>K)
					{
						sum-=group[index];
						break;
					}
					else
						index= (index+1)%N;
				}
				if(visit[index]==-1)
				{
					income[j]=sum;
					ans += sum;
					visit[index]=j;
				}
				else
				{
					ans+=sum;
					income[j]=sum;
					int pre = visit[index];
					int dis = j-pre;
					int remind = R-j;
					__int64 cnt = 0;
					for(i=pre+1;i<=j;i++)
						cnt+=income[i];
					ans += ((__int64)remind/dis)*cnt;
					for(i=pre+1;i-pre<=remind%dis;i++)
						ans+=income[i];
					break;
				}
			}
		}
	
		printf("Case #%d: %I64d\n",ncase,ans);
	}
	return 0;
}