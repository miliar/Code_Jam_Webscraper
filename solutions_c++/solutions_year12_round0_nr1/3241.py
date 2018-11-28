
#include <map>

#include <cstdlib>
#include <cstdio>

static const int maxLen = 128;
typedef std::map<char, char> TransMap;

static void generateTranslationTable( TransMap &tr )
{
    tr['a'] = 'y';
    tr['b'] = 'h';
    tr['c'] = 'e';
    tr['d'] = 's';
    tr['e'] = 'o';
    tr['f'] = 'c';
    tr['g'] = 'v';
    tr['h'] = 'x';
    tr['i'] = 'd';
    tr['j'] = 'u';
    tr['k'] = 'i';
    tr['l'] = 'g';
    tr['m'] = 'l';
    tr['n'] = 'b';
    tr['o'] = 'k';
    tr['p'] = 'r';
    tr['q'] = 'z';
    tr['r'] = 't';
    tr['s'] = 'n';
    tr['t'] = 'w';
    tr['u'] = 'j';
    tr['v'] = 'p';
    tr['w'] = 'f';
    tr['x'] = 'm';
    tr['y'] = 'a';
    tr['z'] = 'q';
    tr[' '] = ' ';
}

static void translateFile( FILE *fd, int cases, TransMap &tr )
{
    char *input = (char*)malloc(maxLen);
    int caseNum = 0;

    while(caseNum < cases)
    {
        int numChars = getline( &input,
                                (size_t*)&maxLen,
                                fd );

        if( numChars == 0 )
        {
            break;
        }

        printf("Case #%d: ", ++caseNum);
        for(int i=0; i<numChars; ++i)
        {
            if( input[i] == '\n' )
            {
                break;
            }
            printf("%c", tr[input[i]]);
        }
        printf("\n");
    }
    free(input);
}

int main( int argc, char **argv )
{
    std::map<char,char> tr;

    generateTranslationTable( tr );

    FILE *fd = (FILE*)fopen(argv[1], "r");

    char *input = (char*)malloc(maxLen);
    getline( &input,
             (size_t*)&maxLen,
             fd );

    int cases = strtol(input, NULL, 10);
    free(input);

    translateFile( fd, cases, tr );

    fclose(fd);

    return 0;
}

