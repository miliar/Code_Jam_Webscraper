#include <cstdio>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

using namespace std;

int T, C, D, N;
char mix[40][4], clr[40][4], seq[150], res[150];

void solve(int n) {
	int k = 1;
	res[0] = seq[0];
	FOR(i,1,N) {
		res[k++] = seq[i];
		FOR(j,0,C)
			if ((mix[j][0] == res[k-1] && mix[j][1] == res[k-2]) ||
				(mix[j][0] == res[k-2] && mix[j][1] == res[k-1]))
				res[k-2] = mix[j][2], k--;
		FOR(j,0,D)
			FOR(f,0,k)
				if ((clr[j][0] == res[f] && clr[j][1] == res[k-1]) ||
					(clr[j][0] == res[k-1] && clr[j][1] == res[f]))
					k = 0;
	}
	res[k] = '\0';
	printf("Case #%d: [", n);
	if (k > 0)
		putchar(res[0]);
	FOR(i,1,k)
		printf(", %c", res[i]);
	puts("]");
}

int main() {
	scanf("%d\n", &T);
	FOR(i,0,T) {
		scanf("%d ", &C);
		FOR(j,0,C)
			scanf("%s", mix[j]);
		scanf("%d ", &D);
		FOR(j,0,D)
			scanf("%s", clr[j]);
		scanf("%d ", &N);
		scanf("%s", seq);
		solve(i+1);
	}
}