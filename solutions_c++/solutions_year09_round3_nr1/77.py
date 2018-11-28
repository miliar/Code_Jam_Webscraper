#include <stdio.h>
#include <string.h>
#include <strings.h>
typedef long long ll;

int N; char S[100]; int M[256];

ll solve() {
	scanf("%s", S);
	if (!S[1]) return 1;
	memset(M, -1, sizeof(M));
	int mini = 1;
	M[S[0]] = 1;
	for (int i = 1; S[i]; i++) if (M[S[i]] == -1)
	 M[S[i]] = (mini == 1 ? 0 : mini), mini++;
	if (mini == 1) mini = 2;
	ll sum = 0;
	for (int i = 0; S[i]; i++) sum = sum * mini + M[S[i]];
	return sum;
}

int main() {
	scanf("%d", &N);
	for (int case_x = 1; case_x <= N; case_x++)
	 printf("Case #%d: %lld\n", case_x, solve());
	return 0;
}
