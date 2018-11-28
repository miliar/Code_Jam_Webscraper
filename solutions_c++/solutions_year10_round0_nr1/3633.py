#include <stdio.h>
//#include <stdlib.h>
#include <math.h>

#define SMALL
//#define LARGE

#ifdef SMALL
    #define N 10
    #define K 100
#else
    #define N 30
    #define K 100000000
#endif

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

int main()
{
    FILE *fp = fopen(INPUT_FILE, "r");
    FILE *out = fopen(OUTPUT_FILE, "w");

    int tc, n, k;
    int result;

    fscanf(fp, "%d", &tc);

    for( int i=0; i<tc; i++ )
    {
        fscanf(fp, "%d %d", &n, &k);
        result = (k+1)%(int)pow(2, n);
        if( !result )
            fprintf(out, "Case #%d: ON\n",(i+1));
        else
            fprintf(out, "Case #%d: OFF\n",(i+1));
    }

    fclose(fp);
    fclose(out);
    return 0;
}
