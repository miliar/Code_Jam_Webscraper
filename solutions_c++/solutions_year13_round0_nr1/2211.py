#include <stdio.h>
#include <vector>
#include <algorithm>

//#define PROBLEM "a"
//#define DEFAULT_INPUT (PROBLEM ".in")
//#define DEFAULT_OUTPUT (PROBLEM ".out")

//#define debugf fprintf
#define debugf __noop

FILE *Fin, *Fout;

void Test(int testNo)
{
    static const char* OutComes[] = { "Game has not completed", "O won", "X won", "Draw" };
    static char S[16];
    static char Z[4][4];

    int dots = 0, won = 0;

    // read
    for( int i=0; i<4; i++ )
    {
        fgets( S, sizeof(S), Fin );

        for( int j=0; j<4; j++ )
        {
            int v = 0;
            switch(S[j])
            {
            case 'O': v = 1; break;
            case 'X': v = 2; break;
            case 'T': v = 3; break;
            case '.': dots++; break;
            }
            Z[i][j] = v;
        }

        int row = *(int*)&Z[i];
        if( (row & 0x01010101) == 0x01010101 ) won |= 1;
        if( (row & 0x02020202) == 0x02020202 ) won |= 2;
        debugf( stderr, "test: %d, i: %d, won: %x\n", testNo, i, won );
    }

    int d1 = Z[0][0] & Z[1][1] & Z[2][2] & Z[3][3];
    int d2 = Z[0][3] & Z[1][2] & Z[2][1] & Z[3][0];

    won |= d1;
    won |= d2;

    debugf( stderr, "test: %d, d1: %08x\n", testNo, d1 );
    debugf( stderr, "test: %d, d2: %08x\n", testNo, d2 );
    debugf( stderr, "test: %d, diag, won: %x\n", testNo, won );

    // check columns
    for( int i=0; i<4; i++ )
    {
        int c = 3;
        for( int j=0; j<4; j++ )
            c &= Z[j][i];
        won |= c;

        debugf( stderr, "test: %d, c: %d, won: %x\n", testNo, i, won );
    }

    if( !won && !dots )
        won = 3;
        
    debugf( stderr, "test: %d, won: %x\n", testNo, won );

    // output
    fprintf( Fout, "Case #%d: %s\n", testNo+1, OutComes[won] );

    fgets( S, sizeof(S), Fin );
}

void Run()
{
    int T = 0;

    fscanf( Fin, "%d\n", &T );
    for( int t=0; t<T; t++ )
    {
        Test(t);
    }
}

int main(int argc, char* argv[])
{
    /*Fin  = fopen(argc >= 2 ? argv[1] : DEFAULT_INPUT , "rt" ); if( Fin  == NULL )*/ Fin  = stdin;
    /*Fout = fopen(argc >= 3 ? argv[2] : DEFAULT_OUTPUT, "w+t"); if( Fout == NULL )*/ Fout = stdout;

    Run();

    fflush(Fout);
    fclose(Fout);
    fclose(Fin);
    return 0;
}