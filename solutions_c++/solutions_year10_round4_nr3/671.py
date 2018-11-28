#include <cstdio>

const int maxn = 1000;

struct TRec {
	int px1, py1, px2, py2;
};

int casei, cases, n, ans, m;
int set[maxn], remain[maxn];
//bool tag[maxn];
TRec recs[maxn];

inline void init() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d%d", &recs[i].px1, &recs[i].py1, &recs[i].px2, &recs[i].py2);
		//tag[i] = false;
		remain[i] = i;
	}
}

inline bool intersect(int n1, int n2) {
	if (recs[n1].px1 > recs[n2].px2 + 1) return false;
	if (recs[n2].px1 > recs[n1].px2 + 1) return false;
	if (recs[n1].py1 > recs[n2].py2 + 1) return false;
	if (recs[n2].py1 > recs[n1].py2 + 1) return false;
	return true;
}

inline void DFS(int now) {
	int t = remain[now];
	set[m++] = t;

	remain[now] = remain[n - 1];
	--n;

	bool stop = false;
	while (!stop) {
		stop = true;
		int i = 0;
		while (i < n) {
			if (intersect(remain[i], t)) {
				DFS(i);
				stop = false;
			}
			++i;
		}
	}
}

inline void process() {
	ans = 0;	
	while (n > 0) {
		m = 0;
		DFS(0);

		int maxx = 0, maxy = 0;
		for (int i = 0; i < m; ++i) {
			if (recs[set[i]].px2 > maxx) maxx = recs[set[i]].px2;
			if (recs[set[i]].py2 > maxy) maxy = recs[set[i]].py2;
		}
		int nowans = 0;
		for (int i = 0; i < m; ++i) {
			int t = maxx - recs[set[i]].px1 + maxy - recs[set[i]].py1;
			if (t > ans) ans = t;
		}
		if (nowans > ans) ans = nowans;
	}
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans + 1);
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
