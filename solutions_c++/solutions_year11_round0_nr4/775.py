/*
ID: jc1
LANG: C++
TASK: 
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main () {
    FILE *fin  = fopen ("GoroSort.in", "r");
    FILE *fout = fopen ("GoroSortL.out", "w");
    
    int T;
    fscanf(fin, "%d", &T);
    for(int caseN=1; caseN<=T; caseN++)
    {
		int N;
		fscanf(fin, "%d", &N);
		double incorrect = 0;
		for(int i=1; i<=N; i++)
		{
			int n;
			fscanf(fin, "%d", &n);
			if(n!=i)
				incorrect++;
		}
		fprintf(fout, "Case #%d: %.6f\n", caseN, incorrect);
	}
	
    
    
    return 0;
}
