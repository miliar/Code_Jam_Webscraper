#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

const int EMPTY = -1;
int array[20][600];
char* query = "welcome to code jam";
char* line = 0;

void fill(int i, int j)
{
	if (array[i][j] != EMPTY)
		return;

	fill(i , j+1);
	array[i][j] = array[i][j+1];
	
	if(query[i] == line[j])
	{
		fill(i+1, j+1);
		array[i][j] += array[i+1][j+1];
		array[i][j] %= 10000;
	}
}

void solve(int caseNum)
{
	size_t maxSize = 550;
	getline(&line, &maxSize, stdin);

	int n = strlen(line);
	int m = strlen(query) + 1;

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			array[i][j] = EMPTY;

	for (int i = 0; i < m-1; i++)
		array[i][n-1] = 0;
	for (int i = 0; i < n; i++)
		array[m-1][i] = 1;

	fill(0, 0);

	printf("Case #%d: %.4d\n", caseNum, array[0][0]);

	if (line)
	{
		free(line);
		line = 0;
	}
}

int main()
{
	int N;
	scanf("%d\n", &N);

	for (int i = 0; i < N; i++)
		solve(i+1);

	return 0;
}
