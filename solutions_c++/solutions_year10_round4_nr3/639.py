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

int a[200][200];
int b[200][200];

void solve()
{
	int R;
	scanf("%d", &R);

	memset(a, 0, sizeof(a));


	int x1, y1, x2, y2;

	for (int i=0; i<R; i++)
	{
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		if (x1 > x2)
			swap(x1, x2);
		if (y1 > y2)
			swap(y1, y2);
		
		for (int y=y1; y<=y2; y++)
			for (int x=x1; x<=x2; x++)
				a[y][x] = 1;
	}

	int count = 0;



	for (;;)
	{
		count++;

		int tmp = 0;
		for (int i=1; i<=100; i++)
			for (int j=1; j<=100; j++)
			{
				b[i][j] = (a[i-1][j] + a[i][j-1] + a[i][j]) > 1;
				tmp += b[i][j];
			}
		if (tmp == 0)
			break;

		for (int i=1; i<=100; i++)
			for (int j=1; j<=100; j++)
				a[i][j] = b[i][j];
	
	}

	printf("%d\n", count);

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
	//static const char * const config[] = {"C-sample.txt", NULL};
	static const char * const config[] = {"C-small-attempt1.in", "C_out_small.txt"};
	//static const char * const config[] = {"-large.in", "_out_large.txt"};
	return config;
}
