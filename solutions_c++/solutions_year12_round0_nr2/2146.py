#include <cstdio>
#include <vector>
using namespace std;

inline bool surprising(const vector<int> &v) {
	return v[2] - v[0] == 2;
}

int main() {
	int test, cs, n, s, p, ans, sup, i, j, k;
	int scores[128], tmp[3];
	vector< vector< int > > V[31];
	for(i = 0; i <= 10; i++) {
		for(j = i; j <= 10 && j <= i + 2; j++) {
			for(k = j; k <= 10 && k <= i + 2; k++) {
				tmp[0] = i, tmp[1] = j, tmp[2] = k;
				V[i + j + k].push_back(vector< int >(tmp, tmp+3));
			}
		}
	}
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &test);
	for(cs = 1; cs <= test; cs++) {
		scanf("%d %d %d", &n, &s, &p);
		ans = sup = 0;
		for(i = 0; i < n; i++) scanf("%d", &scores[i]);
		for(i = 0; i < n; i++) {
			if(V[scores[i]].size() == 1) {
				if(surprising(V[scores[i]][0])) sup++;
				if(V[scores[i]][0][2] >= p) ans++;
			}
			else {
				if(V[scores[i]][0][2] >= p && V[scores[i]][1][2] >= p) ans++;
				else if(V[scores[i]][0][2] >= p) {
					if(surprising(V[scores[i]][0])) {
						if(sup < s) {
							sup++;
							ans++;
						}
					}
					else ans++;
				}
				else if(V[scores[i]][1][2] >= p) {
					if(surprising(V[scores[i]][1])) {
						if(sup < s) {
							sup++;
							ans++;
						}
					}
					else ans++;
				}
			}
		}
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}