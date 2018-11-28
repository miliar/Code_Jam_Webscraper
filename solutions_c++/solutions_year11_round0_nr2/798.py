#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int T, n;
char s[101];
char comb[256][256];
bool oppo[256][256];

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		memset(comb, -1, sizeof(comb));
		memset(oppo, 0, sizeof(oppo));
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s);
			int a = s[0], b = s[1];
			comb[a][b] = comb[b][a] = s[2];
		}
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s);
			int a = s[0], b = s[1];
			oppo[a][b] = oppo[b][a] = true;
		}
		vector <char> v;
		scanf("%d%s", &n, s);
		for (int i = 0; i < n; ++i) {
			int cur = s[i];
			if (!v.empty() && comb[(int)v.back()][cur] != -1) {
				char t = comb[(int)v.back()][cur];
				v.pop_back();
				v.push_back(t);
			} else {
				bool clear = false;
				for (int j = 0; j < (int)v.size(); ++j) {
					if (oppo[(int)v[j]][cur]) {
						v.clear();
						clear = true;
						break;
					}
				}
				if (!clear) {
					v.push_back(s[i]);
				}
			}
		}
		printf("Case #%d: [", caseNum);
		for (int i = 0; i < (int)v.size(); ++i) {
			i > 0 && printf(", ");
			printf("%c", v[i]);
		}
		printf("]\n");
	}
	return 0;
}
