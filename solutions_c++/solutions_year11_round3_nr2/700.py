#include <cstdio>
#include <algorithm>
#include <queue>
#define f first
#define s second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int T, L, N, C;
pii a[1111];

ll t, ans, len;

int last[1111];
int time[1111111];
bool boost[1111111];
priority_queue <int> Q;

int main(){
	scanf("%d", &T);
	for (int q = 1; q <= T; q++){
		scanf("%d%lld%d%d", &L, &t, &N, &C);
		
		ans = len = 0;
		for (int i = 0; i < C; i++){
			scanf("%d", &a[i].f);
			a[i].s = i;
			len += ((N - i - 1) / C + 1) * a[i].f;
			last[i] = (N / C) * C + i;
			if (last[i] >= N)
				last[i] -= C;
		}
		
		time[0] = 0;
		for (int i = 1; i <= N; i++){
			time[i] = time[i - 1] + a[(i - 1) % C].f * 2;
			if (time[i] >= t && i != N){
				Q.push(a[i % C].f);
			}
			if (time[i] >  t && time[i - 1] < t){
				Q.push((time[i] - t) / 2);
			}
		}
		time[N + 1] = 2147000000;
		
		int ans = time[N];

		for (; L > 0 && !Q.empty(); L--)
			ans -= Q.top(), Q.pop();
		while (!Q.empty())
			Q.pop();
		printf("Case #%d: %d\n", q, ans);
	}
}
