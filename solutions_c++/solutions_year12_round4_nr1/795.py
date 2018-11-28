#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;
int L[1000000],D[1000000];
int dist[1000000];
bool got[1000000];
int main()
{
	freopen("D:\\gcj\\A-small-attempt0.in","r",stdin);
    freopen("D:\\gcj\\A-small-attempt0.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=0;test<tests;test++)
	{
		int N;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d %d",&D[i],&L[i]);
		}
		int Dist;
		scanf("%d",&Dist);
		memset(got,0,sizeof(got));
		got[0]=true;
		dist[0]=D[0];
		int curIdx=0;
		bool ok=false;
		if(D[0]+dist[0]>=Dist)ok=true;
		while(curIdx<N)
		{
			if(!got[curIdx])break;
			int sidx=curIdx+1;
			while(sidx<N && D[curIdx]+dist[curIdx]>=D[sidx])
			{
				if(!got[sidx])
				{
				  dist[sidx]=min(D[sidx]-D[curIdx],L[sidx]);
				  got[sidx]=true;
				  if(D[sidx]+dist[sidx]>=Dist)ok=true;

				}
				++sidx;
			}
			++curIdx;
		}
		printf("Case #%d: ",test+1);
		if(ok)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	

	}
}