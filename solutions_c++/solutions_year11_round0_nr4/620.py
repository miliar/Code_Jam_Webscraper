#include <cstdio>

int n;
int a[1111];
int c[1111];

void test()
{
	int res = 0;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) scanf("%d", &a[i]);
	for(int i=0;i<=n;i++) c[i]=0;
	for(int i = 1; i <= n; i++)
	{
		if(c[i]) continue;
		int p = i, q = a[i], w = 1;
		c[i]=1;
		while(q != i)
		{
			c[q]=1;
			p = q;
			q = a[q];
			w++;
		}
		if(w != 1) res += w;
	}
	printf("%d\n", res);
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
