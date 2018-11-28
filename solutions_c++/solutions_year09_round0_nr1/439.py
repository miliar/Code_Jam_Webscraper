#include <cstdio>
#include <cstring>

int l, d, n;

char str[5010][25];
bool has[25][32];
char buff[10000];

int main()
{
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; ++i) {
		scanf("%s", str[i]);
	}
	for (int t = 1; t <= n; ++t) {
		memset(has, false, sizeof(has));
		bool inside = false;
		int ind = 0;
		scanf("%s", buff);
		for (int ii = 0; buff[ii]; ++ii) {
			char ch = buff[ii];
			if (ch == '(') inside = true;
			else if (ch == ')') {
				inside = false;
				++ind;
			}
			else {
				has[ind][ch - 'a'] = true;
				if (!inside) ++ind;
			}
		}
		int num = 0;
		for (int i = 0; i < d; ++i) {
			bool flag = true;
			for (int j = 0; j < l; ++j) {
				if (!has[j][str[i][j] - 'a']) {
					flag = false;
					break;
				}
			}
			if (flag) ++num;
		}
		printf("Case #%d: %d\n", t, num);
	}
	return 0;
}