#include <algorithm>
#include <string>
#include <map>
#include <cstdio>
using namespace std;

const int inf = 0x7fffffff;

map<string, int> engines;
int N, f[1000], g[1000];

void update(int id) {
	for (int i = 0; i < N; ++i)
		if (id == i) {
			f[i] = inf;
		} else {
			if (g[i] != inf && g[i] + 1 < f[i])
				f[i] = g[i] + 1;
		}
	int m1 = inf, m2 = inf;
	for (int i = 0; i < N; ++i)
		if (f[i] < m1) {
			m2 = m1;
			m1 = f[i];
		} else if (f[i] < m2) {
			m2 = f[i];
		}
	for (int i = 0; i < N; ++i)
		g[i] = f[i] == m1 ? m2 : m1;
}

int main() {
	int case_count;
	scanf("%d", &case_count);
	for (int case_id = 0; case_id < case_count; ++case_id) {
		int count;
		char buf[1000];

		scanf("%d", &count);
		gets(buf);
		engines.clear();
		for (int i = 0; i < count; ++i) {
			gets(buf);
			engines[buf] = i;
		}
		N = count;

		scanf("%d", &count);
		gets(buf);
		fill(f, f + N, 0);
		fill(g, g + N, 0);
		for (int i = 0; i < count; ++i) {
			gets(buf);
			update(engines[buf]);
		}
		
		int ans = inf;
		for (int i = 0; i < N; ++i)
			if (f[i] < ans)
				ans = f[i];
		printf("Case #%d: %d\n", case_id + 1, ans);
	}
	return 0;
}
