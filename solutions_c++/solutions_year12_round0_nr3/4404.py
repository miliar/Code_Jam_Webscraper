#include <stdio.h>
#include <string.h>

#define N 8
#define M 10000

char str[N];

int T, A, B;

bool flag[M];

void int2string(int n, char s[], int *plen)
{
	sprintf(s, "%d", n);
	*plen = strlen(s);
}

int string2int(char s[], int len)
{
	int val = 0;
	int i = 0;
	while(i < len)
	{
		val = val * 10 + s[i] - '0';
		i++;
	}
	return val;
}

int solute(char s[], int len, int is)
{
	int idx = 0, k, l = 1, pos = 0, c = 0;
	char string[N];
	memset(flag, 0, sizeof(flag));
	for(l = 1; l < len; l++)
	{
		pos = len - l;
		k = 0;
		for(idx = pos; idx < len; idx++, k++)
			string[k] = s[idx];
		for(idx = 0; idx < pos; idx++, k++)
			string[k] = s[idx];
		string[k] = '\0';
		k = string2int(string, len); 
		if(k <= B && k > is && !flag[k])
		{
			flag[k] = true;
			c++;
		}
	}
	return c;
}

int main()
{
	int c = 0, len = 0, j = 0, ret = 0;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		scanf("%d %d", &A, &B);
		if(A == B) ret = 0;
		else
		{
			ret = 0;
			for(j = A; j < B; j++)
			{
				int2string(j, str, &len);
				if(len == 1) break;
				ret += solute(str, len, j);
			}
		}
		printf("Case #%d: %d\n", i, ret);
	}

	return 0;
}