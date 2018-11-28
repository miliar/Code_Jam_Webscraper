#include<cstdio>
#include<cstring>
#include<cmath>
bool P[1000001];
int PL[1000001], pcnt;

long long bm(long long a, long long b, long long p){
	if (b == 0) return 1;
	if (b == 1) return a%p;
	long long m = bm(a, b/2, p);
	m = (m * m) % p;
	if (b&1) return (m*a)%p;
	else return m;
}

int main(){
	P[1] = 1;
	for (int i = 2; i <= 1001; ++i)
		if (!P[i])
			for (int j = i*i ; j <= 1000000; j+=i)
				P[j] = 1;
	for (int i  = 2; i <= 1000000; ++i)
		if (!P[i])
			PL[pcnt++] = i;
	int T, ca=0;
	scanf("%d", &T);
	int px, py;
	while (T--){
		printf("Case #%d: ", ++ca);
		int D, K;
		scanf("%d%d", &D, &K);
		int G[K];
		for (int i = 0 ; i < K; ++i) scanf("%d", G+i);
		int Lim = 1;
		for (int i = 0; i < D; ++i) Lim *= 10;
		int ans = -1, diu=0;
		for (int i = 0 ; !diu && i < pcnt && PL[i] < Lim;++i){
			int pp = PL[i];
			if (K < 3) break;
			bool ok = 1;
			for (int j = 0 ; ok &&j < K; ++j) ok = pp > G[j];
			if (!ok) continue;
			long long X = G[1]-G[0], Y = G[2]-G[1];
			//while (X<0) X+=pp; while (Y<0) Y += pp;
			if (X < 0) X += ((-X/pp) + ((-X)%pp > 0)) * pp;
			if (Y < 0) Y += ((-Y/pp) + ((-Y)%pp > 0)) * pp;
			long long xx, yy;
			if (X == 0) continue;
			xx = bm(X, pp-2, pp);
			long long A = (Y * xx) % pp;
			long long B = G[1] - A * G[0];
			//while (B < 0) B += pp;
			if (B < 0) B += ((-B/pp) + ((-B)%pp > 0)) * pp;
			int S = G[0];
			for (int j = 0; ok && j < K; ++j)
				ok = S == G[j], S = ((A*S)+B)%pp;
			if (ok){
				if (ans == -1) ans = S;
				else diu = ans != S;
			}
		}
		bool id = 1 && (K > 1);
		for (int i = 0 ; i < K-1 && id; ++i) id  = G[i] == G[i+1];
		if (id) ans = G[0];
 		if (diu || ans == -1) puts("I don't know.");
		else printf("%d\n", ans);
	}
	return 0;
}
