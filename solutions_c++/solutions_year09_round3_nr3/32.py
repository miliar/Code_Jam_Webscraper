#include <cstdio>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

int p, q;
int r[102];
int cache[102][102];
int when[102][102];
int i;

int solve(int start, int end)
{
	if (end == start+1)
		return 0;
	if (when[start][end] == i)
		return cache[start][end];
	int j;
	int best = 99999999;
	for (j = start+1; j < end; j++)
		best = min(best, solve(start, j) + solve(j, end));
	cache[start][end] = best + r[end] - r[start] - 2;
	when[start][end] = i;
	return cache[start][end];
}

int main()
{
	FILE* input = fopen("input3.txt", "r");
	FILE* output = fopen("output3.txt", "w");
	int n;
	fscanf(input, "%d", &n);
	for (i = 1; i <= n; i++)
	{
		fscanf(input, "%d %d", &p, &q);
		r[0] = 0;
		r[q+1] = p+1;
		int j;
		for (j = 1; j <= q; j++)
			fscanf(input, "%d", &r[j]);
		fprintf(output, "Case #%d: %d\n", i, solve(0, q+1));
	}
}