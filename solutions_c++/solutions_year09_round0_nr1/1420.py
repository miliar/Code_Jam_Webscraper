#include <stdio.h>
#include <string.h>

int L, D, N, cnt;
char cuv[5096][16], pattern[65536];
int op[16][26];

int main()
{
	int i, j, k, ok, len, bracket = 0;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d %d %d", &L, &D, &N);
	for (i = 1; i <= D; ++i)
		scanf("%s", cuv[i]); 

	for (i = 1; i <= N; ++i)
	{
		memset(op, 0, sizeof(op));

		// read and parse the pattern		
		scanf("%s", pattern);
		len = strlen(pattern);
		bracket = 0;
		for (j = 0, k = 0; j < len; ++j)
		{
			if (pattern[j] == '(')
			{
				bracket = 1;
				continue;
			}
			if (pattern[j] == ')')
			{
				++k;
				bracket = 0;
				continue;
			}				
			op[k][pattern[j]-'a'] = 1;
			if (!bracket)
				++k;			
		}
		
		cnt = 0;
		for (j = 1; j <= D; ++j)
		{
			ok = 1;
			for (k = 0; k < L && ok; ++k)
				ok = op[k][cuv[j][k]-'a'];
			cnt += ok;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	
	return 0;
}
