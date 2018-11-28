#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int D, K;
long long int P[15];
long long int primos[1000000];
char crivo[1000010];
int nprimos;
void faz_crivo() {
	MSET(crivo, 1);
	nprimos = 0;
	crivo[0] = crivo[1] = 0;
	foreach(i, 2, 1000) if (crivo[i]) {
		for (int j = i*i; j < 1000000; j += i) crivo[j] = 0;
	}
	rep(i, 1000000) if (crivo[i]) primos[nprimos++] = i;
}

long long int eleva(long long int a, int b, long long int primo) {
	if (b == 0) return 1;
	if (b % 2 == 1) return (a*eleva((a*a)%primo, b/2, primo))%primo;
	return eleva((a*a)%primo, b/2, primo);
}

long long int mod(long long int a, long long int b) {
	return ((a%b)+b)%b;
}

int tenta(long long int primo) {
	// Testa se A == 1
	long long int B = mod(P[1] - P[0], primo);
	bool pode = true;
	rep(i, K-1) {
		if (mod(P[i+1]-P[i], primo) != B) pode = false;
	}

	long long int A = mod((P[2]-P[1])*eleva(P[1]-P[0], primo-2, primo), primo);
	if (A == 1) return pode?mod(P[K-1]+B, primo):-1;
	long long int Am1inv = eleva(A-1, primo-2, primo);
	long long int x = mod((A-1)*P[0], primo);
	long long int y = mod(mod((A-1)*P[1] - (A-1)*P[0], primo)*Am1inv, primo);
	B = mod(y - x, primo);
	long long int atual = P[0];
	bool pode2 = true;
	rep(i, K) {
		if (P[i] != atual) pode2 = false;
		atual = mod(A*atual + B, primo);
	}
	B = mod(P[1] - P[0], primo);
	if (pode && pode2) return -2;
	if (pode) return mod(P[K-1]+B, primo);
	if (pode2) return atual;
	return -1;
}

int main() {
	TRACE(setbuf(stdout, NULL));
	int _42;
	scanf("%d", &_42);
	faz_crivo();
	rep(_41, _42) {
		printf("Case #%d:", _41+1);
		scanf("%d %d", &D, &K);
		long long int maior = 0;
		rep(i, K) {
			scanf("%lld", &P[i]);
			maior = max(maior, P[i]);
		}
		if (K == 1) {
			printf(" I don't know.\n");
			continue;
		}
		int lim = 1;
		rep(j, D) lim *= 10;
		if (K == 2) {
			if (P[0] == P[1]) printf(" %lld\n", P[0]);
			else printf(" I don't know.\n");
			continue;
		}
		if (P[K-1] == P[K-2]) {
			printf(" %lld\n", P[K-1]);
			continue;
		}
		int ans = -1;
		rep(i, nprimos) {
			if (primos[i] <= maior) continue;
			if (primos[i] > lim) break;
			int temp = tenta(primos[i]);
			if (temp == -1) continue;
			if (temp == -2) {
				ans = -1;
				break;
			}
			if (ans != -1 && ans != temp) {
				ans = -1;
				break;
			}
			ans = temp;
		}
		if (ans == -1) printf(" I don't know.\n");
		else printf(" %d\n", ans);
	}
	return 0;
}
