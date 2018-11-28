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

void solve(int N, int K)
{
	int a = 1 << N;
	
	if (K % a == a - 1)
		printf("ON");
	else
		printf("OFF");
}

int main()
{
	int T;
	sscanf(readLine(), "%d", &T);
	for (int i=1; i<=T; i++)
	{
		printf("Case #%d: ", i);
		int N, K;
		sscanf(readLine(), "%d %d", &N, &K);
		solve(N, K);
		printf("\n");
	}
}

const char * const * getConfig()
{
	//static const char * const config[] = {"A-sample.txt", NULL};
	//static const char * const config[] = {"A-small-attempt0.in", "A-small-attempt0.out"};
	static const char * const config[] = {"A-large.in", "A-large.out"};
	return config;
}
