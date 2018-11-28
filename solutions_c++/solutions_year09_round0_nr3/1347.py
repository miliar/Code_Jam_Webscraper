#include <cstdio>
#include <cstring>

char S[20] = "welcome to code jam";
char t[516];

int memo[516][20];

int rek(int n, int k){
	int &sol = memo[n][k];

	if (sol != -1) return sol;
	if (S[k] == '\0') return sol = 1;
	if (t[n] == '\0') return sol = 0;

	sol = rek(n+1, k);
	if (t[n] == S[k]) sol = (sol+rek(n+1, k+1))%10000;

	return sol;
}

int main(){
	int N;
	scanf("%d", &N);

	for (int tt = 1; tt <= N; ++tt){
		do{
			fgets(t, 516, stdin);
		}while(t[0] == '\0' || t[0] == 10);
		memset(memo, -1, sizeof memo);

		printf("Case #%d: %04d\n", tt, rek(0, 0));
	}

	return 0;
}
