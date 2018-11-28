#include <stdio.h>
#include <cstring>
#include <cmath>

char combine[26][26];
bool opposed[26][26];
char list[200];

int main() {
	FILE *fin = fopen("B-large.in","r");
	FILE *fout = fopen("out.txt","w");


	int T;
	fscanf(fin,"%d\n",&T);

	for (int t=1; t<=T; t++) {
		printf("%d\n",t);

		for (int i=0; i<26; i++) {
			for (int j=i; j<26; j++) {
				combine[i][j] = '\0';
				combine[j][i] = '\0';

				opposed[i][j] = false;
				opposed[j][i] = false;
			}

		}

		int C;
		fscanf(fin,"%d",&C);

		for (int i=0; i<C; i++) {
			char s[5];
			fscanf(fin,"%s",s);
			combine[s[0]-'A'][s[1]-'A'] = s[2];
			combine[s[1]-'A'][s[0]-'A'] = s[2];
		}

		int D;
		fscanf(fin,"%d",&D);
		for (int i=0; i<D; i++) {
			char s[5];
			fscanf(fin,"%s",s);
			opposed[s[0]-'A'][s[1]-'A'] = true;
			opposed[s[1]-'A'][s[0]-'A'] = true;
		}


		int N;
		char s[105];
		fscanf(fin,"%d %s",&N,s);

		int li = 0;

		for (int i=0; i<N; i++) {
			if (li == 0) {
				list[li++] = s[i];
			}
			else {
				if (combine[list[li-1]-'A'][s[i]-'A'] != '\0') {
					list[li-1] = combine[list[li-1]-'A'][s[i]-'A'];
				}
				else {
					for (int j=0; j<li; j++) {
						if (opposed[list[j]-'A'][s[i]-'A']) {
							li = 0;
							break;
						}
					}
					if (li != 0) {
						list[li++] = s[i];
					}
				}
			}
		}

		fprintf(fout,"Case #%d: [",t);
		for (int i=0; i<li; i++) {
			fprintf(fout,"%c",list[i]);
			if (i != li-1) {
				fprintf(fout,", ");
			}
		}
		fprintf(fout,"]\n");

	}
}
