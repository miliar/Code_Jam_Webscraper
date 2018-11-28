#include <stdio.h>
#include <algorithm>

int main() {
	int tn, t; // testcas
	int nn; // Number
	int kn; // K
	int i, j, k, ch;
	bool r, b;
	char m[50][50]; // map
	char tr[50][50]; // transform
	FILE *input, *output;
	input = fopen("lainput.in","r");
	output = fopen("output.txt","w");

	fscanf(input, "%d", &tn);
	for (t=0;t<tn;t++) {	
		r = false;
		b = false;
		fscanf(input, "%d %d", &nn, &kn);

		for (i=nn-1;i>=0;i--) {
			fscanf(input, "%c");
			for (j=0;j<nn;j++) {
				fscanf(input, "%c", &m[i][j]);
				tr[nn-1-j][i]=m[i][j];
			}
		}

		do {
		for (i=1;i<nn;i++) {
			for (j=0;j<nn;j++) {
				if (tr[i-1][j]=='.' && tr[i][j]!='.') {
					tr[i-1][j]=tr[i][j];
					tr[i][j]='.';
				}
			}
		}
		ch = 1;
		for (i=1;i<nn;i++) {
			for (j=0;j<nn;j++) {
				if (tr[i-1][j]=='.' && tr[i][j]!='.') ch = 0;
			}
		}
		} while (ch==0);

		for (i=0;i<nn;i++) {
			for (j=0;j<nn;j++) {
				if (tr[i][j]!='.') {
					if (j<=nn-kn) {
						ch = 0;
						for (k=0;k<kn;k++) {
							if (tr[i][j]!=tr[i][j+k]) ch = 1;
						}
						if (ch==0) {
							if (tr[i][j]=='R') r = true;
							if (tr[i][j]=='B') b = true;
						}
					}
					if (i<=nn-kn) {
						ch = 0;
						for (k=0;k<kn;k++) {
							if (tr[i][j]!=tr[i+k][j]) ch = 1;
						}
						if (ch==0) {
							if (tr[i][j]=='R') r = true;
							if (tr[i][j]=='B') b = true;
						}
					}
					if (i <= nn-kn && j <= nn-kn) {
						ch = 0;
						for (k=0;k<kn;k++) {
							if (tr[i][j] != tr[i+k][j+k]) ch = 1;
						}
						if (ch==0) {
							if (tr[i][j]=='R') r = true;
							if (tr[i][j]=='B') b = true;
						}
					}
					if (i <= nn-kn && j >= kn-1) {
						ch = 0;
						for (k=0;k<kn;k++) {
							if (tr[i][j] != tr[i+k][j-k]) ch = 1;
						}
						if (ch==0) {
							if (tr[i][j]=='R') r = true;
							if (tr[i][j]=='B') b = true;
						}
					}
				}
			}
		}

		if (r&&b) fprintf(output, "Case #%d: Both\n", t+1);
		else if (r) fprintf(output, "Case #%d: Red\n", t+1);
		else if (b) fprintf(output, "Case #%d: Blue\n", t+1);
		else fprintf(output, "Case #%d: Neither\n", t+1);

	}
	return 0;
}