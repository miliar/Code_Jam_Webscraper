#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int t, n, m, r;
long long c, sum;
long long value;
int cur;

vector<long long> v;
pair<long long, int> memo[1000];
int visit[1000];
vector<long long> q;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &t);
	for(int i = 0; i < t; ++i) {
		scanf("%d %d %d", &n, &m, &r);

		sum = 0;
		v.clear();
		for(int j = 0; j < r; ++j) {
			scanf("%lld", &c);
			v.push_back(c);
			sum += c;
		}

		value = 0;
		for(int j = 0; j < r; ++j) {
			memo[j].first = 0;
			memo[j].second = (j + r - 1) % r;
			for(int k = 0; k < r; ++k) {
				if (memo[j].first + v[(j + k)%r] <= m) {
					memo[j].first += v[(j + k)%r];
					memo[j].second = (j + k) % r;
				}
				else break;
			}
		}

		q.clear();
		memset(visit, 0, sizeof(visit));
		cur = 0;
		for(int j = 0; j < n; ++j) {			
			if (visit[cur] != 0) {
				int sz = j - visit[cur] + 1;

				sum = 0;
				for(int k = visit[cur] - 1; k < q.size(); ++k)
					sum += q[k];

				value += ((n - j) / sz) * sum;

				for(int k = 0; k < (n - j) % sz; ++k)
					value += q[visit[cur] - 1 + k];

				break;
			}

			visit[cur] = j + 1;
			q.push_back(memo[cur].first);
			value += memo[cur].first;
			cur = (memo[cur].second + 1) % r;
		}

		printf("Case #%d: %lld\n", i + 1, value);
	}

	return 0;
}