#include <cstdio>
#include <vector>

using namespace std;

int n, d;
vector<pair<int, int> > P;

int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int r;
		int case_no = 0;
		scanf("%d", &r);
		while (r--) {
				P.clear();
				scanf("%d %d", &n, &d);
				for (int i = 0; i < n; ++i) {
						int pos, v;
						scanf("%d %d", &pos, &v);
						P.push_back(make_pair(pos, v));
				}

				long long maxv = 0;
				for (int i = 0; i < n; ++i) {
						int total = 0;
						long long tmp;
						for (int j = i; j < n; ++j) {
								total += P[j].second;
								tmp = (long long)(total - 1) * d - (P[j].first - P[i].first);
								if (tmp > maxv) maxv = tmp;
						}
				}
				printf("Case #%d: %I64d.%s\n", ++case_no, maxv / 2, (maxv % 2) ? "5" : "0");
		}
} 