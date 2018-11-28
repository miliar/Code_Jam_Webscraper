#include <cstdio>
#include <cstdlib>

typedef unsigned long long int      ull;

static int
cmp (const void * a, const void * b )
{
    const int * pa = (const int *)a;
    const int * pb = (const int *)b;

    if ( *pa > *pb)
        return -1;
    else
    {
        if ( *pa < *pb )
            return 1;
    }
    return 0;
}


int freq[1000];

int main ( int argc, char * argv[] )
{
    if ( argc < 3 )
    {
        printf ( "wrong usage\n" );
        return -1;
    }

    FILE * fi = fopen ( argv[1], "r" );
    FILE * fo = fopen ( argv[2], "w" );

    int N = 0;
    fscanf ( fi, "%d", &N );

    for ( int test = 1; test <= N; test++ )
    {
        int P, K, L;
        fscanf ( fi, "%d %d %d", &P, &K, &L );
        for ( int i = 0; i < L; i++ )
            fscanf ( fi, "%d", freq + i );

        qsort ( freq, L, sizeof(int), cmp );

 //       for ( int i = 0; i < L; i++ )
 //       {
//          printf ( "%d ", freq[i] );
//        }
//        printf ( "\n" );

        ull answer = 0;

        unsigned int add = 0; int free_keys = 0;
        int lpk = 0;
        for ( int i = 0; i < L; i++ )
        {
            if ( free_keys == 0 )
            {
                free_keys=K;
                add++;
                lpk++;

                if ( lpk > P )
                    break;
            }

            answer += add * freq[i];
//            printf ( "+ %d x %d\n", add, freq[i] );
            free_keys--;
        }

        if ( lpk <= P )
        {
            unsigned long res = answer;
            fprintf ( fo, "Case #%d: %d\n", test, res );
        }
        else
        {
            fprintf ( fo, "Case #%d: impossible\n", test );
        }
    }

    fclose(fi);
    fclose(fo);
}
