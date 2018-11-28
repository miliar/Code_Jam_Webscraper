#include<iostream>
#include<set>
#include<algorithm>
#include<list>
#include<queue>
using namespace std;
__int64 g[3][3];
__int64 ct(__int64 m,__int64 n)
{
	__int64 i , t = 1 , tt=1;
	for (i = 0 ; i < m ; i++)
	{
		t *= n-i;
	}
	for (i = 0 ; i < m ; i++)
		t /= tt+i;
	return t;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	__int64 n,N,A,B,C,D,M,x0,y0,i,j,k,ca,ans;
	scanf("%I64d",&N);
	for (ca = 1 ; ca <= N ; ca++)
	{
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		memset(g,0,sizeof g);
		g[x0%3][y0%3]++;
		for (i = 1 ; i < n ; i++)
		{
			x0 = (A*x0+B) % M;
			y0 = (C*y0+D) % M;
			g[x0%3][y0%3]++;
		}
		ans = 0;
		//
		for (i = 0 ; i < 9 ; i++)
		{
			for (j = i+1 ; j < 9 ; j++)
			{
				for (k = j+1 ; k < 9 ; k++)
				{
					if ((i/3 + j/3 + k/3)%3 == 0 && (i%3 + j%3 + k%3) %3 == 0 )
					{
						ans += g[i/3][i%3]*g[j/3][j%3]*g[k/3][k%3];
					}
				}
			}
		}
		for (i = 0 ; i < 3 ; i++)
		{
			for (j = 0 ; j < 3 ; j++)
			{
				if (g[i][j]>=3)
				{
					ans += ct(3,g[i][j]);
				}
			}
		}
		//
		
		printf("Case #%I64d: %I64d\n",ca,ans);
	}
	return 0;
}
