#include <cstdio>
#include <cstring>


int nt;
int n;

int a[100];
char s[100];

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &n);

		for(int i = 1; i <= n; i++)
		{
			int k = 0;
			scanf("%s", s);
			for(int j = 1; j <= n; j++)	if (s[j - 1] == '1') k = j;
			a[i] = k;
		}

		int res = 0;

		for(int i = 1; i <= n; i++)
		{
			int k = i;
			while(1)
			{
				if (a[k] <= i) break;
				k++;
			}

			while(k > i)
			{
				int t = a[k];
				a[k] = a[k - 1];
				a[k - 1] = t;

				k--;
				res++;
			}
		}

		printf("%d\n", res);

	}

	return 0;	
}