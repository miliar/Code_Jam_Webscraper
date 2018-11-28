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


bool isWin(int a, int b)
{
	if (a == b)
		return false;
	
	if (a % b == 0)
		return true;

	bool t1 = isWin(b,a % b);
	bool t2 = true;

	if (a - b > b)
		t2 = isWin(a % b + b, b);

	if (t1 && t2)
		return false;

	return true;
}

void solve()
{
	int A1, A2;
	int B1, B2;
	scanf("%d %d %d %d", &A1, &A2, &B1, &B2);

	int count = 0;
	for (int i=A1; i<=A2; i++)
	{
		for (int j=B1; j<=B2; j++)
		{
			int a, b;
			if (i >= j)
			{
				a = i;
				b = j;
			}
			else
			{
				a = j;
				b = i;
			}
			if (isWin(a, b))
				count++;
		}
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
	static const char * const config[] = {"C-small-attempt0.in", "C_out_small.txt"};
	//static const char * const config[] = {"-large.in", "_out_large.txt"};
	return config;
}
