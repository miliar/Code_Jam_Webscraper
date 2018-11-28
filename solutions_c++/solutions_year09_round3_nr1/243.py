#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;
#define MAX_L 100
#define llong long long

int main(int argc, char* argv[]) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int cas;
	for (cas = 1; cas <= T; ++cas) {
		char buf[MAX_L];
		scanf("%s", buf);
		int len = strlen(buf);
		map<char, int> M;
		M.clear();
		int i;
		int m = -1;
		for (i = 0; i < len; ++i) {
			if (i == 0) {
				M.insert(make_pair(buf[i], 1));	
			} else {
				if (M.find(buf[i]) == M.end()) {
					if (m == -1) {
						M.insert(make_pair(buf[i], 0));
						m = 0;
					} else if (m == 0) {
						M.insert(make_pair(buf[i], 2));
						m = 2;
					} else {
						m++;
						M.insert(make_pair(buf[i], m));	
					}
				}
			}
		}	
		if (m < 2) {
			m = 2;
		} else {
			m++;
		}
		llong res = 0;
		llong base = 1;
		for (i = len - 1; i >= 0; --i) {
			int k = M[buf[i]];
			res += k * base;
			base *= m;
		}
		printf("Case #%d: %I64d\n", cas, res);
	}
	return EXIT_SUCCESS;
}
