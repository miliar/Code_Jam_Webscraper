#include <cstdio>
#include <cstring>
#include <map>
#include <set>

using namespace std;

int n, m;
char dict[10000][11];
char order[100][27];
int top[11];
map<int, int> kid[11][10000 * 30];
int mask[11][10000 * 30];

void init()
{
	
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", dict[i]);
	}
	for (int i = 0; i < m; i++) {
		scanf("%s", order[i]);
	}
}

void work()
{
	int ans;
	for (int i = 0; i < m; i++) {
		for (int j = 1; j <= 10; j++) {
			kid[j][0].clear();
			mask[j][0] = 0;
			top[j] = 0;
		}
		for (int j = 0; j < n; j++) {
			int s = 0, len = strlen(dict[j]);
			for (int k = 0; k < len; k++) {
				s |= 1 << (dict[j][k] - 'a');
			}
			int u = 0;
			mask[len][0] |= s;
			for (int k = 0; k < 26; k++) {
				int ch = 0;
				for (int l = 0; l < len; l++) {
					if (dict[j][l] == order[i][k]) ch |= (1 << l);
				}
				if (kid[len][u][ch] == 0) {
					kid[len][u][ch] = ++top[len];
					kid[len][top[len]].clear();
					mask[len][top[len]] = 0;
				}
				u = kid[len][u][ch];
				mask[len][u] |= s;
			}
		}
		
		int maxi = -1;
		for (int j = 0; j < n; j++) {
			int s = 0, u = 0, len = strlen(dict[j]), cur = 0;
			for (int k = 0; k < len; k++) {
				s |= 1 << (dict[j][k] - 'a');
			}
			for (int k = 0; k < 26; k++) {
				int ch = 0;
				for (int l = 0; l < len; l++) {
					if (dict[j][l] == order[i][k]) ch |= (1 << l);
				}
				if (s & (1 << (order[i][k] - 'a'))) s -= (1 << order[i][k]);
				if (s == 0) break;
				if (ch == 0 && (mask[len][u] & (1 << (order[i][k] - 'a')))) cur++;
				u = kid[len][u][ch];
			}
			if (cur > maxi) {
				maxi = cur;
				ans = j;
			}
		//	printf("%d %d\n", j, cur);
		}
		printf("%s", dict[ans]);
		if (i != m - 1) printf(" ");
	}
	printf("\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%d: ", tt);
		init();
		work();
	}
}