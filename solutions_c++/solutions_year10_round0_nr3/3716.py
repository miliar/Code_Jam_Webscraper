#include <iostream>
using namespace std;
__int64 num[1200];
bool used[1200];
__int64 pos[1200];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,N,K,R,i,j;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		memset(used,0,sizeof(used));
		scanf("%I64d%I64d%d",&R,&K,&N);
		__int64 sum=0;
		for(j=1;j<=N;j++) { scanf("%I64d",&num[j]); sum+=num[j]; }
		int now=1;
		__int64 money=0;
		int t=1;
		if(sum<=K) { printf("Case #%d: %I64d\n",i,sum*R); continue; }
		for(;t<=R;t++)
		{
			if(used[now]==1) { t--; break; }
			__int64 moment=0;
			int next;
			for(j=now;;)
			{
				if(j==N) next=1;
				else next=j+1;
				moment+=num[j];
				if(moment+num[next]>K) break;
				j=next;
			}
			pos[t]=moment;
			now=next;
			money+=moment;
		}
		__int64 p;
		int k;
		if(R>t) 
		{ 
			money*=R/t;
			for(p=(R/t)*t+1,k=1;p<=R;p++,k++) money+=pos[k];
		}
		printf("Case #%d: %I64d\n",i,money);
	}
	//while(1);
	return 0;
}
