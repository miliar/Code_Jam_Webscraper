#include <stdio.h>
#define M 50

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

int T,N,D[M],X,I,C,S;

int main()
{
	int i,j,t;

	fscanf (fin,"%d",&T);
	
	while (T--){
		fscanf (fin,"%d",&N); C = 0;
		for (i=0;i<N;i++){
			D[i] = -1;
			for (j=0;j<N;j++){
				fscanf (fin,"%1d",&t);
				if (t) D[i] = j;
			}
		}

		for (i=0;i<N;i++){
			if (D[i] > i){
				for (j=i+1;j<N;j++){
					if (D[j] <= i){I = j; break;}
				}
				for (j=I-1;j>=i;j--){
					t = D[j]; D[j] = D[j+1]; D[j+1] = t; C++;
				}
			}
		}

		fprintf (fout,"Case #%d: %d\n",++S,C);
	}

	return 0;
}