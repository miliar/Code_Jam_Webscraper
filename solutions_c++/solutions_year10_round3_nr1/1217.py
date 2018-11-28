#include<cstdio>
#define NM 10001
#define sh short int
int y1[NM],y2[NM],N;
int main()
{
	freopen("A.in","r",stdin);
	freopen("a.out","w",stdout);
	sh T;
	scanf("%hd",&T);
	for (sh t=1; t<=T; ++t)
	{
		scanf("%d",&N);
		long long num=0;
		for (int i=1;i<=N; ++i)
		{
			scanf("%d%d",&y1[i],&y2[i]);
			for (int j=1; j<i; ++j)
			{
				if (y1[i]>y1[j]&&y2[i]>y2[j])
				{
				
					continue;
				}
				if (y1[i]<y1[j]&&y2[i]<y2[j])
				{
					
					continue;
				}
				if (y1[i]<y1[j]&&y2[i]>y2[j])
				{
					++num;
					continue;
				}
				if (y1[i]>y1[j]&&y2[i]<y2[j])
				{
					++num;
					continue;
				}
			}
		}
		printf("Case #%d: %lld\n",t,num);
	}
	return 0;
}
