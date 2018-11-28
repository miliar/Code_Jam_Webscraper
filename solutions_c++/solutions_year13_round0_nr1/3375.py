#include <fstream>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

char A[10][10];
int T, TI;

bool Win (char C)
{
    int i, j, ok=0;

    for (i=1; i<=4; i++)
    {
        ok=1;
        for (j=1; j<=4; j++)
            if (A[i][j]!=C && A[i][j]!='T')
                ok=0;
        if (ok) return 1;
    }

    for (j=1; j<=4; j++)
    {
        ok=1;
        for (i=1; i<=4; i++)
            if (A[i][j]!=C && A[i][j]!='T')
                ok=0;
        if (ok) return 1;
    }

    ok=1;
    for (i=1; i<=4; i++)
        if (A[i][i]!=C && A[i][i]!='T')
            ok=0;
    if (ok) return 1;

    ok=1;
    for (i=1; i<=4; i++)
        if (A[i][5-i]!=C && A[i][5-i]!='T')
            ok=0;
    if (ok) return 1;

    return 0;
}

void Solve ()
{
    if (Win('X'))
    {
        g << "X won";
        return;
    }
    if (Win('O'))
    {
        g << "O won";
        return;
    }
    bool ok=0;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            if (A[i][j]=='.')
                ok=1;

    if (ok==0)
    {
        g << "Draw";
        return;
    }

    g << "Game has not completed";
}

int main ()
{
    f >> T;

    for (TI=1; TI<=T; TI++)
    {
        g << "Case #" << TI << ": ";

        for (int i=1; i<=4; i++)
            f >> (A[i]+1);
        Solve();

        g << '\n';
    }

    f.close();
    g.close();

    return 0;
}
