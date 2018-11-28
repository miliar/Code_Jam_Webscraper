#include <stdio.h>
#define MN 111

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

int T,N,M,NC;
int O[MN][MN],D[MN][MN],C[MN][MN];
int DX[4] = {-1,0,0,1};
int DY[4] = {0,-1,1,0};
int X[MN*MN],Y[MN*MN];
int HEAD,TAIL,G,CASE;

int main()
{
	int i,j,k,d,m,x,y;

	fscanf (fin,"%d",&T);

	while (T--){ CASE++;
		fscanf (fin,"%d %d",&N,&M);

		for (i=0;i<N;i++){
			for (j=0;j<M;j++) fscanf (fin,"%d",&O[i][j]);
		}

		for (i=0;i<N;i++){
			for (j=0;j<M;j++){
				d = 5; m = O[i][j]; C[i][j] = -1;
				for (k=0;k<4;k++){
					x = i + DX[k]; y = j + DY[k];
					if (x < 0 || x >= N || y < 0 || y >= M) continue;

					if (m > O[x][y]){
						m = O[x][y]; d = k;
					}
				}

				D[i][j] = d;
			}
		}

		NC = 0;
		fprintf (fout,"Case #%d:\n",CASE);
		for (i=0;i<N;i++){
			for (j=0;j<M;j++){
				if (C[i][j] == -1){
					HEAD = TAIL = -1;
					++HEAD; X[HEAD] = i; Y[HEAD] = j; G = NC;
					while (HEAD > TAIL){
						++TAIL; x = X[TAIL]; y = Y[TAIL];
						
						if (D[x][y] == 5 || C[x+DX[D[x][y]]][y+DY[D[x][y]]] == -1){
							++HEAD; X[HEAD] = x + DX[D[x][y]]; Y[HEAD] = y + DY[D[x][y]];
							if (D[x][y] == 5) break;
						}
						else{
							G = C[x+DX[D[x][y]]][y+DY[D[x][y]]]; break;
						}
					}

					for (k=0;k<=HEAD;k++) C[X[k]][Y[k]] = G;

					if (G == NC) NC++;
				}

				fprintf (fout,"%c ",C[i][j] + 'a');
			}
			fprintf (fout,"\n");
		}
	}

	return 0;
}