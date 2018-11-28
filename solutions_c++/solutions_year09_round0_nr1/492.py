#include <cstdio>
#include <cstring>

char words[5100][20];
int anscount;
char pack[30][30];
int len[30];
int len2;

int main()
{
	int l,d,n;
	scanf("%d %d %d\n", &l, &d, &n);

	int i, j;
	for(i = 0; i < d; i++)
	{
		scanf("%s", words[i]);
	}

	for(i = 0; i < n; i++)
	{
		for(j = 0; j < 30; j++)len[j] = 0;
		len2 = 0;
		anscount = 0;
		int isinside = 0;

		char qword[500];
		scanf("%s", qword);
		int wlen = strlen(qword);
		
		for(j = 0; j < wlen; j++)
		{
			if(qword[j] == ')')
			{
				isinside = 0;
				len2++;
			}
			else if(qword[j] == '(')
			{
				isinside = 1;
			}
			else
			{
				if(isinside)
				{
					pack[len2][len[len2]++] = qword[j];
				}
				else
				{
					pack[len2][len[len2]++] = qword[j];
					len2++;
				}
			}
		}

		if(len2 == l)
		{
			int a[5100];
			anscount = d;
			for(j = 0; j < d; j++)
				a[j] = 1;
			for(int k = 0; k < l; k++)
				for(j = 0; j < d; j++)
				{
					if(a[j])
					{
						int m;
						for(m = 0; m < len[k]; m++)
							if(words[j][k] == pack[k][m])break;
						if(m >= len[k])
						{
							a[j] = 0;
							anscount--;
						}
					}
				}
		}
		printf("Case #%d: %d\n", i+1, anscount);

	}

}