#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <cstring>
using namespace std;

int t, e, n, c, i, it;
char token[1000];
set<string> exist;
vector<string> maj;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		c = 0;
		scanf("%d%d\n", &e, &n);
		exist.clear();
		while(--e >= 0) {
			gets(token);
			exist.insert(token);
		}
		maj.clear();
		while(--n >= 0) {
			gets(token);
			if(!exist.count(token)) {
				exist.insert(token);
				++c;
				i = strlen(token);
				while(--i > 0) {
					if(token[i] == '/') {
						token[i] = '\0';
						if(!exist.count(token)) {
							++c;
							exist.insert(token);
						} else { break; }
					}
				}
			}
		}
		printf("Case #%d: %d\n", it, c);
	}
	return 0; }