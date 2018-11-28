#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void main(void){
	FILE* fin = fopen("triangle.in","rt");
	FILE* fout = fopen("triangle.out","wt");

	int N;
	bool primes[20000];
	int p[20000];
	int pc;
	p[0] = 2; pc = 1;
	memset(primes,0,sizeof(primes));
	primes[2] = true;
	for(int i=3;i<20000;i++)
	{
		primes[i] = true;
		for(int j=2;j*j<=i;j++) if (i%j == 0) primes[i] = false;
		if (primes[i])
			p[pc++] = i;
	}

	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		int N,M,T,x,y, A, B;
		bool found = false;

		fscanf(fin, "%d %d %d\n", &N, &M, &T);
		
		for(A=1; A<=N; A++) {
			for(B=M; B>=1; B--)
				if (A*B>=T) {
					int Z = A*B-T;
					for(x=0;x<=A;x++) 
						for(y=0;y<=B;y++)
							if (x*y==Z)
							{
								found = true;
								goto l;
							}
				}else
					break;
		}
l:
		if (found) 
			fprintf(fout,"Case #%d: %d %d %d %d %d %d\n",i+1, 0,0, A, y, x, B);
		else 
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",i+1);
	}

	fclose(fin);
	fclose(fout);
}