#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

typedef __int64 LL;

const long maxn = 1010;

long g[maxn];
//long cur_tot[maxn];
long vis[maxn];
LL r_tot[maxn];
long n, k, m, t;
LL tot_sum;

void init()
{
	scanf("%ld%ld%ld", &m, &k, &n);
	
	tot_sum = 0;
	
	for (long i = 0; i < n; ++i)
	{
		scanf("%ld", &g[i]);
		tot_sum += g[i];
	}
}

LL cal(long &head, long &m, long &tot_r)
{
	memset(vis, 0, sizeof(vis));
	memset(r_tot, 0, sizeof(r_tot));
	tot_r = 0;
	
	LL tot = 0;
	
	for (; m > 0 ;)
	{
		if (vis[head] > 0) break;
		
		r_tot[head] = tot;
		vis[head] = ++tot_r;
		--m;
		
		bool pd = 1;
		long tmp = head;
		for (long cur_k = k; cur_k >= g[head]; head = (head+1)%n)
		{
			if (tmp == head) 
			{
				if (pd) pd = 0;
				else break;
			}
		
			cur_k -= g[head];
			tot += (LL)g[head];
		}
	}	
	
	tot_sum = tot - r_tot[head];
	return tot;
}

void solve()
{
	LL ans = 0;
	long head, tot_r, cyc;
	
	head = 0;
	ans = cal(head, m, tot_r);
	
	
	cyc = tot_r - vis[head] + 1;
	ans += (LL)tot_sum * (m/cyc);
	
	m %= cyc;
	
	ans += cal(head, m, tot_r);
	
	printf("%I64d\n", ans);
}

int main()
{
	freopen("CL.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		init();
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}

