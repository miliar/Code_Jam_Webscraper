#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define maxn 60

char s[maxn];
int len;

int ugly(int oo)
{
	int u[maxn];
	for (int i = 0; i < len - 1; i++)
	{
		u[i] = (oo % 3);
		oo /= 3;
	}
	long long a = 0;
	long long p = s[0] - '0';
	int sign = 0;
	for (int i = 1; i < len; i++)
	{
		if (u[i - 1])
		{
			if (sign <= 1)
				a += p;
			if (sign == 2)
				a -= p;
			sign = u[i - 1];
			p = 0;
		}
		p = p * 10 + (s[i] - '0');
	}
	if (sign <= 1)
		a += p;
	if (sign == 2)
		a -= p;
	return a % 2 == 0 || a % 3 == 0 || a % 5 == 0 || a % 7 == 0;
}

long long solve()
{
	len = strlen(s);
	long long res = 0;
	int z = (int) pow(3.0, len - 1.0);
	for (int i = 0; i < z; i++)
		res += ugly(i);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%s", s);
		printf("Case #%d: %lld\n", test_count + 1, solve());
	}
	return 0;
}