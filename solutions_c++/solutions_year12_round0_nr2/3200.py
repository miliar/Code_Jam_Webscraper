/*
Author:MarsChenly
Date:2012.04.14
*/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
//#include<alogirhtm>
#include<algorithm>

using namespace std;

const int maxn(105);
int f[maxn][maxn],t[maxn];

void update(int &x,int y)
{
	if (x < y) x = y;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int task;
	scanf("%d",&task);
	
	for (int cnt = 1; cnt <= task; cnt++)
	{
            int n,s,p;
		scanf("%d %d %d",&n,&s,&p);
		for (int i = 1; i<= n; i++)
			scanf("%d",&t[i]);
		memset(f,0,sizeof(f));
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j <= min(i,s); j++)
			{
				for (int t1 = 0 ; t1 <= t[i+1] ; t1 ++)
				for (int t2 = t1; t2 <= t[i+1] - t1; t2 ++)
				{
					int t3 = t[i+1] - t1 - t2;
					if (t2 <= t3)
					if (t3 - t1 <= 2)
					{
						if (t3 - t1 == 2)
						{
							update(f[i+1][j+1],f[i][j] + (t3 >= p));
						} else
						{
							update(f[i+1][j],f[i][j] + (t3 >= p));
						}
					}
				}
				//f[i+1][] f[i][j]
			}
		}
		ans = f[n][s];
		printf("Case #%d: %d\n",cnt,ans);
	}
	
	return 0;
}
