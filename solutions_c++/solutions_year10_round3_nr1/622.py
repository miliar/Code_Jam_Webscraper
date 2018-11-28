#include <stdio.h>
#include <memory.h>
#include <string.h>
#define N 1001

int left[N];
int right[N];
int n;

bool intersect(int a, int b)
{
	if(left[a] > left[b] && right[a] > right[b]) return false;
	if(left[a] < left[b] && right[a] < right[b]) return false;
	return true;
}

int main()
{
	//freopen("A-small.in.txt", "r", stdin);
	//freopen("A-small.out.txt", "w", stdout);
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	int t, i, j, k;
	int sum;	
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%d %d", left + j, right + j);
		}

		sum = 0;
		for(j = 0; j < n; j++)
		{
			for(k = j + 1; k < n; k++)
			{
				if(intersect(j, k)) sum++;
			}
		}
		printf("Case #%d: %d\n", i + 1, sum);
	}
	return 0;
}