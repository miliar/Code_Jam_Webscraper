
#include <stdio.h>
#include <malloc.h>

using namespace std;

int computePower (unsigned long N, unsigned long K);

int main(int argc, char *argv[])
{
    int noOfTests;
    unsigned long N, K;
    char *inputFile = "A-small-attempt0.in";
    char *outFile = "A-small-attempt0.out";
    FILE* inFileHandle = fopen(inputFile, "r");
    FILE* outFileHandle = fopen(outFile, "w");
    
    fscanf(inFileHandle,"%d",&noOfTests);
    
    for (int i=1; i <= noOfTests; i++) {
        fscanf(inFileHandle,"%lu %lu",&N,&K);
        
        fprintf (outFileHandle,"Case #%d: %s\n",i,(computePower(N,K)?"ON":"OFF"));
    }
    
    fclose(inFileHandle);
    fclose(outFileHandle);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}


typedef unsigned long ul;
int computePower (unsigned long N, unsigned long K)
{
    ul i,j;
    
    int *istate = (int *)malloc(N * sizeof(int));
    int *inp = (int *)malloc(N * sizeof(int));
    int *outp = (int *)malloc(N * sizeof(int));

    for(i=0; i<N; i++) {
        istate[i]= 0;
        inp[i] = 0;
        outp[i] = 0;
    }
    inp[0]=1;

    
    
    for (i=0; i<K ; i++) {
        for(j=0; j<N; j++) {
            if (inp[j] == 1) istate[j] = (istate[j]==0)?1:0;
            inp[j] = (j==0)?1:outp[j-1];
            outp[j] = istate[j]?inp[j]:0;
        }

    }
    
    
    
    int result = outp[N-1];
    
    free(istate);
    free(inp);
    free(outp);
    
    return result;
}
