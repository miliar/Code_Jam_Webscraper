#include <stdio.h>
#include <math.h>
#include<memory.h>
#include<string.h>
int main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T;
	int N; //represent the number of buttonns taht need to be pressed
	char R[1000];
	int P[1000];
	int i, j;

	int Oj, Op;
	int Bj, Bp;

	int y, t;

	fscanf(fp, "%d", &T);
	for(i = 1; i <= T; ++i){

		fscanf(fp, "%d", &N);
		for(j = 0; j < N; ++j)
			fscanf(fp, " %c%d", &R[j], &P[j]);
		R[N] = 'O';
		R[N+1] = 'B';
		P[N] = 1;
		P[N+1] = 1;
		
		y = 0;
		Oj = Bj = 0;
		Op = Bp = 1;
		while(R[Oj] == 'B') ++Oj;
		while(R[Bj] == 'O') ++Bj;

		while(Oj < N || Bj < N) {
			if(Oj < Bj){
				y += t = abs(P[Oj] - Op) + 1;
				if(abs(P[Bj] - Bp) < t){ Bp = P[Bj];
				}else{
					if(P[Bj] < Bp) Bp -= t;
					else Bp += t;
				}

				Op = P[Oj];
				++Oj;
				while(R[Oj] == 'B') ++Oj;

			}else{
				y += t = abs(P[Bj] - Bp) + 1;
				if(abs(P[Oj] - Op) < t){ Op = P[Oj];
				}else{
					if(P[Oj] < Op) Op -= t;
					else Op += t;
				}

				Bp = P[Bj];
				++Bj;
				while(R[Bj] == 'O') ++Bj;
			}

		}

		fprintf(ofp, "Case #%d: %d\n", i, y);

	}

	return 0;
}