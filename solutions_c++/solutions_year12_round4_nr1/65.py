#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

#define oo 10005

int N, D;
struct Tnode{
	int x, y;
}	a[oo];
int f[oo];

bool comp(const Tnode & A, const Tnode &B) {
	return A.x < B.x;
}

inline void Readin() {
	scanf("%d", &N);
	
	for (int i=1; i<=N; ++i)
		scanf("%d%d", &a[i].x, &a[i].y);
	scanf("%d", &D);
	a[0].x = 0, a[0].y =0;
	a[N+1].x = D, a[N+1].y = 0;
	
	//sort(a, a+N+2, comp);
}

inline void Solve() {
	memset(f, -1, sizeof f);
	f[0] = 0;
	f[1] = a[1].x;
	for (int i=1; i<=N+1; ++i)
		for (int j=i+1; j<=N+1; ++j)
			if (a[i].x + f[i] >= a[j].x)
				f[j] = max(f[j], min(a[j].y, a[j].x - a[i].x));
	
	if (f[N+1] != -1) puts("YES");
	else puts("NO");
}

int main() {
	int Test, Case;
	scanf("%d", &Test);
	for (Case =1; Case <= Test; ++Case) {
		printf("Case #%d: ", Case);
		Readin();
		Solve();
	}

	return 0;
}