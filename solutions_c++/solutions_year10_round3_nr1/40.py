#include<stdio.h>
#include<algorithm>
#define FILENAME "large"
int T, N;
struct LIST{
	int s, e;
	bool friend operator < (LIST a,LIST b){
		return a.s<b.s;
	}
}list[1005];
int main()
{
	freopen(FILENAME ".in","r",stdin);
	freopen(FILENAME ".out","w",stdout);
	int t;
	int i, j;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for(i=1;i<=N;i++)
		{
			scanf("%d %d",&list[i].s,&list[i].e);
		}
		std::sort(list+1,list+1+N);
		int count = 0;
		for(i=1;i<=N;i++)
		{
			for(j=1;j<i;j++)
			{
				if(list[j].e > list[i].e) count ++;
			}
		}
		printf("Case #%d: %d\n",t,count);
	}
	return 0;
}