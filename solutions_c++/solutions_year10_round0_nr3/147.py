#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>

int n, limit, R;
int g[1010];

void init()
{
	memset(g,0,sizeof(g));
	scanf("%d%d%d", &R, &limit, &n);
	for (int i=0; i<n; i++)
		scanf("%d", &g[i]);
}

int r[2010];
int f[2010];

void work(int testCase)
{
	long long answer = 0;
	int st = 0;
	memset(f,0,sizeof(f));
	for (int i=1; i<=R; i++)
		if (f[st]!=0)
		{
			long long sum = 0;
			int L = i - f[st];
			for (int t=f[st]; t<i; t++)
				sum = sum + r[t];
			R = R - i + 1;
			answer = answer + sum * (R/L);
			for (int t=f[st]; t<f[st] + (R%L); t++)
				answer = answer + r[t];
			break;
		}
		else
		{
			f[st] = i;
			int cur = g[st], ed = (st+1) % n;
			while (cur + g[ed]<=limit && ed!=st)
			{
				cur = cur + g[ed];
				ed = (ed + 1)%n;
			}
			st = ed;
			r[i] = cur;
			answer = answer + cur;
		}

	printf("Case #%d: %lld\n", testCase, answer);
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("c.txt","w",stdout);
	int T = 0;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		init();
		work(i+1);
	}
}