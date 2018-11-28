/* 
 * Problem: Google Code Jam 2010 Qualification Round - Theme Park
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.5.8 9:53
 * State: Solved
 * Memo: 計算環
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 1001;

typedef long long big;

int R,K,N;
big g[MAXN],next[MAXN],val[MAXN],length[MAXN],tov[MAXN],Ans;

void solve()
{
	memset(next,0,sizeof(next));
	memset(val,0,sizeof(val));
	memset(length,0,sizeof(length));
	memset(tov,0,sizeof(tov));
	Ans = 0;
	
	big i,j,c,r,w,x,t;
	tov[1] = 0;
	length[1] = 1;
	for (i=1,r=1;r<=R ;r++)
	{
		for (j=i,c=0,t=1;c + g[j] <= K && t<=N;t++)
		{
			c += g[j];
			if (++j > N)
				j = 1;
		}
		next[i] = j;
		val[i] = c;
		tov[i] += c;
		Ans = tov[i];
		
		if (length[j] != 0)
		{
			w = length[i] - length[j] + 1;
			x = tov[i] - tov[j] + val[j];
			i = j;
			break;
		}
		else
		{
			length[j] = length[i] + 1;
			tov[j] = tov[i];
		}
		
		i = j;
	}
	
	R-=r;
	if (R > 0)
	{
		Ans += R / w * x;
		R %= w;
		for (r=1;r<=R;r++,i = next[i])
		{
			Ans += val[i];
		}
	}
}

int main()
{
	int T;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for (int j=1;j<=N;j++)
			scanf("%lld",&g[j]);
		solve();
		printf("Case #%d: %lld\n",i,Ans);
	}
	return 0;
}
