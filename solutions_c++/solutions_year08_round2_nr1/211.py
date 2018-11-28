#include <cstdio>
using namespace std;
#define MAXN 100000
int main() {
	int N;
	scanf("%d", &N);
	for (int T=1; T<=N; T++) {
		unsigned long long int n, A, B, C, D, x0, y0, M;
		scanf("%llu%llu%llu%llu%llu%llu%llu%llu", &n, &A, &B, &C, &D, &x0, &y0, &M);
		int x[MAXN], y[MAXN];
		int X, Y;
		x[0] = X = x0;
		y[0] = Y = y0;		
		for (int i=1; i<n; i++) {
			x[i] = X = (A*X+B) %M;
			y[i] = Y = (C*Y+D) %M;			
		}
		unsigned long long cnt = 0;
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				for (int k=j+1; k<n; k++)
					cnt+=((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0);
		printf("Case #%d: %lld\n", T, cnt);
	}
	return 0;
}