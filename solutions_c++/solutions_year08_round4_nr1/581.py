#include<algorithm>
#include<iostream>
using namespace std;
#define INF 0x3FFFFFFF


int D[10005][2],Map[10005];
int C[10005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int l,ncase; scanf("%d",&ncase);
	for(l=1;l<=ncase;++l)
	{
		int i,M,V,Temp;
		memset(D,-1,sizeof(D));
		scanf("%d%d",&M,&V);
		for(i=1;i<=(M-1)/2;i++)scanf("%d%d",&Map[i],&C[i]);

		for(i=(M-1)/2+1;i<=M;i++)
		{
			scanf("%d",&Temp);
			D[i][Temp]=0;D[i][1-Temp]=INF;
		}
		for(i=(M-1)/2;i>=1;i--)
		{
			D[i][0]=D[i][1]=INF;
			if(Map[i]==1)
			{
				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]);
				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][1]);
				D[i][0]=min(D[i][0],D[i*2][1]+D[i*2+1][0]);
				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]);
			}
			else 
			{
				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]);
				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]);
				D[i][1]=min(D[i][1],D[i*2][0]+D[i*2+1][1]);
				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][0]);
			}
			if(C[i])
			{
				if(Map[i]==0)
				{
					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]+1);
					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][1]+1);
					D[i][0]=min(D[i][0],D[i*2][1]+D[i*2+1][0]+1);
					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]+1);
				}
				else 
				{
					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]+1);
					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]+1);
					D[i][1]=min(D[i][1],D[i*2][0]+D[i*2+1][1]+1);
					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][0]+1);
				}
			}
		}
		if(D[1][V]<INF)printf("Case #%d: %d\n",l,D[1][V]);
		else printf("Case #%d: IMPOSSIBLE\n",l);
	}

	return 0;
}
