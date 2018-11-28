#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;

int n;

int solve()
{
	char ch[1];
	int k,last = -1;
	int t[2] = {0,0};
	int p[2] = {1,1};
	while (n-- > 0)
	{
		scanf("%s%d",ch,&k);
		int w = ch[0] == 'O' ? 0 : 1;
		if (last == -1 || last == w)
		{
			t[w] = t[w] + abs(k - p[w]) + 1;
			p[w] = k;
		} else 
		{
			t[w] = max(t[w] + abs(k - p[w]) + 1, t[w ^ 1] + 1);
			p[w] = k;
		}	
	    last = w;	
	}
	return max(t[0],t[1]);
}

int main()
{
//  freopen("A.in","r",stdin);
//   freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i ++)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
