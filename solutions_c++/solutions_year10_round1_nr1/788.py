#include <stdio.h>
#include <string.h>
const int maxn = 100;
char map[maxn][maxn], newmap[maxn][maxn];
void rotate(int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			newmap[j][n - 1 - i] = map[i][j]; 
}
void gravity(int n)
{
	for (int i = n - 2; i >= 0; i--)
		for (int j = 0; j < n; j++)
			if (newmap[i][j] != '.') {
				int p = i + 1, cur = i;
				while (p < n && newmap[p][j] == '.') {
					char c = newmap[cur][j];
					newmap[cur][j] = newmap[p][j];
					newmap[p][j] = c;
					cur = p;
					p++;
				}
			}
}
int check(int n, int k)
{
	int findred = 0, findblue = 0;
	for (int i = 0; i < n && !findred; i++)
	{
		for (int j = 0; j < n && !findred; j++)
			if (newmap[i][j] == 'R')
			{
				int p;
				for (p = 0; p < k; p++)
				{
					if (j + p >= n) break;
					if (newmap[i][j + p] != 'R') break;
				}
				if (p == k) findred = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n) break;
					if (newmap[i + p][j] != 'R') break;
				}
				if (p == k) findred = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n || j - p < 0) break;
					if (newmap[i + p][j - p] != 'R') break;
				}
				if (p == k) findred = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n || j + p >= n) break;
					if (newmap[i + p][j + p] != 'R') break;
				}
				if (p == k) findred = 1;
			}
	}
	for (int i = 0; i < n && !findblue; i++)
	{
		for (int j = 0; j < n && !findblue; j++)
			if (newmap[i][j] == 'B')
			{
				int p;
				for (p = 0; p < k; p++)
				{
					if (j + p >= n) break;
					if (newmap[i][j + p] != 'B') break;
				}
				if (p == k) findblue = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n) break;
					if (newmap[i + p][j] != 'B') break;
				}
				if (p == k) findblue = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n || j - p < 0) break;
					if (newmap[i + p][j - p] != 'B') break;
				}
				if (p == k) findblue = 1;
				for (p = 0; p < k; p++)
				{
					if (i + p >= n || j + p >= n) break;
					if (newmap[i + p][j + p] != 'B') break;
				}
				if (p == k) findblue = 1;
			}
	}
	if (!findred && !findblue) return -1;
	if (findred && findblue) return 3;
	if (findred) return 1;
	return  2;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%s", map[i]);
		rotate(n);
		gravity(n);
		/*for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				printf("%c", newmap[i][j]);
			printf("\n");
		}*/
		int sol = check(n, k);
		if (sol == -1) printf("Case #%d: Neither\n", c);
		else if (sol == 1) printf("Case #%d: Red\n", c);
		else if (sol == 2) printf("Case #%d: Blue\n", c);
		else printf("Case #%d: Both\n", c);
	}
}