#include <cstdio>
#include <set>

using namespace std;

const int maxn = 2000;

struct Node {
    int x, y;

    Node() {
    }

    Node(int x, int y) : x(x), y(y) {
    }

    void Input() {
	scanf("%d %d", &x, &y);
	x--;
    }
};

bool operator < (const Node &a, const Node &b) {
    return a.x != b.x ? a.x < b.x : a.y < b.y;
}

int value[maxn];
set<Node> rec[maxn];
int n, m;
bool used[maxn];

void Init() {
    scanf("%d %d", &n, &m);
    int i, j;
    for (i = 0; i < m; i++)
	rec[i].clear();
    Node curr;
    for (i = 0; i < m; i++) {
	scanf("%d", &j);
	while (j--) {
	    curr.Input();
	    rec[i].insert(curr);
	}
    }
    for (i = 0; i < n; i++)
	value[i] = 0;
    for (i = 0; i < m; i++)
	used[i] = 0;
}

void No() {
    printf("IMPOSSIBLE\n");
}

void Work() {
    bool flag = 1;
    int i, j, x;
    Node curr;
    while (flag) {
	flag = 0;
	for (i = 0; i < m; i++)
	    if (rec[i].size() == 1 && rec[i].begin()->y) {
		if (used[i]) continue;
		used[i] = 1;
		flag = 1;
		x = rec[i].begin()->x;
		curr = Node(x, 0);
		value[x] = 1;
		for (j = 0; j < m; j++) {
		    rec[j].erase(curr);
		    if (!rec[j].size()) {
			No();
			return;
		    }
		}
	    }
    }
    for (i = 0; i < n; i++) {
	if (i) printf(" ");
	printf("%d", value[i]);
    }
    printf("\n");
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
	printf("Case #%d: ", i + 1);
	Init();
	Work();
    }
    return 0;
}
