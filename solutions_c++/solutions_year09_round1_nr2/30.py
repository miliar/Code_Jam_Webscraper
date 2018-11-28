#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

#define SS 0
#define WW 1
#define EE 2

using namespace std;

typedef long long Int64;

const int maxn = 100;
const int maxv = 40000;
const int maxe = 160000;
const Int64 inf = 1000000000000000000LL;

struct Edge {
	int data, kind, S, W, T, next;
	
	Edge() {
	}
	
	Edge(int data, int kind, int S, int W, int T, int next) : data(data), kind(kind), S(S), W(W), T(T), next(next) {
	}
};

Edge edge[maxe];
int list[maxv];
int code[maxn][maxn][4];
Int64 minpath[maxv];
bool used[maxv];
int n, m, e, pop;

void Add_Link(int a, int  b, int kind, int S, int W, int T) {
	edge[e] = Edge(b, kind, S, W, T, list[a]);
	list[a] = e++;
	edge[e] = Edge(a, kind, S, W, T, list[b]);
	list[b] = e++;
}

Int64 Predict_S(int S, int W, int T, Int64 curr) {
	Int64 base = S + W;
	Int64 p = ((curr - T) % base + base) % base;
	if (p < S) return curr;
	return base - p + curr;
}

Int64 Predict_W(int S, int W, int T, Int64 curr) {
	Int64 base = S + W;
	Int64 p = ((curr - T) % base + base) % base;
	if (p >= S) return curr;
	return S - p + curr;
}

void Solve() {
	scanf("%d %d", &n, &m);
	pop = 0;
	int i, j, k;
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			for (k = 0; k < 4; k++)
				code[i][j][k] = pop++;
	e = 0;
	for (i = 0; i < pop; i++)
		list[i] = -1;
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++) {
			int S, W, T;
			scanf("%d %d %d", &S, &W, &T);
			Add_Link(code[i][j][0], code[i][j][1], SS, S, W, T);
			Add_Link(code[i][j][0], code[i][j][3], WW, S, W, T);
			Add_Link(code[i][j][1], code[i][j][2], WW, S, W, T);
			Add_Link(code[i][j][2], code[i][j][3], SS, S, W, T);
			if (i + 1 < n) {
				Add_Link(code[i][j][1], code[i + 1][j][0], EE, 0, 0, 0);
				Add_Link(code[i][j][2], code[i + 1][j][3], EE, 0, 0, 0);
			}
			if (j + 1 < m) {
				Add_Link(code[i][j][0], code[i][j + 1][3], EE, 0, 0, 0);
				Add_Link(code[i][j][1], code[i][j + 1][2], EE, 0, 0, 0);
			}
		}
	for (i = 0; i < pop; i++) {
		minpath[i] = inf;
		used[i] = 0;
	}
	int start = code[n - 1][0][2], finish = code[0][m - 1][0];
	minpath[start] = 0;
	//printf("start = %d\n", start);
	int who, succ;
	Int64 mm;
	while (1) {
		mm = inf;
		for (i = 0; i < pop; i++)
			if (!used[i] && minpath[i] < mm) {
				who = i;
				mm = minpath[i];
			}
		if (mm == inf) break;
		used[who] = 1;
		//printf("who = %d\n", who);
		if (who == finish) break;
		for (i = list[who]; i != -1; i = edge[i].next) {
			succ = edge[i].data;
			if (used[succ]) continue;
			switch(edge[i].kind) {
				case EE : {
					minpath[succ] = min(minpath[succ], mm + 2);
				} break;
				case SS : {
					minpath[succ] = min(minpath[succ], Predict_S(edge[i].S, edge[i].W, edge[i].T, mm) + 1);
				} break;
				case WW : {
					minpath[succ] = min(minpath[succ], Predict_W(edge[i].S, edge[i].W, edge[i].T, mm) + 1);
				} break;
			}
		}
	}
	printf("%I64d\n", minpath[finish]);
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
