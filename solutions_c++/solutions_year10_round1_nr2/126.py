#include <iostream>
using namespace std;

const int MaxN = 110;
const int MaxA = 260;
const int MaxV = MaxN * MaxA;
const int MaxE = MaxV * 520;
const int Inf = 1000000010;

int TCase, D, I, M, N, A[MaxN];
int ESum, Head[MaxV], Dist[MaxV], Q[MaxV * 200], QHead, QTail;
bool Use[MaxV];
struct {
	int Ending, Prev, Cost;
} E[MaxE];

int Node(int x, int y) {
	return x * 256 + y + 1;
}

void Ins_Edge(int x, int y, int c) {
	E[++ESum]. Ending = y, E[ESum]. Prev = Head[x], Head[x] = ESum, E[ESum]. Cost = c;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case) {
		//init
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 1; i <= N; ++i)
			scanf("%d", A+i);
		//build graph
		ESum = 0;
		memset(Head, 0, sizeof(Head));
		for (int i = 1; i <= N; ++i)
			for (int j = 0; j <= 255; ++j) {
				int cur = Node(i, j);
				Ins_Edge(Node(i - 1, j), cur, D);
				for (int k = max(0, j - M); k <= min(255, j + M); ++k) {
					Ins_Edge(Node(i, k), cur, I);
					Ins_Edge(Node(i - 1, k), cur, abs(k - A[i]));
				}
			}
		//spfa
		memset(Dist, 63, sizeof(Dist));
		memset(Use, 0, sizeof(Use));
		QTail = 0;
		for (int i = 0; i <= 255; ++i)
			Dist[Q[++QTail] = Node(0, i)] = 0;
		for (QHead = 1; QHead <= QTail; ++QHead) {
			Use[Q[QHead]] = 0;
			for (int i = Head[Q[QHead]]; i; i = E[i]. Prev)
				if (Dist[E[i]. Ending] > Dist[Q[QHead]] + E[i]. Cost) {
					Dist[E[i]. Ending] = Dist[Q[QHead]] + E[i]. Cost;
					if (!Use[E[i]. Ending]) Use[Q[++QTail] = E[i]. Ending] = 1;
				}
		}
		//get answer
		int Ans = Inf;
		for (int i = 0; i < 255; ++i)
			Ans = min(Ans, Dist[Node(N, i)]);
		printf("Case #%d: %d\n", Case, Ans);
	}
	return 0;
}
