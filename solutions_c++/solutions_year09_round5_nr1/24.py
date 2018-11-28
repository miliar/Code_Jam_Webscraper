#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int maxl = 20;
const int maxn = 5;
const int maxq = 1000000;
const int dire[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

char mat[maxl][maxl];
int n, R, C;

struct Point {
	int x, y;
	
	Point() {
	}
	
	Point(int x, int y) : x(x), y(y) {
	}
	
	bool Outside() const {
		return x < 0 || y < 0 || x >= R || y >= C;
	}
};

bool operator < (const Point &a, const Point &b) {
	return a.x != b.x ? a.x < b.x : a.y < b.y;
}

bool operator == (const Point &a, const Point &b) {
	return a.x == b.x && a.y == b.y;
}

bool Conj(const Point &a, const Point &b) {
	int x1 = min(a.x, b.x), x2 = max(a.x, b.x);
	int y1 = min(a.y, b.y), y2 = max(a.y, b.y);
	return x1 == x2 && y1 + 1 == y2 || y1 == y2 && x1 + 1 == x2;
}

struct Status {
	Point posi[maxn];
	
	Status() {
	}
	
	Status(const Status &a) {
		int i;
		for (i = 0; i < n; i++)
			posi[i] = a.posi[i];
	}
	
	Status &operator = (const Status &a) {
		if (this == &a) return *this;
		int i;
		for (i = 0; i < n; i++)
			posi[i] = a.posi[i];
		return *this;
	}
	
	void Formalize() {
		sort(posi, posi + n);
	}
	
	bool Stable() const {
		if (n <= 1) return 1;
		int i, j;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++)
				if (i != j && Conj(posi[i], posi[j])) break;
			if (j >= n) return 0;
		}
		return 1;
	}
	
	bool Dest() const {
		int i;
		char ch;
		for (i = 0; i < n; i++) {
			ch = mat[posi[i].x][posi[i].y];
			if (ch != 'x' && ch != 'w') return 0;
		}
		return 1;
	}
};

bool operator < (const Status &a, const Status &b) {
	int i;
	for (i = 0; i < n; i++) {
		if (a.posi[i] < b.posi[i]) return 1;
		if (b.posi[i] < a.posi[i]) return 0;
	}
	return 0;
}

map<Status, int> rec;
Status queue[maxq];
int head, tail;

void Solve() {
	scanf("%d %d", &R, &C);
	int i, j;
	for (i = 0; i < R; i++)
		for (j = 0; j < C; j++)
			scanf(" %c", &mat[i][j]);
	Status start;
	n = 0;
	for (i = 0; i < R; i++)
		for (j = 0; j < C; j++)
			if (mat[i][j] == 'o' || mat[i][j] == 'w') start.posi[n++] = Point(i, j);
	start.Formalize();
	if (start.Dest()) {
		printf("0\n");
		return;
	}
	queue[0] = start;
	rec.clear();
	rec[start] = 0;
	Status curr, succ;
	bool stable;
	set<Point> ss;
	for (head = tail = 0; head <= tail; head++) {
		curr = queue[head];
		int step = rec[curr];
		stable = curr.Stable();
		ss.clear();
		for (i = 0; i < n; i++)
			ss.insert(curr.posi[i]);
		for (i = 0; i < n; i++) {
			Point dot = curr.posi[i];
			for (j = 0; j < 4; j++) {
				int dx = dire[j][0];
				int dy = dire[j][1];
				Point prev = dot, next = dot;
				prev.x -= dx;
				prev.y -= dy;
				next.x += dx;
				next.y += dy;
				if (prev.Outside() || next.Outside()) continue;
				if (mat[prev.x][prev.y] == '#' || mat[next.x][next.y] == '#') continue;
				if (ss.find(prev) != ss.end() || ss.find(next) != ss.end()) continue;
				succ = curr;
				succ.posi[i] = next;
				succ.Formalize();
				if (!stable && !succ.Stable()) continue;
				if (rec.find(succ) == rec.end()) {
					queue[++tail] = succ;
					rec[succ] = step + 1;
					if (succ.Dest()) {
						printf("%d\n", step + 1);
						return;
					}
				}
			}
		}
	}
	printf("-1\n");
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
