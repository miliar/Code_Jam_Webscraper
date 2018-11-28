#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//#define SMALL
#define LARGE

#define T 15
#define SIZE 10000

#ifdef SMALL
    #define N 2
#else
    #define N 1000
#endif

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"
#define RED 1
#define BLUE 2

int main()
{
    FILE *fp = fopen(INPUT_FILE, "r");
    FILE *out = fopen(OUTPUT_FILE, "w");
    int arr1[N], arr2[N];

    int tc, n, count=0, d1, d2;

    fscanf(fp, "%d", &tc);

    for( int i=0; i<tc; i++ )
    {
        count = 0;
        fscanf(fp, "%d", &n);

        for( int j=0; j<n; j++ )
        {
            fscanf(fp, "%d %d", &arr1[j], &arr2[j]);
        }

        for( int x=0; x<n-1; x++ )
        {
            for( int y=x+1; y<n; y++ )
            {

                d1 = arr1[x]-arr1[y];
                d2 = arr2[x]-arr2[y];
                if( (d1*d2)<0 )
                    count++;
            }
        }
        
        fprintf(out, "Case #%d: %d\n",(i+1),count);
    }

    fclose(fp);
    fclose(out);
    return 0;
}
