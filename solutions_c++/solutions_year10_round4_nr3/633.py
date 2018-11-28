/* 
 * Problem: Google Code Jam 2010 Round 2 bacteria
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.6.5 22:18
 * State: Solved
 * Memo: 模擬
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 301;

bool C[2][MAXN][MAXN];
int Ans;

void simulate()
{
	int i,j,k,p;
	bool s = false;
	for (k=p=0;!s;k++,p=1-p)
	{
		s = true;
		for (i=1;i<MAXN;i++)
		{
			for (j=1;j<MAXN;j++)
			{
				if (C[p][i][j])
					C[1-p][i][j] = C[p][i-1][j] || C[p][i][j-1];
				else
					C[1-p][i][j] = C[p][i-1][j] && C[p][i][j-1];
				if (C[1-p][i][j])
					s = false;
			}
		}
	}
	
	Ans = k;
}

void solve()
{
	int i,R,x1,x2,y1,y2;
	scanf("%d",&R);
	memset(C,0,sizeof(C));
	for (i=1;i<=R;i++)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for (int x=x1;x<=x2;x++)
		{
			for (int y=y1;y<=y2;y++)
			{
				C[0][x][y] = true;
			}
		}
	}
	if (R == 0)
		Ans = 0;
	else
		simulate();
	printf("%d\n",Ans);
}

int main()
{
	int T;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
