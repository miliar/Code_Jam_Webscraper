// recycled.cpp
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
	int T=0;

	FILE* fin  = fopen("in.txt", "r");
	FILE* fout = fopen("out.txt", "w");

	if ((fin != NULL) && (fout != NULL)) 
	{
		// read nr of test cases
		fscanf(fin, "%d", &T);
		
		for(int i=0; i<T; ++i)
		{
			long counter=0;
			int D=0;
			long S=0;
			long A=0; 
			long B=0;
				
			// read minimal and maximal boundaries
			fscanf(fin, "%ld%ld", &A, &B);
			
			// calculatig nr of digits
			for(long d=A; d>0; d/=10) ++D;

			S = powl(10L, (long)(D-1)); // shifting value

			// for each number between A and B
			for(long n=A; n<B; ++n)
			{
				long m=n; 				// rotated pair of n
				int  c=0;					// history counter
				long h[10];				// history of the rotated pairs
				
				// permutation
				for(int j=0; j<D-1; ++j)
				{
					int r = m%10;
					m /= 10L;
					m += r * S;

					if(m <= n) continue;
					if(m > B) continue;
				
					// search in history
					bool found=false;
					for(int k=0; k<c; ++k)
					{
						if(h[k]==m) found=true;
					}
					
					if(found) continue;

					// update history
					h[c++]=m;
	
					// found a valid pair
					++counter; // counts the valid pairs
				}
			}

			fprintf(fout,"Case #%d: %ld\n", i+1, counter);
		}
	}
	else
	{
		printf("error: open file out.txt or in.txt\n");
	}
	
	fclose(fin);
	fclose(fout);
	return 0; 
}
