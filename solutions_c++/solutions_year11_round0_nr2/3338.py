#include <stdio.h>

int main ()
{
	int t;
	int cnt=0;
	char co[50][10], op[50][10];
	char str[200];

	FILE *fout = fopen("out.out", "w");
	scanf("%d", &t);

	while (t--)
	{
		int cn, on, n;
		scanf("%d", &cn);
		for (int i = 0; i < cn; i++)
			scanf("%s", co[i]);

		scanf("%d", &on);
		for (int i = 0; i < on; i++)
			scanf("%s", op[i]);
		
		scanf("%d", &n);
		scanf("%s", str);

		for (int i = 1; i < n; i++)
		{
			for (int j = i - 1; j >= 0; j--)
			{
				if (str[j] == 0) continue;

				for (int k = 0; k < cn; k++)
				{
					if (str[i] == co[k][0] && str[j] == co[k][1])
					{
						str[i] = co[k][2];
						str[j] = 0;
						break;
					}

					if (str[i] == co[k][1] && str[j] == co[k][0])
					{
						str[i] = co[k][2];
						str[j] = 0;
						break;
					}
				}

				break;
			}

			for (int j = 0; j < i; j++)
			{
				if (str[i] != 0 && str[j] != 0)
				{
					for (int k = 0; k < on; k++)
					{
						if ((str[i] == op[k][0] && str[j] == op[k][1]) || (str[i] == op[k][1] && str[j] == op[k][0]))
						{
							for (int l = 0; l <= i; l++)
								str[l] = 0;
							break;
						}
					}
				}
			}
		}

		fprintf(fout, "Case #%d: [",++cnt);
		bool f = true;
		for (int i = 0; i < n; i++)
		{
			if (str[i] != 0)
			{
				if (f)
				{
					fprintf(fout, "%c", str[i]);
					f = false;
				}
				else 
				{
					fprintf(fout, ", %c", str[i]);
				}
			}
		}
		fprintf(fout, "]\n");
	}
	fclose(fout);

	return 0;
}