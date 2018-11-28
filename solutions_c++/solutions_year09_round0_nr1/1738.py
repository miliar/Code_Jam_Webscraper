#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
char t[5009][20];
int key[20][200];
int l, d, n;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	while (scanf("%d %d %d", &l, &d, &n)==3) {
		for (int i=0; i<d; ++i) scanf("%s", t[i]);
		memset(key, -1, sizeof(key));
		int cas = 0;
		for (int i=0; i<n; ++i) {
			char s[600];
			scanf("%s", s);
			for (int j=0,k=0; j<l; ++j,++k) {
				if (s[k]=='(') {
					++k;
					for (; s[k]!=')'; ++k)
						key[j][s[k]] = i;
				}
				else key[j][s[k]] = i;
			}
			int res = 0;
			for (int j=0; j<d; ++j) {
				bool flag = true;
				for (int k=0; k<l; ++k) if (key[k][t[j][k]]!=i) {
					flag = false;
					break;
				}
				res += flag;
			}
			printf("Case #%d: %d\n", ++cas, res);
		}
	}
	return 0;
}
			

