
#include <cstdlib>
#include <cstdio>

#include <string.h>

static const int maxLen = 1024;

static const char *X_WINS = "X won";
static const char *O_WINS = "O won";
static const char *DRAW = "Draw";
static const char *INCOMPLETE = "Game has not completed";

typedef struct
{
    int row;
    int col;
} pos_t;

unsigned int winning_pos[10]
    = {
       0xf000,     // 1111 0000 0000 0000
       0x0f00,     // 0000 1111 0000 0000
       0x00f0,     // 0000 0000 1111 0000
       0x000f,     // 0000 0000 0000 1111
       0x8888,     // 1000 1000 1000 1000
       0x4444,     // 0100 0100 0100 0100
       0x2222,     // 0010 0010 0010 0010
       0x1111,     // 0001 0001 0001 0001
       0x8421,     // 1000 0100 0010 0001
       0x1248      // 0001 0010 0100 1000
    };


static const char* solve( FILE *fd, char *inputBuf )
{
    char a, b, c, d;
    unsigned int x = 0;
    unsigned int o = 0;
    bool moves_left = false;

    for( int i=0; i<4; ++i )
    {
        char in[4];

        int numChars = getline( &inputBuf,
                                (size_t*)&maxLen,
                                fd );

        sscanf( inputBuf, "%4c", in );

        for( int k=0; k<4; ++k )
        {
//            printf("%c", in[k]);

            int bit = 15 - (i*4 + k);

            switch( in[k] )
            {
                case 'X':
                    x |= (1 << bit);
                    break;

                case 'O':
                    o |= (1 << bit);
                    break;

                case 'T':
                    x |= (1 << bit);
                    o |= (1 << bit);
                    break;

                case '.':
                    moves_left = true;
                    break;

                default:
                    break;
            }
        }
//        printf("\n");
    }
     
//    printf("x: %4x\n", x);
//    printf("o: %4x\n", o);

    // Search X for win
    for( int i=0; i<10; ++i )
    {
        unsigned int win = winning_pos[i];

//        printf("win: %4x (&x: %4x) (&o: %4x)\n", 
//               win,
//               win & x,
//               win & o);

        if( (win & x) == win )
        {
            return X_WINS;
        }
        else if( (win & o) == win )
        {
            return O_WINS;
        }
    }

    return (moves_left) ? INCOMPLETE : DRAW;
}



int main( int argc, char **argv )
{
    if( argc < 2 )
    {
        printf("!!! NO INPUT FILE !!!\n");
        return -1;
    }

    FILE *fd = (FILE*)fopen(argv[1], "r");

    char *inputBuf = (char*)malloc(maxLen);
    getline( &inputBuf,
             (size_t*)&maxLen,
             fd );

    int cases = strtol(inputBuf, NULL, 10);

    memset(inputBuf, 0, maxLen);

    for( int caseNum=0; caseNum < cases; caseNum++ )
    {
        const char* answer = solve( fd, inputBuf );

        printf("Case #%d: ", caseNum+1);
        printf("%s\n", answer);
        
        // grab blank line between boards
        getline( &inputBuf,
                 (size_t*)&maxLen,
                 fd );
    }

    free(inputBuf);
    fclose(fd);

    return 0;
}

