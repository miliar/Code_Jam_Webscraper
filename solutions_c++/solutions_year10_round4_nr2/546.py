#define  _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <map>

#define sz(x) (int)((x).size())
#define all(x) (x).begin(), (x).end()
#define contains(x, y) ((x).find(y) != (x).end())

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define TASK "B-large"

const int MAXTEAMS = 1024;
const int MAXLEVELS = 10;
int maxMisses[MAXTEAMS];
int minValCache[MAXTEAMS][MAXTEAMS];
int price[MAXTEAMS][MAXTEAMS];
int p;

int minVal(int from, int to)
{
	if (from == to) return maxMisses[from];
	if (minValCache[from][to] != -1)
		return minValCache[from][to];
	int mid = (from + to) / 2;
	return minValCache[from][to] = 
		min(minVal(from, mid), minVal(mid + 1, to));
}

int minPriceCache[MAXTEAMS][MAXTEAMS][MAXLEVELS];

int minPrice(int left, int right, int misses)
{
	if (minPriceCache[left][right][misses] != -1)
		return minPriceCache[left][right][misses];
	int m = minVal(left, right);
	if (left + 1 == right)
	{
		return
			minPriceCache[left][right][misses] = m == misses ? price[left][right] : 0;
	}
	// take a ticket
	int mid = (left + right) / 2;
	int res = minPrice(left, mid, misses) + minPrice(mid + 1, right, misses) + price[left][right];

	// do not take a ticket
	if (minVal(left, right) > misses)
		res = min(res, minPrice(left, mid, misses + 1) + minPrice(mid + 1, right, misses + 1));
	return minPriceCache[left][right][misses] = res;
}

int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++)
	{
		memset(minValCache, -1, sizeof(minValCache));
		memset(minPriceCache, -1, sizeof(minPriceCache));

		scanf("%d", &p);
		int teams = (1 << p);
		for (int i = 0; i < teams; i++)
			scanf("%d", &maxMisses[i]);
		int step = 1;
		for (int i = 0; i < p; i++)
		{
			step *= 2;
			for (int j = 0; j < teams; j += step)
				scanf("%d", &price[j][j + step - 1]);
		}
		int res = minPrice(0, teams - 1, 0);
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}