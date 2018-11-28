#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<algorithm>
using namespace std;

int Case , TC = 1;
int R,x1,x2,y1,y2;
int map[110][110];
int tmp[110][110];
int Count;

int solve()
{
	int i,j,k;
	int flag = 0 , ans = 0;
	while(1)
	{
		ans++;
		for(j=1;j<=100;j++)
		{
			for(k=1;k<=100;k++)
			{
				if(map[j][k])
				{
					if(!map[j-1][k] && !map[j][k-1])
					{ 
						tmp[j][k] = 0;
						Count--;
					}
					else	tmp[j][k] = map[j][k];
				}
				else
				{
					if(map[j-1][k] && map[j][k-1])
					{  
						tmp[j][k] = 1;
						Count++;
					}
					else	tmp[j][k] = map[j][k];
				}
			}
		}
		if(!Count) break;
		for(j=1;j<=100;j++)
			for(k=1;k<=100;k++)
				map[j][k] = tmp[j][k];
	}
	return ans;
}
	
int main()
{
	int i;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&Case);
	for(;Case>0;Case--)
	{
		scanf("%d",&R);
		memset(map,0,sizeof(map));
		Count = 0;
		for(i=0;i<R;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int j=x1;j<=x2;j++)
				for(int k=y1;k<=y2;k++)
				{
					if(!map[j][k])
					{
						map[j][k] = 1;
						Count++;
					}
				}
		}
		printf("Case #%d: %d\n",TC++,solve());
	}
	return 0;
}
