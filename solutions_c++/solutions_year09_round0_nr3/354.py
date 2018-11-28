#include <stdio.h>
#include <string.h>

char stra[32] = "welcome to code jam";
char strb[512];

int n, m[20][512];

int lena = strlen(stra);
int lenb;

int main()
{
	scanf("%d", &n);
	gets(strb);
	for (int i = 0; i < n; i++)
	{
		gets(strb);
		lenb = strlen(strb);
		if (stra[0] == strb[0])
		{
			m[0][0] = 1;
		}
		else
		{
			m[0][0] = 0;
		}
		for (int k = 1; k < lenb; k++)
		{
			if (stra[0] == strb[k])
			{
				m[0][k] = m[0][k-1] + 1;
			}
			else
			{
				m[0][k] = m[0][k-1];
			}
		}

		for (int j = 1; j < lena; j++)
		{
			for (int k = 0; k < j; k++)
			{
				m[j][k] = 0;
			}
			for (int k = j; k < lenb; k++)
			{
				if (stra[j] == strb[k])
				{
					m[j][k] = (m[j-1][k-1] + m[j][k-1]) % 10000;
				}
				else
				{
					m[j][k] = m[j][k-1];
				}
			}
		}
		printf("Case #%d: %04d\n", i+1, m[lena-1][lenb-1]);
	}
	return 0;
}
