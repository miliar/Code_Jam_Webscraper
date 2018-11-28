#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

const int N = 101;
const int A = 28;

int n;
int u;
int st[N];
int res[A][A];
bool kill[A][A];

inline int GetIndex(char x)
{
	return x - 'A' + 1;
}

inline char RevIndex(int x)
{
	return (char)x + 'A' - 1;
}

void ReadResults()
{
	int c;
	scanf("%d ", &c);

	while (c--)
	{
		char a, b, c;
		int indA, indB, indC;

		scanf("%c%c%c ", &a, &b, &c);

		indA = GetIndex(a);
		indB = GetIndex(b);
		indC = GetIndex(c);

		res[indA][indB] = indC;
		res[indB][indA] = indC;
	}
}

void ReadKills()
{
	int d;
	scanf("%d ", &d);

	while (d--)
	{
		char a, b;
		int indA, indB;

		scanf("%c%c ", &a, &b);

		indA = GetIndex(a);
		indB = GetIndex(b);

		kill[indA][indB] = true;
		kill[indB][indA] = true;
	}
}

void ReadCase()
{
	ReadResults();
	ReadKills();
	scanf("%d ", &n);
}

void TryCombine()
{
	char ch;
	scanf("%c", &ch);
	st[++u] = GetIndex(ch);

	if (res[st[u-1]][st[u]])
	{
		st[--u] = res[st[u]][st[u+1]];
		return;
	}

	for (int i = 1; i < u; ++i)
		if (kill[st[i]][st[u]])
		{
			u = 0;
			return;
		}
}

void PrintCase(int test)
{
	if (u == 0)
	{
		printf("Case #%d: []\n", test);
		return;
	}

	printf("Case #%d: [", test);

	for (int i = 1; i < u; ++i)
		printf("%c, ", RevIndex(st[i]));

	printf("%c]\n", RevIndex(st[u]));
}

void Solve(int test)
{
	memset(res, 0, sizeof(res));
	memset(kill, 0, sizeof(kill));
	u = 0;
	ReadCase();

	for (int i = 1; i <= n; ++i)
		TryCombine();

	PrintCase(test);
}

int main()
{
	freopen("magicka.in", "r", stdin);
	freopen("magicka.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for (int i = 1; i <= t; ++i)
		Solve(i);

	return 0;
}
