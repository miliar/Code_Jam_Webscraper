#include <stdio.h>

int l, d, n;
char words[5120][20];
bool a[20][256];
char s[10000];

int main()
{
	scanf("%d%d%d", &l, &d, &n);
	for (int i=0; i<d; i++)
	{
		scanf("%s", words[i]);
	}
	for (int i=0; i<n; i++)
	{
		scanf("%s", s);
		for (int k=0; k<l; k++)
			for (int l=0; l<256; l++)
				a[k][l] = false;
		int p = 0;
		for (int k=0; k<l; k++)
		{
			if (s[p] == '(')
			{
				for (p++; s[p] != ')'; p++)
					a[k][s[p]] = true;
				p++;
			}
			else
			{
				a[k][s[p]] = true;
				p++;
			}
		}

		int counter = 0;
		for (int j=0; j<d; j++)
		{
//			printf("%d\n", j);
			for (int k=0; k<l; k++)
				if (!a[k][words[j][k]]) break;
//			printf("%d\n", k);
			if (k == l)
				counter++;
		}
		printf("Case #%d: %d\n", i+1, counter);
	}

	return 0;
}
