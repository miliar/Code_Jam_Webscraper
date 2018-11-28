#include<stdio.h>

int nCase;
char S[128], R[32];
char sample[4][2][128] = {{"y qee", "a zoo"},
	{"ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"}, 
	{"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"}, 
	{"de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"}};

int main() {
	for(int i = 0; i < 32; ++i) R[i] = -1;
	for(int i = 0; i < 4; ++i) {
		for(char *p = sample[i][0], *q = sample[i][1]; *p; ++p, ++q) {
			if(*p < 'a' || *p > 'z') continue;
			if(R[*p-'a'] != -1 && R[*p-'a'] != *q-'a')
				fprintf(stderr, "mismatch %c -> %c / %c\n", *p, R[*p-'a']+'a', *q);
			R[*p-'a'] = *q - 'a';
		}
	}
	R['z'-'a'] = 'q' - 'a';
	for(int i = 0; i < 26; ++i) {
		if(R[i] == -1) fprintf(stderr, "R[%c] = %c\n", i+'a', R[i]+'a');
		for(int j = i+1; j < 26; ++j) {
			if(R[i] == R[j]) fprintf(stderr, "R[%c] = R[%c] = %c\n", i+'a', j+'a', R[i]+'a');
		}
	}
	scanf("%d", &nCase);
	fgets(S, 100, stdin);
	for(int cs = 1; cs <= nCase; ++cs) {
		fgets(S, 120, stdin);
		for(char *p = S; *p; ++p) {
			if('a' <= *p && *p <= 'z') *p = R[*p-'a'] + 'a';
			else if('A' <= *p && *p <= 'Z') *p = R[*p-'A'] + 'A';
			else if(*p == '\n' || *p == '\r') *p = '\0';
		}
		printf("Case #%d: %s\n", cs, S);
	}
}

