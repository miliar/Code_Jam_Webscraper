#include <stdio.h>
#define calc 400
#define mo 100
int a[1000];
void prepare(void)
{
	a[0] = 2;
	a[1] = 6;
	for (int i = 2;i <= calc;i++)
	{
		a[i] = 6 * a[i - 1] - 4 * a[i - 2];
		a[i] %= 1000;
		a[i] += 1000;
		a[i] %= 1000;
	};
}
void Write(int x)
{
	x = x + 999;
	x %= 1000;
	printf("%d",x / 100);
	printf("%d",(x / 10) % 10);
	printf("%d",x % 10);
	printf("\n");
}
int main(void)
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	prepare();
	int T;
	scanf("%d",&T);
	for (int cases = 1;cases <= T;cases++)
	{
		printf("Case #%d: ",cases);
		int n;
		scanf("%d",&n);
		if (n <= calc) {Write(a[n]);}
		else
		{
			n %= mo;
			n += mo;
			Write(a[n]);
		}
	}
	return 0;
}
