#include<stdio.h>
#include<string.h>
#include<ctype.h>

#define SZ 5005

char dict[SZ][20];
bool pat[20][27];

char line[SZ];

int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int l, d, n, i, k, j, kase;
	scanf("%d %d %d", &l, &d, &n);
	for(i = 0; i < d; i++)
	{
		scanf("%s",dict[i]);
	}
	gets(line);
	for(kase = 1; kase <= n; kase++)
	{
		int cnt = 0;
		memset(pat, false, sizeof(pat));
		gets(line);
		k = 0;
		j = 0;
		int len = strlen(line);
		bool flag = false;
		for(i = 0; i < len; i++)
		{
			if(line[i] == '(')
			{
				flag = true;
			}
			if(isalpha(line[i]))
			{
				pat[k][line[i] - 'a'] = true;
				if(flag == false)
					k++;
			}
			if(line[i] == ')')
			{
				flag = false;
				k++;
			}
		}
		for(i = 0; i < d; i++)
		{
			for(j = 0; j < l; j++)
			{
				if(pat[j][dict[i][j] - 'a'] == false)
					break;
			}
			if(j >= l)
				cnt++;
		}
		printf("Case #%d: %d\n", kase, cnt);
	}
	return 0;
}

