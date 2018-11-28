#include <iostream>
#include <algorithm>
using namespace std;

bool p[105];
int q[105];
int ans = 0x7777777;
int m, n;

int Am(int pos)
{
	int res = 0, i = pos-1;
	while(i >= 0 && !p[i]) {
		res++;
		i--;
	}
	i = pos+1;
	while(i < m && !p[i])
	{
		res++;
		i++;
	}
	return res;
}

void solve()
{
	int flag[105];
	for(int i = 0; i < n; i++)
	{
		flag[i] = i;
	}
	do
	{
		memset(p, false, sizeof(p));
		int tmp = 0;
		for(int i = 0; i < n; i++)
		{
			p[q[flag[i]]] = true;
			tmp += Am(q[flag[i]]);
		}
		if(tmp < ans) ans = tmp;
		
	}while(next_permutation(flag, flag+n));
}

int main()
{
	int T;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C0.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d", &m, &n);
		for(int i = 0; i < n; i++) 
		{
			scanf("%d", &q[i]);
			q[i]--;
		}
		ans = 0x7777777;
		solve();
		printf("Case #%d: %d\n",t,  ans);
	}
	return 0;
}


