#include <cstdio>
#include <queue>
#include <vector>
#include <map>

using namespace std;

const int MAXN = 40;

int n;

char maze[MAXN][MAXN + 10];
int last[MAXN];

bool done(const vector<int> &v)
{
	for (int i = 0; i < v.size(); ++i) {
		if (last[v[i]] > i) {
			return false;
		}
	}
	return true;
}

int run()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%s", maze[i]);
	for (int i = 0; i < n; ++i) {
		last[i] = -1;
		for (int j = n - 1; j >= 0; --j) {
			if (maze[i][j] == '1') {
				last[i] = j;
				break;
			}
		}
	}
	vector<int> v;
	for (int i = 0; i < n; ++i) {
		v.push_back(last[i]);
	}
	int sum = 0;
	for (int i = 0; i < n; ++i) {
		int j;
		for (j = 0; j < n - i; ++j) {
			if (v[j] <= i) {
				break;
			}
		}
		sum += j;
		v.erase(v.begin() + j);
	}
	return sum;
}

int main()
{
	freopen("Ain2.txt", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}