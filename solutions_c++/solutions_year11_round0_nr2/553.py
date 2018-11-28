#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
const int MAXN = 1007;
int g[30][30], g2[30][30];
char ord[120];
int has[30];


int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	int t, n, var = 0;
	scanf("%d", &t);
	while (t -- ) {
		scanf("%d", &n);
		memset(g, -1, sizeof g);
		memset(g2, -1, sizeof g2);
		memset(has, 0, sizeof has);
		while ( n -- ) {
			scanf(" %s", ord);
			g[ord[0]-'A'][ord[1]-'A'] = ord[2]-'A';
			g[ord[1]-'A'][ord[0]-'A'] = ord[2]-'A';
		}
		scanf("%d", &n);
		while ( n -- ) {
			scanf(" %s", ord);
			g2[ord[0]-'A'][ord[1]-'A'] = -2;
			g2[ord[1]-'A'][ord[0]-'A'] = -2;
		}
		scanf("%d %s", &n, ord);
		vector < int > ans;
 		for (int i = 0 ; i < n ; i ++ ) {
			int id = ord[i] - 'A';
			if (ans.size() && g[id][ans[ans.size()-1]] >= 0) {
				int last = ans[ans.size()-1];
				ans.pop_back();
				ans.push_back(g[id][last]);
			} else {
				ans.push_back(id);
				for (int j = 0 ; j < ans.size() ; j ++ ) {
					if (g2[id][ans[j]] == -2) {
						ans.clear();
						break;
					}
				}
			}
			/*printf("[");
			for (int i = 0 ; i < ans.size() ; i ++ ) {
				if (i) printf(", ");
				printf("%c", ans[i] + 'A');
			}
			printf("]\n");*/
		}
		printf("Case #%d: ", ++var);
		printf("[");
		for (int i = 0 ; i < ans.size() ; i ++ ) {
			if (i) printf(", ");
			printf("%c", ans[i] + 'A');
		}
		printf("]\n");
	}
	return 0;
}