#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int que[20000];
bool isevil[110][110];
int w,h,r;
int x[10],y[10];
int num[110][110];
bool vis[110][110];

int bfs();

int main()
{
	int t, T;
	scanf("%d",&T);
	for(t = 1;t <= T;++t)
	{
		scanf("%d%d%d",&h,&w,&r);
		memset(isevil,0,sizeof(isevil));
		for(int i = 0;i < r;++i)
		{
			scanf("%d%d",&x[i],&y[i]);
			isevil[x[i]][y[i]] = 1;
		}
		int ans = bfs();
		ans %= 10007;
		printf("Case #%d: %d\n",t,num[h][w]);
	}

}


int bfs()
{
    int i,x0,y0, start = 0,en = 0,temp,ans = 0;

	que[en++] = 1001;

	vis[1][1] = 1;
	num[1][1] = 1;	
	memset(vis,0,sizeof(vis));
	memset(num,0,sizeof(num));
	while(start != en)
	{
		temp = en;
		for(i = start;i < en;++i)
		{
			x0 = que[i] / 1000;
			y0 = que[i] % 1000;
			if(x0+1 <= h && y0+2 <= w)
			{
				if(((!isevil[x0][y0+1]) && (!isevil[x0][y0+2]) && (!isevil[x0+1][y0+2])) || ((!isevil[x0+1][y0]) && (!isevil[x0+1][y0+1]) && (!isevil[x0+1][y0+2])))
					num[x0+1][y0+2] += num[x0][y0];
				num[x0+1][y0+2] %= 10007;
				if(!vis[x0+1][y0+2])
				{
					vis[x0+1][y0+2] = 1;
					que[temp++] = (x0+1)*1000+y0+2;
				}
			}
			if(x0+2 <= h && y0+1 <= w)
			{
				if(((!isevil[x0+1][y0+1]) && (!isevil[x0][y0+1]) && (!isevil[x0+2][y0+1])) || ((!isevil[x0+1][y0]) && (!isevil[x0+2][y0]) && (!isevil[x0+2][y0+1])))
					num[x0+2][y0+1] += num[x0][y0];
				num[x0+2][y0+1] %= 10007;
				if(!vis[x0+2][y0+1])
				{
					vis[x0+2][y0+1] = 1;
					que[temp++] = (x0+2)*1000+y0+1;
				}
			}	
		}
		start = en;
		en = temp;
	}
	return num[h][w];
}

