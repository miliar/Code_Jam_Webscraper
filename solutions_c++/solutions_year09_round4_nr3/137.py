#include <cstdio>
#include <cstring>

//最大匹配  记得边的方向是图的左边往右
//speed: ??
//range: ??
const int MaxN = 20930;
const int MaxM = 503271;
const int BIGNUM = 1000000000;

int Link[MaxN], Edge[MaxM][2], EdgeNum;
int P[MaxN], Visd[MaxN];
int Case, Flag;

void Setup_Map() {
     memset(Link, 0, sizeof Link);
     EdgeNum = 0;
}

//插入边，边默认为单向，2个参数分别为起点、终点
void Edge_Insert(int x, int y) {
     int Tmp = Link[x];
     EdgeNum ++;
     Edge[EdgeNum][0] = y;
     Edge[EdgeNum][1] = Tmp;
     Link[x] = EdgeNum;
}

void Solve(int Cur, int Null, int L, int R) {
	for (int i = Link[Cur]; i; i = Edge[i][1]) {
		int Next = Edge[i][0];
		if (Visd[Next] == Case || Next < L || Next > R) continue;
		if (P[Next] == Null) {
			P[Next] = Cur;
			Flag = 1;
			return;
		}
		Visd[Next] = Case;
		int Tmp = P[Next];
		P[Next] = Cur;
		Solve(Tmp, Null, L, R);
		if (Flag) return;
		P[Next] = Tmp;
	}
}

//算点a~b与点c~d的最大匹配 
int Match(int a, int b, int c, int d) {
	int Ans = 0;
	Case = 1;
	for (int i = c; i <= d; i ++) {
		Visd[i] = 0;
		P[i] = a - 1;
	}
	for (int i = a; i <= b; i ++) {
		Flag = 0;
		Solve(i, a - 1, c, d);
		Ans += Flag;
		Case ++;
	}
	return Ans;
}

int N;
int K;
int price[100][25];

void init() {
	Setup_Map();

	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < K; j++)
			scanf("%d", &price[i][j]);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			bool ok = true;
			for (int k = 0; k < K && ok; k++)
				if (price[i][k] >= price[j][k])
					ok = false;
			if (ok) Edge_Insert(i + 1, N + j + 1);
		}
}

void solve() {
	int ans = Match(1, N, N + 1, 2 * N);
	printf("%d\n", N - ans);
}

int main() {
	freopen("p3.in", "r", stdin);
	freopen("p3.out", "w", stdout);

	int Case; scanf("%d", &Case);
	for (int i = 0; i < Case; i++) {
		init();
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}

