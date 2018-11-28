
#include <stdio.h>
#include <string.h>

const char *pattern="welcome to code jam";

void solve(FILE *fp, char *str)
{
	char sRes[60];
	int res = 0;
	int ans[510][30]; //ans[i][j] = answer for prefix for str up to i, pattern up to j
	memset(ans, 0, sizeof(ans));

	int pL = strlen(pattern);
	int l = strlen(str);

	for (int i = 0; i < l; i++)
	{
		for (int j = 0; j < pL; j++)
		{
			if (j > i)
				ans[i][j] = 0;
			else
			{
				if (i==0)
					ans[i][j] = (str[0] == pattern[0]);
				else
				{
					if (pattern[j] == str[i])
					{
						if (j == 0)
							ans[i][j] = (ans[i-1][j]+1)%10000;
						else
							ans[i][j] = (ans[i-1][j-1]+ans[i-1][j])%10000;
					}
					else
						ans[i][j]=ans[i-1][j];
				}
			}
		}
	}
	res = ans[l-1][pL-1];
	sprintf(sRes, "%d", (res+10000)%100000);
	fprintf(fp, " %s\n", sRes+1);
}

void readln(FILE *fp, char *w)
{
	int idx = 0;
	int c;
	while ((c = getc(fp))!=EOF)
	{
		if (c == '\n' || c == '\r')
		{
			if (idx > 0)
				return ;
			else
				while ((c == '\n' || c == '\r') && (c!=EOF))
					c = getc(fp);
			if (c==EOF)
				return;
		}
		w[idx]=c;
		idx++;
		w[idx]=0;
	}
}

int main()
{
	int N;
	FILE *fp=fopen("C-large.in","rt");
	FILE *fpo=fopen("output.out","wt");
	fscanf(fp, "%d", &N);
	for (int i = 0; i < N; i++)
	{
		char w[1000];
		readln(fp, w);
		fprintf(fpo, "Case #%d:", i+1);
		solve(fpo, w);
	}
	fclose(fp);
	fclose(fpo);
}
