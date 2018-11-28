#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int nCase = 1; nCase <= t; ++nCase) {
		int c;
		scanf("%d", &c);
		char cm[128][128] = {};
		for (int i = 0; i < c; ++i) {
			char buf[9];
			scanf("%s", buf);
			cm[buf[0]][buf[1]] = buf[2];
			cm[buf[1]][buf[0]] = buf[2];
		}
		int d;
		scanf("%d", &d);
		bool dm[128][128] = {};
		for (int i = 0; i < d; ++i) {
			char buf[9];
			scanf("%s", buf);
			dm[buf[0]][buf[1]] = true;
			dm[buf[1]][buf[0]] = true;
		}
		int n;
		char str[110];
		scanf("%d%s", &n, str);
		vector<char>ans;
		for (int i = 0; i < n; ++i) {
			ans.push_back(str[i]);
			char ch;
			while (ans.size() > 1 && (ch = cm[ans[ans.size() - 2]][ans[ans.size() - 1]]) != 0) {
				ans.pop_back();
				ans.pop_back();
				ans.push_back(ch);
			}
			ch = ans.back();
			for (int i = 0; i < ans.size() - 1; ++i) {
				if (dm[ch][ans[i]]) {
					ans.clear();
					break;
				}
			}
		}
		printf("Case #%d: [", nCase);
		for (int i = 0; i < ans.size(); ++i) {
			if (i != 0) {
				printf(", ");
			}
			printf("%c", ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
