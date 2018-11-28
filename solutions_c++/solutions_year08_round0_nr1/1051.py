#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char**argv)
{
	int Cn;

	fscanf(stdin, "%d\n", &Cn);
	for (int Ci=0; Ci < Cn; Ci++) {
		int Sn;
		char S[128][128];
		fscanf(stdin, "%d\n", &Sn);
		for (int Si=0; Si<Sn; Si++) {
			//fscanf(stdin, "%s\n", S[Si]);
			fgets(S[Si], 128, stdin);
		}
		int Qn;
//		char Q[1024][128];
		int  q[1024];
		fscanf(stdin, "%d\n", &Qn);
		for (int Qi=0; Qi<Qn; Qi++) {
			char Q[128];
			//fscanf(stdin, "%s\n", Q);
			fgets(Q, 128, stdin);
			for (int i = 0; i < Sn; i++) {
				if (!strcmp(S[i], Q)) {
					q[Qi] = i;
					break;
				}
			}
		}

		// solve
		int n = 0;
		int s[128] = {}; // flag
		int sn = 0;
		for (int i = 0; i < Qn; i++) {
			if (s[q[i]] == 0) {
				sn++;
				s[q[i]] = 1;
			}
			if (sn >= Sn) {
				bzero(s, sizeof(s));
				n++;
				s[q[i]] = 1;
				sn = 1;
			}
		}


		printf("Case #%d: %d\n", Ci+1, n);
	}

	return 0;
}
