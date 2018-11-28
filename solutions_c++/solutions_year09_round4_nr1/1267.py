#include <cstdio>
#include <cstring>

#include <algorithm>
#include <queue>
#include <vector>
#include <set>

using namespace std;

typedef vector<int> TIntVector;
typedef queue< TIntVector > TQueue;

const int MAXN = 100;

int n;
int matrix[MAXN][MAXN];
bool can[MAXN][MAXN];
int maxOne[MAXN];
unsigned int dist[16777216 + 100];

int IndexOf(const TIntVector& pos) {
	int result = 0;
	for (size_t i = 0; i < pos.size(); ++i)
		result = n*result + pos[i];
	return result;
}

bool IsGood(const TIntVector& pos) {
	for (size_t i = 0; i < pos.size(); ++i)
		if (!can[i][pos[i]])
			return false;
	return true;
}

int main() {
	// freopen("input.txt", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);

	int nT;
	scanf("%d", &nT);
	for (int t = 0; t < nT; ++t) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			char buffer[MAXN];
			scanf("%s", buffer);
			for (int j = 0; j < n; ++j)
				matrix[i][j] = buffer[j] != '0';
		}

		memset(maxOne, -1, sizeof(maxOne));

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (matrix[i][j])
					maxOne[i] = j;

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				can[i][j] = maxOne[i] <= j;

		TIntVector pos;
		for (int i = 0; i < n; ++i)
			pos.push_back(i);
		
		memset(dist, -1, sizeof(dist));
		dist[IndexOf(pos)] = 0;
		
		TQueue q;
		q.push(pos);

		while (!IsGood(q.front())) {
			TIntVector current = q.front();
			int curIndex = IndexOf(current);
			q.pop();
			for (int i = 1; i < n; ++i) {
				swap(current[i - 1], current[i]);
				int index = IndexOf(current);
				if (dist[index] == (unsigned int)-1) {
					dist[index] = dist[curIndex] + 1;
					q.push(current);
				}
				swap(current[i - 1], current[i]);
			}
		}
		
		printf("Case #%d: %d\n", t + 1, dist[IndexOf(q.front())]);
	}

	return 0;
}