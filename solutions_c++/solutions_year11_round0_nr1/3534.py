#include <stdio.h>
#include <math.h>

int main ()
{
	int t;
	int cnt=0;
	int a[200];
	int b[200];
	scanf("%d", &t);
	FILE *fout = fopen("out.out", "w");

	while (t--)
	{
		int n;
		scanf("%d", &n);

		char str[100];

		for (int i = 0; i < n; i++)
		{
			scanf("%s", str);
			if (str[0] == 'O') a[i] = 1; else a[i] = 2;
			scanf("%d", &b[i]);
		}

		int ans = 0;
		int aa = 1, bb = 1;
		int la = 0, lb = 0;
		for (int i = 0; i < n; i++)
		{
			if (a[i] == 1)
			{
				if (abs(aa-b[i]) > (ans - la))
					ans += abs(aa - b[i]) - (ans - la) + 1;
				else 
					ans += 1;

				aa = b[i];
				la = ans;
			}
			else 
			{
				if (abs(bb-b[i]) > (ans - lb))
					ans += abs(bb - b[i])  - (ans - lb) + 1;
				else
					ans += 1;
				bb = b[i];
				lb = ans;
			}
		}
		fprintf(fout, "Case #%d: %d\n",++cnt, ans);
	}
	fclose(fout);

	return 0;
}