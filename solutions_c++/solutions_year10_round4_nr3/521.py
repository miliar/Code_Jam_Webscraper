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

#define TASK "C-small-attempt0"

bool alive[2][101][101];

int main()
{
	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++)
	{
		memset(alive, 0, sizeof(alive));
		int r;
		scanf("%d", &r);
		for (int i = 0; i < r; i++)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					alive[0][i][j] = true;
		}
		int res = 0;
		bool hasAlive = true;
		for(; hasAlive; res++)
		{
			hasAlive = false;
			bool cur = (res & 1);
			memset(alive[!cur], 0, sizeof(alive[!cur]));
			for (int i = 1; i <= 100; i++)
				for (int j = 1; j <= 100; j++)
				{
					if (
						(alive[cur][i][j] && (alive[cur][i - 1][j] || alive[cur][i][j - 1])) ||
						(alive[cur][i - 1][j] && alive[cur][i][j - 1])
						)
						hasAlive = alive[!cur][i][j] = true;
				}
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}