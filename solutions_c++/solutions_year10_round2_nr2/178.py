#include <iostream>
#include <algorithm>
using namespace std;

const int maxN = 55;

struct Tur
{
	int x, v;
} P[maxN];

bool operator< (const Tur &a, const Tur &b)
{
	return a.x < b.x;
}

int main()
{
	int C;
	cin >> C;
	for (int _C = 1; _C <= C; _C ++)
	{
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		for (int i = 0; i < N; i ++) cin >> P[i].x;
		for (int i = 0; i < N; i ++) cin >> P[i].v;
		sort(P, P + N);
		int ans = 0;
		for (int i = N - 1; i >= 0; i --)
		{
			if (B - P[i].x > P[i].v * T) ans += K; else K --;
			if (K == 0) break;
		}
		printf("Case #%d: ", _C);
		if (K == 0) printf("%d\n", ans); else printf("IMPOSSIBLE\n");
	}
}
