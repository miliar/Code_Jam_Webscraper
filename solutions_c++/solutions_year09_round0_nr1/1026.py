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

const int L = 16;
const int N = 5001;
const int K = 27;

char buf[1 << 9];
int l, d, n;
char a[N][L];
int w[K][L];
int f[N];

inline int ch(char c)
{
	return c - 'a' + 1;
}

void scan()
{
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++)
		scanf("%s", a[i]);
}

void solve()
{
	for (int i = 0; i < n; i++)
	{
		CL(w);
		scanf("%s", buf);
		char *c = buf;
		for (int j = 0; j < l; j++)
		{
			if (*c == '(')
				while (*(++c) != ')') w[ ch(*c) ][j] = 1;
			else
				w[ ch(*c) ][j] = 1;
			c++;
		}
		CL(f);
		for (int j = 0; j < l; j++)
			for (int k = 0; k < d; k++)
				if (w[ ch(a[k][j]) ][j])
					f[k]++;
		int res = 0;
		for (int j = 0; j < d; j++)
			if (f[j] == l)
				res++;
		printf("Case #%d: %d\n", i+1, res);
	}
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif

	scan();
	solve();
	
	return 0;
}