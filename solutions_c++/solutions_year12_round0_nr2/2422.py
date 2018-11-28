// dance.cpp
#include <stdio.h>
#include <string.h>

int main(void)
{

	int T = 0; // nr of test cases
	int N = 0; // nr of googlers
	int S = 0; // nr of surpriseing triplets
	int P = 0; // expected best result

	FILE* fin  = fopen("in.txt", "r");
	FILE* fout = fopen("out.txt", "w");

	if ((fin != NULL) && (fout != NULL)) 
	{
		fscanf(fin, "%d", &T);
	
		// for each test case
		for(int i=0; i<T; ++i)
		{
			int count = 0; // counts the number of googlers having maximum score equal to p

			fscanf(fin, "%d%d%d", &N, &S, &P);

			// minimal value allowed to be splitted in non surpriseing scores and to have maximum equal to P
			int x = 3*P-2; 

			// minimal value allowed to be splitted in surpriseing scores and to have maximum value equal to P
			int y = 3*P-4; 
			if(y < 2) y = 2; // if y <= 2 then can't be generated surpriseing triplet

			// for each score
			for(int j=0; j<N; ++j)
			{
				int v = 0; // total score of a googler

				fscanf(fin, "%d", &v);

				// can be splittet to non surpriseing
				// and max score will be greater than P
				if(v >= x)
				{
					++count;
				} 
				else
				{
					// can be splittet to surpriseing and
					// max score will be greater than P
					if((v >= y) && (S-- > 0))
					{
						++count;
					}
					else
					{
						// can't be splitted so that max score will be greater than P
					}
				}
			}

			fprintf(fout,"Case #%d: %d\n", i+1, count);
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
