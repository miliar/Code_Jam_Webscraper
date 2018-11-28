#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>

using namespace std;

int t, n;
vector<int> o, b;
pair<char, int> order[110];

void solve();
int get_ans();

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		solve();
	return 0;
}

void solve() {
	scanf("%d", &n);
	o.clear();
	b.clear();
	for (int i = 0; i < n; ++i) {
		char buf[8];
		int p;
		scanf("%s%d", buf, &p);
		order[i] = make_pair(buf[0], p);
		if (buf[0] == 'O')
			o.push_back(p);
		else
			b.push_back(p);
	}
	printf("Case #%d: %d\n", ++t, get_ans());
}

int get_ans() {
	int p = 1, q = 1, x = 0, y = 0, ans = 0;
	for (int i = 0; i < n; ++i) {
		//printf("-- %d %d\n", p, q);
		if (order[i].first == 'O') {
			int tmp = abs(order[i].second - p) + 1;
			ans += tmp;
			p = order[i].second;
			++x;
			if (y < b.size()) {
				if (b[y] > q)
					q = (b[y] - q > tmp ? q + tmp : b[y]);
				else
					q = (q - b[y] > tmp ? q - tmp : b[y]);
			}
		} else {
			int tmp = abs(order[i].second - q) + 1;
			ans += tmp;
			q = order[i].second;
			++y;
			if (x < o.size()) {
				if (o[x] > p)
					p = (o[x] - p > tmp ? p + tmp : o[x]);
				else
					p = (p - o[x] > tmp ? p - tmp : o[x]);
			}
		}
	}
	return ans;
}
