#include <iostream>
using namespace std;

int main()
{
	int n, m;
	int seq[105], but[105]; 
	int a[105], b[105];
	FILE* out = fopen("a.txt","w+");

	scanf("%d", &n);
	for (int cas = 1; cas <= n; cas++)
	{
		scanf("%d", &m);
		for (int i= 0;i <= m; i++)
			a[i] = b[i] = seq[i] = but[i] = 0;
		for (int i = 1; i <= m; i++)
		{
			char op;
			int num;
			getchar();
			scanf("%c %d", &op, &num);
			if (op == 'O')
				seq[i] = 1;
			else
				seq[i] = 2;
			but[i] = num;
		}

		int ap, bp;
		ap = bp = 1;
		int j, k;
		j = k = 1;
		for (int i = 1; i <= m; i++)
		{
			if (seq[i] == 1)
			{
				if (ap < but[i])
					a[j] = but[i] - ap + 1;
				else
					a[j] = ap - but[i] + 1;
				j++;
				ap = but[i];
			}
			else
			{
				if (bp < but[i])
					b[k] = but[i] - bp + 1;
				else
					b[k] = bp - but[i] + 1;
				k++;
				bp = but[i];
			}
		}

		int t1, t2;
		t1 = t2 = 0;
		int ans = 0;
		j = k = 1;
		for (int i = 1; i <= m; i++)
		{
			if (seq[i] == 1)
			{
				if (t1 + a[j] > ans)
				{
					ans = t1 + a[j];
				}
				else
					ans++;
				t1 = ans;
				j++;
			}
			else
			{
				if (t2 + b[k] > ans)
				{
					ans = t2 + b[k];
				}
				else
					ans++;
				t2 = ans;
				k++;
			}
		}

		printf("Case #%d: %d\n", cas, ans);
		fprintf(out,"Case #%d: %d\n", cas, ans);
 	}
	fclose(out);

	system("pause");

	return 0;
}