#include <iostream>

using namespace std;

int getac(int a[], int N)
{
	int ret = 0;
	while (1)
	{
		int p1 = -1, p2;
		for (int i = 0; i < N; i++)
		{
			if (a[i]>i+1)
			{
				p1 = i;
				break;
			}
		}
		if (p1 == -1) break;
		for (int i = p1+1; i < N; i++)
		{
			if (a[i]<=p1+1)
			{
				p2 = i;
				break;
			}
		}
		ret+= p2-p1;
		int t = a[p2];
		for (int i = p2; i > p1; i--)
		{
			a[i] = a[i-1];
		}
		a[p1] = t;
	}
	return ret;
}

int main()
{
	int a[40];
	char s[40];
	int T;
	scanf("%d", &T);
	for (int tt = 0; tt < T; tt++)
	{
		int N;
		scanf("%d", &N);
		gets(s);
		for (int i =0 ; i < N; i++)
		{
			int r = 0;
			for (int j = 0; j < N; j++)
			{
				char t;
				scanf("%c", &t);
				if (t == '1') r = j+1;
			}
			a[i] = r;
			gets(s);
		}
		printf("Case #%d: %d\n", tt+1, getac(a, N));
	}
	return 0;
}