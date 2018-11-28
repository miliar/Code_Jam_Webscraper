#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

char S[1010];
char result[1010];
int k, N;
int pos[17], used[17];
int best;

void apply() {
	int i, away, mod;
	for(i = 0; i < N; i++) {
		away = ((int)(i / k)) * k;
		result[i] = S[pos[i %k]-1+away];
	}
	char prev_letter = 0;
	int changes = 0;
	for(i = 0; i < N; i++) {
		if(result[i] != prev_letter) {
			changes ++;
			prev_letter = result[i];
		}
	}
	//result[N] = '\0';
	//printf("result: %s\n", result);
	if(changes < best) {
		best = changes;
	}
}

void generate_pos(int p) {
	if(p == k) {
		/*printf("solutie: ");
		for(int i=0; i<k; i++) {
			printf("%d ", pos[i]);
		}
		printf("\n");*/
		apply();
	}
	for(int i=1; i<=k; i++) {
		if(!used[i]) {
			pos[p] = i;
			used[i] = 1;
			generate_pos(p+1);
			used[i] = 0;
		}
	}
}

void solve(int case_number) {
	best = N  + 1;
	generate_pos(0);
	printf("Case #%d: %d\n", case_number, best);
	fprintf(stderr, "Case #%d: %d\n", case_number, best);
}

int main(void) {
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D.out", "wt", stdout);

	int i, T;
	scanf("%d",&T);
	for(i=1; i<=T; i++) {
		scanf("%d\n",&k);
		fgets(S, 1010, stdin);
		if(S[strlen(S)-1] == '\n') {
			S[strlen(S)-1] = '\0';
		}
		N = strlen(S);
		//printf("N: %d\n", N);
		solve(i);
	}

	return 0;
}