#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

typedef pair <int, int> PII;

void run(set <PII>& st) {
	set <PII> res;
	for (set <PII>::iterator it = st.begin(); it != st.end(); it++) {
		if (st.find(make_pair(it->first - 1, it->second)) == st.end() && st.find(make_pair(it->first, it->second - 1)) == st.end()) {
			continue;
		}
		res.insert(*it);
	}
	for (set <PII>::iterator it = st.begin(); it != st.end(); it++) {
		if (st.find(make_pair(it->first - 1, it->second + 1)) != st.end()) {
			res.insert(make_pair(it->first, it->second + 1));
		}
	}
	st = res;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n, x1, y1, x2, y2;
		scanf("%d", &n);
		set <PII> st;
		for (int i = 0; i < n; i++) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int j = x1; j <= x2; j++) {
				for (int k = y1; k <= y2; k++) {
					st.insert(make_pair(j, k));
				}
			}
		}
		int res = 0;
		while (!st.empty()) {
			run(st);
			res++;
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
