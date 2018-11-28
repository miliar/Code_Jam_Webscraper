#include "stdio.h"
#include "string.h"
#include "math.h"

int main ( int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	fout = fopen ( argv[2], "w" );
	int T, N;
	int i, j, k, l, t, res;
	char a[40][40];
	int b[40];
	fscanf(fin, "%d\n", &T);
	for (i=0; i<T; i++) {
		res = 0;
		fscanf(fin, "%d\n", &N);
		for (j=0; j<N; j++) {
			b[j] = 0;
			for (k=0; k<N; k++) {
				fscanf(fin, "%c", &(a[j][k]));
				if (a[j][k] == '1') b[j] = k+1;
			}
			fscanf(fin, "\n");
		}
		for (j=0; j<N; j++) {
			if(b[j] > j+1) {
				for (k=j+1; k<N; k++) {
					if (b[k] <= j+1) break;
				}
				t = b[k];
				l = k;
				for(k=l-1; k>=j; k--) {
					b[k+1] = b[k];
					res++;
				}
				b[j] = t;
			}
		}
		fprintf(fout,"Case #%d: %d\n", i+1, res);
	}

	fclose ( fin );
	if ( ! fout ) return 0;
	fclose (fout);
	return 1;
}