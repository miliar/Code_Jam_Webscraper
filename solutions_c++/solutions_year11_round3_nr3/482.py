#include <stdio.h>


bool common(int a, int b)
{
	if (a > b)
	{
		return (a % b == 0);
	}

	return (b % a == 0);
}
int main()
{
	int p[20000];
	int t;
	scanf("%d", &t);
	int cnt=0;
	FILE *fout = fopen("out.out", "w");
	while (t--)
	{
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		for (int i=0; i<n; i++)
			scanf("%d", &p[i]);

		int ans = -1;
		for (int i=l; i<=h; i++)
		{
			bool f = false;
			for (int j=0; j<n; j++)
			{
				if (!common(i, p[j]))
				{
					f = true;
					break;
				}

			}
			if (f == false)
			{
				ans = i; 
				break;
			}
		}

		fprintf(fout, "Case #%d: ", ++cnt);
		if (ans == -1)
			fprintf(fout, "NO\n");
		else 
			fprintf(fout, "%d\n", ans);
	}
	fclose(fout);
	return 0;
}