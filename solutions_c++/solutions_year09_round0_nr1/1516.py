// alienlang.cpp --  Thu Sep 03 2009
// http://code.google.com/codejam/contest/dashboard?c=90101#s=p1
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAX_L 15
#define MAX_D 5000
#define MAX_N 500
#define MAX_C 26
#define CHAR2BIT(ch) (1 << ((ch)-'a'))
int words[MAX_D][MAX_L];
char patn[(MAX_C + 2) * (MAX_L + 1) + 1];
char w[MAX_L+1];
int patn_bmp[MAX_L];

void set_word_bmp(const char *w, int *bmp) {
	for(int i = 0; w[i]; ++i) bmp[i] = CHAR2BIT(w[i]);
}

void set_pattern_bmp(const char *w, int *bmp) {
	for(int i = 0, j = 0; w[i]; ++i, ++j) {
		if(w[i] == '(') {
			bmp[j] = 0;
			do bmp[j] |= CHAR2BIT(w[i]); while(w[++i] != ')');
		} else {
			bmp[j] = CHAR2BIT(w[i]);
		}
	}
}

bool match_pattern(const int *wd, int L, const int *patn) {
	for(int i = L-1; i >= 0; --i) {
		if((wd[i] & patn[i]) == 0) return false;
	}
	return true;
}

int main(int argc, char *argv[]) {
	int L, D, N;
	scanf(" %d %d %d", &L, &D, &N);
	assert(L <= MAX_L);
	assert(D <= MAX_D);
	assert(D <= MAX_D);

	// Read in Words
	for(int j = 0; j < D; ++j) {
		scanf(" %s", w);
		assert((int)strlen(w) == L);
		set_word_bmp(w, words[j]);
	}

	for(int k = 0; k < N; ++k) {
		int c = 0;
		scanf(" %s", patn);
		set_pattern_bmp(patn, patn_bmp);
		for(int q = 0; q < D; ++q) {
			if(match_pattern(words[q], L, patn_bmp)) ++c;
		}
		printf("Case #%d: %d\n", k+1, c);
	}

	return 0;
}

