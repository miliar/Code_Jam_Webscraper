#include <cstdio>
#include <string>

int main() {
	int T, idx = 0; scanf("%d", &T);
	while (T--) {
		int s, q; scanf("%d", &s);
		char S[s][110], tmp[110]; gets(tmp);
		int count = 0, ans = 0;
		bool vs[s];
		for (int i = 0; i < s; ++i) {
			gets(S[i]);
		}
		scanf("%d", &q); gets(tmp);
		memset(vs, 0, sizeof(vs));
		for (int k = 0; k < q; ++k) {
			gets(tmp);
			//printf("%s %d %d\n", tmp, count, ans);
			for (int i = 0; i < s; ++i) {
				if (!strcmp(S[i], tmp)) {
					count += !vs[i];
					vs[i] = 1;
					if (count == s) {
						memset(vs, 0, sizeof(vs));
						vs[i] = 1;
						++ans;
						count = 1;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", ++idx, ans);
	}
	return 0;
}
