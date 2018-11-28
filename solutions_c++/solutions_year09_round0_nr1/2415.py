#include <stdio.h>
#include <string.h>
#include <math.h>

int l, d, n;
char dizionario[5000][15];
char pattern[420];
int token[26];

void tokenizer() {
	for(int i=0; i<26; i++) {
		token[i] = 0;
	}

	bool aperta = false;

	for(int j=0, k=0;pattern[j]!='\0'; j++) {
		if(pattern[j]=='(') {
			aperta = true;
			continue;
		}

		if(pattern[j]==')') {
			aperta = false;
			k++;
			continue;
		}

		token[k] = token[k] | ((int) pow(2,(pattern[j]-'a')));

		if(!aperta)
			k++;
	}
}

int main() {
	int matchWords;
	bool match;

	FILE *fin=fopen("A-large.in","r");
	FILE *fout=fopen("alienLanguage.out","w");

	fscanf(fin, "%d %d %d", &l, &d, &n);

	for(int j=0; j<d; j++) {
		fscanf(fin, "%s", &dizionario[j]);
	}

	for(int k=0; k<n; k++) {
		fscanf(fin, "%s", &pattern);
		matchWords = 0;

		tokenizer();

		for(int i=0; i<d; i++) {
			match = true;
			for(int m=0; m<l&&match; m++) {
				if((((int) pow(2,dizionario[i][m]-'a')) & token[m]) == 0)
					match = false;
			}
			if(match)
				matchWords++;
		}

		fprintf(fout, "Case #%d: %d\n", k+1, matchWords);
	}

	return 0;
}
