#include <stdio.h>
#include <string.h>
const int maxn = 10;
int t, f[maxn], n, ans;
char s[100000], ns[100000];
bool v[maxn];

void check()
{
	int i;
	for (i=0;s[i];++i)
		ns[i] = s[i / n * n + f[i % n + 1] - 1];
	int tmp = 1;
	for (i=1;ns[i];++i)
		if (ns[i] != ns[i - 1])
			++tmp;
	if (tmp < ans)
		ans = tmp;
}

void search(int k)
{
	if (k > n)
	{
		check();
	}
	for (int i=1;i<=n;++i)
		if (!v[i])
		{
			f[k] = i;
			v[i] = true;
			search(k + 1);
			v[i] = false;
		}
}

void work()
{
	scanf("%d", &n);
	scanf("%s", s);
	memset(ns, 0, sizeof(ns));
	memset(v, 0, sizeof(v));
	ans = 100000000;
	search(1);
	printf("Case #%d: %d\n", t, ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d", &test);
	for (t=1;t<=test;++t)
		work();
}
