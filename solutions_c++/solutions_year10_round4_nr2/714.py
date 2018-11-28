/* 
 * Problem: Google Code Jam 2010 Round 2 World Cup 2010
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.6.5 23:07
 * State: unSolved
 * Memo: 模擬
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXP = 21,MAXN = 2025;

int P,A;
int M[MAXN],path[MAXP];
bool Q[MAXP][MAXN];

void cover(int x,int y)
{
	if (x == 0)
	{
		M[y] --;
	}
	else
	{
		cover(x-1,y*2);
		cover(x-1,y*2+1);
	}
}

int getmax()
{
	int i,j,v = -MAXP;
	for (i=0;i<A;i++)
	{
		if (M[i] > v)
		{
			v = M[i];
			j = i;
		}
	}
	return j;
}

void solve()
{
	int i;
	memset(Q,0,sizeof(Q));
	scanf("%d",&P);
	A = 1;
	for (i=1;i<=P;i++)
		A += A;
	for (i=0;i<A;i++)
	{
		scanf("%d",&M[i]);
		M[i] = P - M[i];
		if (M[i] < 0)
			M[i] = 0;
		if (M[i] > P)
			M[i] = P;
	}
	for (int B=A/2;B;B/=2)
	{
		int t;
		for (i=0;i<B;i++)
			scanf("%d",&t);
	}
	int Ans = 0;
	while (M[i = getmax()] > 0)
	{
		fprintf(stderr,"%d\n",i);
		int j=i,k;
		for (k=1;k<=P;k++)
		{
			j/=2;
			path[k] = j;
		}
		Ans += M[i];
		for (k=P;k>=1 && M[i]>0 ;k--)
		{
			if (Q[k][ path[k] ])
				continue;
			Q[k][ path[k] ] = true;
			cover(k,path[k]);
			fprintf(stderr,"(%d,%d)\n",k,path[k]);
		}
	}
	printf("%d\n",Ans);
}

int main()
{
	int T;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
