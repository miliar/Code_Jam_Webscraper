#include <cstdlib>
#include <cstdio>

using namespace std;

int T;
char map[5][5];
FILE* reader;
FILE* printer;

char readnext()
{
    char c=0;
    do
    {
        fscanf(reader, "%c", &c);
    } while (!(c=='X' || c=='O' || c=='T' || c=='.'));

    return c;
}

bool rowcheck(int r, char p)
{
    bool w=true;
    for(int c=1; c<=4; c++)
        if(map[r][c]!=p && map[r][c]!='T')
            w=false;

    return w;
}

bool columncheck(int c, char p)
{
    bool w=true;
    for(int r=1; r<=4; r++)
        if(map[r][c]!=p && map[r][c]!='T')
            w=false;

    return w;
}

bool diagcheck(char p)
{
    bool w=true;
    for(int i=1; i<=4; i++)
        if(map[i][i]!=p && map[i][i]!='T')
            w=false;

    return w;
}

bool diag2check(char p)
{
    bool w=true;
    for(int i=1; i<=4; i++)
        if(map[i][5-i]!=p && map[i][5-i]!='T')
            w=false;

    return w;
}

int main()
{
    reader = fopen("A-large.in", "r");
    printer = fopen("A-large-out.txt", "w");
    fscanf(reader, "%d", &T);

    for(int case_id=1; case_id<=T; case_id++)
    {
        bool may_draw=true;
        for(int r=1; r<=4; r++)
            for(int c=1; c<=4; c++)
            {
                map[r][c]=readnext();
                //printf("%c", map[r][c]);
                if (map[r][c]=='.')
                    may_draw=false;
            }

        bool x_won=false;
        bool o_won=false;

        x_won=diagcheck('X') | diag2check('X');
        o_won=diagcheck('O') | diag2check('O');

        for(int i=1; i<=4; i++)
        {
            x_won=x_won | rowcheck(i, 'X') | columncheck(i, 'X');
            o_won=o_won | rowcheck(i, 'O') | columncheck(i, 'O');
        }

        fprintf(printer, "Case #%d: ", case_id);
        if(x_won)
            fprintf(printer, "X won\n");
        else if(o_won)
            fprintf(printer, "O won\n");
        else if(may_draw)
            fprintf(printer, "Draw\n");
        else
            fprintf(printer,"Game has not completed\n");
    }



    return 0;
}
