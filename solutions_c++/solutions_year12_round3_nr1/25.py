#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int maxn = 1010;

vector<int> edge[maxn];
bool been[maxn];

bool cross(int at) {
	if (been[at]) return true;
	been[at] = true;
	bool ret = false;
	for (int i=0; i<edge[at].size(); i++) {
		ret |= cross(edge[at][i]);
	}
	return ret;
}

void initIO() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int main() {
	initIO();
	int t;
	scanf("%d", &t);
	for (int ti=1; ti<=t; ti++) {
		for (int i=0; i<maxn; i++) {
			edge[i].clear();
		}
		int n;
		scanf("%d", &n);
		for (int i=1; i<=n; i++) {
			int m;
			scanf("%d", &m);
			for (int j=0; j<m; j++) {
				int to;
				scanf("%d", &to);
				edge[i].push_back(to);
			}
		}
		bool result = false;
		for (int i=1; i<=n; i++) {
			memset(been, 0, sizeof(been));
			result |= cross(i);
			
		}
		printf("Case #%d: %s\n", ti, result?"Yes":"No");
	}
	return 0;
}