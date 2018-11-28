#include <stdio.h>
#include <cstring>
#include <cmath>

int buttons[105];
char buttonsC[105];

int O[105];
int B[105];

int main() {
	FILE *fin = fopen("A-large.in","r");
	FILE *fout = fopen("out.txt","w");


	int T;
	fscanf(fin,"%d\n",&T);

	for (int t=1; t<=T; t++) {
		int N;
		fscanf(fin,"%d",&N);

		int On = 0;
		int Bn = 0;

		for (int i=0; i<N; i++) {
			char s[2];
			int d;
			fscanf(fin,"%s %d",s,&d);
			if (s[0] == 'O') {
				O[On++] = d;
			}
			else {
				B[Bn++] = d;
			}
			buttons[i] = d;
			buttonsC[i] = s[0];
		}

		int Oi = 0;
		int Bi = 0;
		int Op = 1;
		int Bp = 1;

		int total = 0;
		for (int i=0; i<N; i++) {
			if (buttonsC[i] == 'O') {
				int t = fabs(buttons[i]-Op) + 1;
				Op = buttons[i];
				Oi++;
				total += t;

				int d = (B[Bi] >= Bp) ? 1 : -1;
				if ((int)fabs(B[Bi]-Bp) <= t) {
					Bp = B[Bi];
				}
				else {
					Bp += d*t;
				}
			}
			else if (buttonsC[i] == 'B') {
				int t = fabs(buttons[i]-Bp) + 1;
				Bp = buttons[i];
				Bi++;
				total += t;


				int d = (O[Oi] >= Op) ? 1 : -1;
				if ((int)fabs(O[Oi]-Op) <= t) {
					Op = O[Oi];
				}
				else {
					Op += d*t;
				}
			}
		}

		fprintf(fout,"Case #%d: %d\n",t,total);
	}
}
