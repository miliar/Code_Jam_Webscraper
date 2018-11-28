#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T;
int n, val[16], t, s, sum;
bool flags[16], found;

void dfs(int idx)
{
	int i;
	if(found) return;
	for(i = idx + 1; i < n; i++)
	{
		if(flags[i])
		{
			flags[i] = false;
			s ^= val[i];
			t ^= val[i];
		}
		if(s != t) dfs(i);
		else
		{
			found = true;
		}
		flags[i] = true;
		s ^=val[i];
		t ^=val[i];
	}
}

int comp(const void *a, const void *b)
{
	return *(int *)a > *(int *)b ? 1 : -1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int i, j;

	scanf("%d", &T);
	for(i = 0; i < T; i++)
	{
		s = t = sum = 0;
		memset(flags, 1, sizeof(flags));
		found = false;
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%d", &val[j]);
			s ^= val[j];
		}
		qsort(&val[0], n, sizeof(int), comp);
		for(j = 0; j < n; j++)
		{
			flags[j] = false;
			s ^= val[j];
			t ^= val[j];
			if(s != t)
			{
				dfs(j);
			}
			else
			{
				found = true;
				break;
			}
			flags[j] = true;
		}
		printf("Case #%d: ", i + 1);
		if(!found)
		{
			printf("NO\n");
		}
		else
		{
			for(j = 0; j < n; j++)
			{
				if(flags[j]) sum += val[j];
			}
			printf("%d\n", sum);
		}
	}

	return 0;
}