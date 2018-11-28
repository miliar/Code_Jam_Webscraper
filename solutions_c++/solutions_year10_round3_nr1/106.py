#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define For(i, a, b) for(int i = a; i < b; i++)
#define Ror(i, a, b) for(int i = a - 1; i >= b; i--)

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;

int sign(int a)
{
	if(a < 0)
		return -1;
	if(a == 0)
		return 0;
	return 1;
}

int Solution(int nTest)
{
	int n;
	scanf("%d", &n);
	vector<pii> v(n);
	For(i, 0, n)
		scanf("%d%d", &v[i].first, &v[i].second);
	int res = 0;
	For(i, 0, n)
		For(j, i + 1, n)
	{
		if(sign(v[i].first - v[j].first) * sign(v[i].second - v[j].second) < 0)
			res++;
	}


	printf("Case #%d: ", nTest + 1);

	printf("%d\n", res);
	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 9999;
	scanf("%d", &n);
	while(i < n && Solution(i))
		i++;

	return 0;
}