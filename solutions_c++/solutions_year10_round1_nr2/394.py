/* 
 * Problem: Google Code Jam 2010 Round 1A smooth
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.5.22 9:00
 * State: Solved
 * Memo: 枚舉
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 101,MAXM = 255,INF = ~0U>>1;

int D,I,M,N,mam;
int A[MAXN],B[MAXN],Ans;

inline int abso(int k)
{
	return k<0?-k:k;
}

void dfs(int i,int v)
{
	if (i > N)
	{
		int k=0;
		for (int j=1;j<=N;j++)
		{
			if (A[j] == -1)
				continue;
			B[++k] = A[j];
		}
		for (int j=1;j<k;j++)
		{
			int d = abso(B[j+1] - B[j]);
			if (d != 0)
			{
				if (M == 0)
					return;
				if (d % M == 0)
					d = d / M - 1;
				else
					d = d / M;
				d *= I;
			}
			v += d;
		}
		if (v < Ans)
			Ans = v;
		return;
	}
	int t = A[i],j,d;
	for (j=-1;j<=mam;j++)
	{
		A[i] = j;
		if (j == -1)
			d = D;
		else
			d = abso(j - t);
		dfs(i+1,v + d);
	}
	A[i] = t;
}

void solve()
{
	dfs(1,0);
}

int main()
{
	int T;
	freopen("smooth.in","r",stdin);
	freopen("smooth.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&N);
		mam = 0;
		for (int j=1;j<=N;j++)
		{
			scanf("%d",&A[j]);
			if (A[j] > mam)
				mam = A[j];
		}
		Ans = INF;
		cerr << i << endl;
		solve();
		printf("Case #%d: %d\n",i,Ans);
	}
	return 0;
}
