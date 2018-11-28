#include <cstdio>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>

using namespace std;

char c[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u',  'o',  'm',  'x',  's',  'e',  'v',  'z',  'p',  'd',  'r',  'j',  'g',  't',  'h',  'a',  'q'};

int f(char ch) {
	for (int i = 0; i < 26; i++){
		if (c[i] == ch) return i;
	}
	return ' ' - 'a';
}

int main(){
	FILE *fin = fopen("A.in", "r");
	FILE *fout = fopen("A.out", "w");

	int t;
	fscanf(fin, "%d", &t);
	char ch[111];
	fgets(ch, 111, fin);
	for (int test = 1; test <= t; test++) {
		fgets(ch, 111, fin);
		fprintf(fout, "Case #%d: ", test);

		int n = strlen(ch);
		for (int i = 0; i < n; i++) {
			fprintf(fout, "%c", f(ch[i]) + 'a');
		}

		fprintf(fout, "\n");		
	}

}