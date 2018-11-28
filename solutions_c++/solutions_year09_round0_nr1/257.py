#include <stdio.h>
#include <string.h>

#define SIZE_L	15
#define SIZE_D	5000
#define SIZE_N	500

int l, d, n;
char dic[SIZE_D][SIZE_L+3];
char inp[1000];

int main()
{
	int i, j, k, ptr, len, cnt, flag = 0;

	scanf("%d %d %d", &l, &d, &n);
	for(i = 0; i < d; i++)
		scanf("%s", dic[i]);
	for(i = 0; i < n; i++)
	{
		scanf("%s", inp);
		len = strlen(inp);
		cnt = 0;
		for(j = 0; j < d; j++)
		{
			ptr = 0;
			for(k = 0; k < l; k++)
			{
				if(inp[ptr] == '(')
				{
					ptr++;
					flag = 0;
					while(inp[ptr] != ')')
					{
						if(inp[ptr++] == dic[j][k]) flag = 1;
					}
					if(!flag) break;
				}
				else if(inp[ptr] != dic[j][k]) break;
				ptr++;
			}
			if(k >= l) cnt++;
		}
		printf("Case #%d: %d\n", i+1, cnt);
	}

	return 0;
}
