#include <cstdio>

#define FOR(i,a,b) for (int i=(a); i<(b); i++)
using namespace std;

int scores[110];

int solve(int n, int s, int p) {
	int t = 0, v, mod;
	FOR(i,0,n) {
		mod = scores[i]%3;
		v = scores[i]/3 + (mod?1:0);
		if (v >= p) t++;
		else if (mod != 1 && s && scores[i]>1 && v+1 >= p)
			t++, s--;
	}
	return t;
}

int main() {
	int t, n, s, p;
	scanf("%d", &t);
	FOR(i,0,t) {
		scanf("%d %d %d", &n, &s, &p);
		FOR(j,0,n) scanf("%d", &scores[j]);
		printf("Case #%d: %d\n", i+1, solve(n,s,p));
	}
	return 0;
}