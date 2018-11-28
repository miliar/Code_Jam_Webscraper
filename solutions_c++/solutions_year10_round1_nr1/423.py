#if defined(_MSC_VER) && _MSC_VER >= 1400
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()

static const char * readLine()
{
	static char buffer[2048];
	if (NULL == fgets(buffer, 2048, stdin))
		return NULL;
	int len = (int)strlen(buffer);
	if ('\n' == buffer[len - 1])
		buffer[--len] = '\0';
	return buffer;
}

int board[52][52];
int N, K;


int verity(int i, int j)
{
	if (0 == board[i][j])
		return 0;

	//printf("haha\n");
	//printf("%d\n", K);

	int ret = board[i][j];

	int k;
	for (k=1; k<K && board[i][j+k] == ret; k++);
	if (k == K)
		return ret;

	for (k=1; k<K && board[i+k][j] == ret; k++);
	if (k == K)
		return ret;

	for (k=1; k<K && board[i+k][j+k] == ret; k++);
	if (k == K)
		return ret;

	for (k=1; k<K && board[i+k][j-k] == ret; k++);
	if (k == K)
		return ret;

	return 0;
}

void solve()
{
	memset(board, 0, sizeof(board));

	scanf("%d %d", &N, &K);
	//printf("%d %d\n", N, K);
	readLine();
	for (int i=0; i<N; i++)
	{
		const char *s = readLine();
		int count = 0;
		for (int j=N-1; j>=0; j--)
		{
			char ch = s[j];
			if ('.' == ch)
				continue;
			if ('R' == ch)
				board[N-count][N-i] = 1;
			else
				board[N-count][N-i] = 2;
			count++;
		}
	}

#if 0
	printf("\n");
	for (int i=0; i<=N+1; i++)
	{
		for (int j=0; j<=N+1; j++)
		{
			if (0 == board[i][j])
				printf(".");
			else if (1 == board[i][j])
				printf("R");
			else
				printf("B");

		}
		printf("\n");
	}
#endif

	int winA = false;
	int winB = false;


#if 1
	for (int i=1; i<=N; i++) 
	{
		for (int j=1; j<=N; j++)
		{
			int ret = verity(i, j);
			if (1 == ret)
				winA = true;
			else if (2 == ret)
				winB = true;
		}
	}
#endif

	if (winA && winB)
		printf("Both");
	else if (winA)
		printf("Red");
	else if (winB)
		printf("Blue");
	else
		printf("Neither");

	printf("\n");
}

int main()
{
	int total;
	scanf("%d", &total);
	readLine();
	for (int no=1; no<=total; no++)
	{
		printf("Case #%d: ", no);
		solve();
	}
}

const char * const * getConfig()
{
	//static const char * const config[] = {"A-sample.txt", NULL};
	//static const char * const config[] = {"A-small-attempt1.in", "A_out_small.txt"};
	static const char * const config[] = {"A-large.in", "A_out_large.txt"};
	return config;
}
