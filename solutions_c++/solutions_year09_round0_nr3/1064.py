#pragma comment(linker, "/STACK:16777216")
#include <stdio.h>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

#define CL(x)		memset(x, 0, sizeof(x))
#define CLX(x, v)	memset(x, v, sizeof(x))
#define PB			push_back
#define MP			make_pair

///////////////////////////////////////////////////////////

const int P = 10000;
const int N = 512;
const int L = 19;
const char *F = "welcome to code jam";

char s[N];
LL d[N][L];

void solve()
{
	CL(d);
	for (int i = 0; s[i]; i++)
		if (s[i] == F[0])
			d[i][0] = 1;
	for (int i = 1; i < L; i++)
		for (int j = 0; s[j]; j++)
		{
			if (s[j] != F[i]) continue;
			for (int k = 0; k < j; k++)
			{
				if (s[k] != F[i-1]) continue;
				d[j][i] = (d[j][i] + d[k][i-1]) % P;
			}
		}
	LL res = 0;
	for (int i = 0; s[i]; i++)
		res = (res + d[i][L-1]) % P;
	printf("%04lld\n", res);
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	int n;
	gets(s);
	sscanf(s, "%d", &n);
	for (int i = 0; i < n; i++)
	{
		gets(s);
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}