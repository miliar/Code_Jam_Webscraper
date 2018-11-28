#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define PII pair<int, int>

using namespace std;


struct range {
	int a, b;
	range(int A, int B) {
		if (A > B) {
			a = 0; b = -1;
		} else {
			a = A; b = B;
		}
	}
	LL len() {
		return b-a+1;
	}
};

range add(range u, range v) {
	return range(max(u.a, v.a), min(u.b, v.b));
}

range getr(int u, int v, int a) {
	if (a == 0) {
		if (u <= 0 && 0 <= v) return range(0, 1100000); else return range(0, -1);
	} else if (a < 0) {
		return getr(-v, -u, -a);
	} else {
		int t1 = u / a;
		if (u % a != 0) t1++;
		int t2 = v / a;
		if (v % a != 0) t2--;
		return range(t1, t2);		
	}
}

queue<PII> q;
set<PII> used;
LL res;
int w, h;

void push(int x, int y) {
	if (x < 0 || y < 0 || x >= w || y >= h) return;
	if (used.count(MP(x,y)) == 0) {
		res++;
		used.insert(MP(x,y));
		q.push(MP(x,y));
	}
}

void solvecase() {
	int x1, y1, x2, y2, x0, y0;
	scanf("%d%d%d%d%d%d%d%d", &w, &h, &x1, &y1, &x2, &y2, &x0, &y0);
	res = 0;
	if (x1 * y2 - x2 * y1 == 0) {
		used.clear();
		push(x0, y0);
		while (!q.empty()) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			push(x + x1, y + y1);
			push(x + x2, y + y2);
		}
	} else {
		/*
		for (int i = 0; i <= 1100000; i++) {
			range r(0, 1100000);
			int t = x0 + i * x1;
			r = add(r, getr(-t, w-1-t, x2));
			t = y0 + i * y1;
			r = add(r, getr(-t, h-1-t, y2));
			res += r.len();
		}

		LL res2 = res;
*/
		res = 0;
		used.clear();
		push(x0, y0);
		while (!q.empty()) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			push(x + x1, y + y1);
			push(x + x2, y + y2);
		}
/*
		
		if (res != res2) {
			printf("!");
		}
		*/
	}
	printf("%lld", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}