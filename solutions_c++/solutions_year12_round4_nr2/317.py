#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

const int MaxN = 1005;
const int oo = 0x3F3F3F3F;

int N, W, L;
int r[MaxN];
int idx[MaxN];

struct Node {
	int L, R, h;
	Node() { }
	Node(int L, int R, int h) : L(L), R(R), h(h) { }
	bool operator<(const Node& other) const {
		if (L != other.L) return L < other.L;
		else if (R != other.R) return R < other.R;
		else return h < other.h;
	}
};

vector<Node> v;
pair<int, int> ret[MaxN];

int find(int L, int R) {
	int h = -1;
	for (int i = 0; i < (int)v.size(); i++) {
		if (v[i].L < R && v[i].R > L) h = max(h, v[i].h);
	}
	if (h == -1) return ::L + 1;
	else return h;
}

bool check() {
	int last = 0, bound, x, y;
	v.clear();
	v.push_back(Node(-oo, oo, 0));
	
	// for (int i = 0; i < N; i++)
		// printf("%d ", idx[i]);
	// puts("");
	
	for (int i = 0; i < N; i++) {
		if (last == 0) bound = last + r[idx[i]];
		else bound = last + 2 * r[idx[i]];
		x = bound - r[idx[i]];
		if (x > W) {
			last = 0;
			i--;
			continue;
		}
		// printf("find last = %d bound = %d %d %d\n", last, bound, x - r[idx[i]], x + r[idx[i]]);
		y = find(x - r[idx[i]], x + r[idx[i]]);
		if (y) y += r[idx[i]];
		// printf("y = %d L = %d\n", y, L);
		if (y > L) return false;
		last = bound;
		ret[idx[i]] = make_pair(x, y);
		v.push_back(Node(x - r[idx[i]], x + r[idx[i]], y + r[idx[i]]));
	}
	for (int i = 0; i < N; i++)
		printf(" %d.0 %d.0", ret[i].first, ret[i].second);
	puts("");
	return true;
}

void sol() {
	for (int i = 0; i < N; i++) idx[i] = i;
	
	// puts("");
	// do {
		if (check()) return;
	// } while (next_permutation(idx, idx + N));
	
	printf(" Failed\n");
}

int main() {
	int T, cas = 1;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d:", cas++);
		scanf("%d%d%d", &N, &W, &L);
		for (int i = 0; i < N; i++)
			scanf("%d", &r[i]);
		sol();
	}
	
	return 0;
}
