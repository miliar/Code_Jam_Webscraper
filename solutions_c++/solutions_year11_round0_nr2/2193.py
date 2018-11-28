#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

int com[26][26];
bool del[26][26];

int main() {
	int T;
	scanf("%d", &T);
	for (int C = 1; C <= T; C++) {

		memset(com, -1, sizeof(com));
		int n;
		for (scanf("%d", &n); n; n--) {
			char a, b, r;
			scanf(" %c%c%c", &a, &b, &r);
			a -= 'A';
			b -= 'A';
			r -= 'A';
			com[a][b] = r;
			com[b][a] = r;
		}

		CLEAR(del);
		for (scanf("%d", &n); n; n--) {
			char a, b;
			scanf(" %c%c", &a, &b);
			a -= 'A';
			b -= 'A';
			del[a][b] = true;
			del[b][a] = true;
		}

		vector<int> v;
		for (scanf("%d", &n); n; n--) {
			char a;
			scanf(" %c", &a);
			a -= 'A';
			if (!v.empty() && com[v.back()][a] != -1)
				v.back() = com[v.back()][a];
			else {
				v.push_back(a);
				FOREACH(i, v)
					if (del[*i][a]) {
						v.clear();
						break;
					}
			}
		}

		printf("Case #%d: [", C);
		for (int i = 0; i < int(v.size())-1; i++)
			printf("%c, ", v[i]+'A');
		if (!v.empty())
			printf("%c", v.back()+'A');
		printf("]\n");
	}

}
