#include <iostream>
#include <map>
#include <string>

using namespace std;
map<string, int> hash[1<<16];

int main() {
	freopen("E://in.txt", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	int t, n, m, tc = 0;
	char str[1024];
	char s[1024];
	scanf("%d", &t);
	while(t--) {
		scanf("%d%d", &n, &m);
		int key = 0;
		int root = 0;
		int ans = 0;
		hash[0].clear();
		while(n--) {
			scanf("%s", str);
			int len = strlen(str);
			str[len++] = '/';
			str[len] = 0;
			int k = 0;
			root = 0;
			for(int i = 1; str[i]; i++) {
				if(str[i] != '/') s[k++] = str[i];
				else {
					s[k] = 0;
					int val = hash[root][s];
					if(val == 0) {
						val = hash[root][s] = ++key;
						hash[val].clear();
					}
					k = 0;
					root = val;
				}
			}
		}
		while(m--) {
			scanf("%s", str);
			int len = strlen(str);
			str[len++] = '/';
			str[len] = 0;
			int k = 0;
			root = 0;
			for(int i = 1; str[i]; i++) {
				if(str[i] != '/') s[k++] = str[i];
				else {
					s[k] = 0;
					int val = hash[root][s];
					if(val == 0) {
						val = hash[root][s] = ++key;
						hash[val].clear();
						ans++;
					}
					k = 0;
					root = val;
				}
			}
		}
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}