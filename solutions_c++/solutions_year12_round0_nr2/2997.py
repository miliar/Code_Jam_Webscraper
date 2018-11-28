#include <stdio.h>

void main()
{
	FILE *in, *out;
	int T, N, S, P;
	int scores, max, mod, cnt, f;
	int i, j;

	in = fopen("B-large.in","r");
	out = fopen("B-large.out","w");

	fscanf(in,"%d",&T);

	for(i=0; i<T; i++) {
		
		cnt=0;
		
		fscanf(in,"%d %d %d", &N, &S, &P);
		
		for(j=0;j<N;j++) {

			fscanf(in,"%d",&scores);
			
			f = (scores >= 2);
			max = scores/3;
			mod = scores%3;
			
			if( mod )
				max++;			

			if( max >= P )
				cnt++;
			else if( S && f && mod != 1 && max+1 >= P ) {
				S--;
				cnt++;
			}

		}
		fprintf(out,"Case #%d: %d\n",i+1,cnt);
	}

}
