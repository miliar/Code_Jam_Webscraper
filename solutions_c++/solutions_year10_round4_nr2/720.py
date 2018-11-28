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

void solve()
{
	int P;
	scanf("%d", &P);
	int n = (1 << P);
	
	vi v(n);
	for (int i=0; i<n; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		v[i] = P - tmp;
	}

	for (int i=0; i<n-1; i++)
	{
		int tmp;
		scanf("%d", &tmp);
	}
	
	int cost = 0;
	int a = n;
	int b = 1;
	for (int i=0; i<P; i++)
	{
		for (int j=0; j<n; j+=a)
		{
			int tmp = 0;
			for (int k=j; k<j+a; k++)
				if (v[k] > 0)
				{
					v[k]--;
					tmp = 1;
				}
			cost += tmp;
		}

		a >>= 1;
		b <<= 1;
	}

	printf("%d\n", cost);

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
	//static const char * const config[] = {"B-sample.txt", NULL};
	static const char * const config[] = {"B-small-attempt0.in", "B_out_small.txt"};
	//static const char * const config[] = {"-large.in", "_out_large.txt"};
	return config;
}
