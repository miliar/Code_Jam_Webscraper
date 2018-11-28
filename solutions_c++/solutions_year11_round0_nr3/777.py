#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main () {
    FILE *fin  = fopen ("CandySplitting.in", "r");
    FILE *fout = fopen ("CandySplittingL.out", "w");
    
	int T;
    fscanf(fin, "%d", &T);
    for(int caseN = 1; caseN<=T; caseN++)
    {
		int tot = 0;
		int min = 99999999;
		int sum = 0;
		int N;
		fscanf(fin, "%d", &N);
		for(int i=0; i<N; i++)
		{
			int num;
			fscanf(fin, "%d", &num);
			tot^=num;
			sum+=num;
			if(min>num)
				min=num;
		}
		if(tot==0)
			fprintf(fout, "Case #%d: %d\n", caseN, sum-min);
		else
			fprintf(fout, "Case #%d: NO\n", caseN);
	}
	
    return 0;
}
