#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 1 << 12;
const int MOD = MAX - 1;

int q[MAX];
int h, r, stop;

int rr, kk, nn;
int g[MAX];

void init()
{
	scanf("%d %d %d", &rr, &kk, &nn);
	int i;
	h = r = 0;
	stop = nn;
	for(i=0; i<nn; ++i)
	{
		scanf("%d", &g[i]);
		q[r++] = g[i];
	}
}

void solve(int no)
{
	int i;
	long long ans = 0;
	int left;
	for(i=0; i<rr; ++i)
	{
		left = kk;
		while(h!=stop && left-q[h]>=0)
		{
			left -= q[h];
			ans += q[h];
			q[r] = q[h];
			h = (h+1) & MOD;
			r = (r+1) & MOD;
		}
		stop = r;
	}
	printf("Case #%d: %lld\n", no, ans);
}

int main()
{
	freopen("/home/chancer/Downloads/C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int t, i;
	scanf("%d", &t);
	for(i=1; i<=t; ++i)
	{
		init();
		solve(i);
	}
	return 0;
}

