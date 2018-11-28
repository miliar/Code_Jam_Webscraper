#include<cstdio>
#include<memory.h>
int M[10][10];
int del[10][10];
int have[10];
char res[105];
int pr(char ch)
{
	if(ch == 'Q')
		return 1;
	if(ch == 'W')
		return 2;
	if(ch == 'E')
		return 3;
	if(ch == 'R')
		return 4;
	if(ch == 'A')
		return 5;
	if(ch == 'S')
		return 6;
	if(ch == 'D')
		return 7;
	if(ch == 'F')
		return 8;
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tt, t;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		int c, i;
		memset(M, 0, sizeof(M));
		memset(del, 0, sizeof(del));
		memset(have, 0, sizeof(have));
		memset(res, 0, sizeof(res));
		char st[105];
		scanf("%d", &c);
		for(i = 0; i < c; ++i)
		{
			scanf("%s", st);
			M[pr(st[0])][pr(st[1])] = M[pr(st[1])][pr(st[0])] = st[2];
		}
		int d;
		scanf("%d", &d);
		for(i = 0; i < d; ++i)
		{
			scanf("%s", st);
			del[pr(st[0])][pr(st[1])] = del[pr(st[1])][pr(st[0])] = -1;
		}
		int n;
		scanf("%d", &n);
		scanf("%s", st);
		int uk = 0;
		for(i = 0; i < n; ++i)
		{
			if(uk == 0)
			{
				res[uk] = st[i];
				++uk;
				++have[pr(st[i])];
				continue;
			}
			if(M[pr(res[uk-1])][pr(st[i])] != 0)
			{
				char ch = res[uk-1];
				--uk;
				--have[pr(ch)];
				res[uk] = M[pr(ch)][pr(st[i])];
				++uk;
				++have[pr(res[uk - 1])];
				continue;
			}
			bool fl = false;
			for(int j = 0; j < 10; ++j)
			{
				if(del[pr(st[i])][j] == -1 && have[j] > 0)
					fl = true;
			}
			if(fl)
			{
				uk = 0;
				memset(have, 0, sizeof(have));
				memset(res, 0, sizeof(res));
				continue;
			}
			res[uk] = st[i];
			++uk;
			++have[pr(st[i])];
		}
		printf("Case #%d: [", tt + 1);
		for(i = 0; i < uk; ++i)
		{
			if(i != 0)
				printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");

	}
	return 0;
}