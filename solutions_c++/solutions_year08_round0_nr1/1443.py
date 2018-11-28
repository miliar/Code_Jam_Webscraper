#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

map <string, bool> was;
set <string> names;
set <string>::iterator it;
int c, n, s, i, q, wasn, cnt;
char ss[1000];

int main() {
	scanf("%d", &n);
	for (c = 1; c <= n; c++) {
		was.clear();
		names.clear();
		printf("Case #%d: ", c);
		scanf("%d%*c", &s);
		for (i = 0; i < s; i++) {
			fgets(ss, 1000, stdin);
			was.insert(make_pair(ss, false));
			names.insert(ss);
		}
		cnt = 0;
		scanf("%d%*c", &q);
		wasn = s;
		for (i = 0; i < q; i++) {
			fgets(ss, 1000, stdin);
			if (!was[ss]) {
				was[ss] = true;
				wasn--;
				if (wasn == 0) {
					cnt++;
					for (it = names.begin(); it != names.end(); ++it) {
						was[*it] = false;
					}
					was[ss] = true;
					wasn = s - 1;
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
