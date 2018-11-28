#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int L, D, N;
char dict[5000][16];
int slist[5000];
int snext[5000];
char src[28 * 16];
int alphabeta[26];

int compare( const void* a, const void* b)
{
	return strcmp(dict[*(int*)a], dict[*(int*)b]);
}

void input(int index)
{
	int i, length;
	scanf("%s", dict[index]);
	length = strlen(dict[index]);
	for (i = 0; i < length; ++i)
	{
		dict[index][i] -= 'a';
	}
}

void solve(int index)
{
	int i, j, p, cnt, head, length, sum;
	int stat;
	for (i = 0; i < D; ++i)
	{
		snext[i] = i + 1;
	}
	scanf("%s", src);
	length = strlen(src);
	cnt = 0;
	stat = 1;
	for (j = 0; j < 26; ++j)
	{
		alphabeta[j] = 0;
	}
	head = 0;
	for (i = 0; i < length; ++i)
	{
		if (src[i] == '(')
		{
			stat = 0;
			continue;
		}
		else if (src[i] == ')')
		{
			stat = 1;
		}
		else
		{
			alphabeta[src[i] - 'a'] = 1;
		}

		if (stat == 1)
		{
			while (head < D)
			{
				if (alphabeta[dict[slist[head]][cnt]] == 0)
				{
					head = snext[head];
				}
				else
				{
					break;
				}
			}
			p = head;
			while (snext[p] < D)
			{
				if (alphabeta[dict[slist[snext[p]]][cnt]] == 1)
				{
					p = snext[p];
					continue;
				}
				snext[p] = snext[snext[p]];
			}

			for (j = 0; j < 26; ++j)
			{
				alphabeta[j] = 0;
			}
			++cnt;
		}
	}
	sum = 0;
	for (p = head; p < D; p = snext[p])
	{
		++sum;
	}
	printf("Case #%d: %d\n", index, sum);
}

int main(void)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i;
	scanf("%d%d%d", &L, &D, &N);
	for (i = 0; i < D; ++i)
	{
		input(i);
	}
	for (i = 0; i < D; ++i)
	{
		slist[i] = i;
	}
	qsort(slist, D, sizeof(int), compare);
	for (i = 0; i < N; ++i)
	{
		solve(i + 1);
	}
	return 0;
}
