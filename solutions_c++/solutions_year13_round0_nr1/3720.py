#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;
const char* fi = "A-large.in";
const char* fo = "output.txt";
const int n = 4;

char a[5][5];
int b[5][5];
bool CheckRow(int row);
bool CheckCol(int col);
bool CheckCross1();
bool CheckCross2();
void ReadFile();
bool finished;

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    int nTest;
    cin >> nTest;
    for (int test=1; test<=nTest; test++)
    {
        ReadFile();
        cout << "Case #" << test << ": ";
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++) b[i][j] = 0;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
                if (a[i][j]=='X' || a[i][j]=='T') b[i][j] = 1;


        /*for (int i=1; i<=n; i++, cout << endl)
            for (int j=1; j<=n; j++) cout << a[i][j];*/
        bool Xwin = false;
        bool Owin = false;
        for (int i=1; i<=n; i++)
            if (CheckRow(i) || CheckCol(i))
            {
                Xwin = true;
                break;
            }

        if (!Xwin) if (CheckCross1() || CheckCross2()) Xwin = true;
        if (!Xwin)
        {
            for (int i=1; i<=n; i++)
                for (int j=1; j<=n; j++) b[i][j] = 0;
            for (int i=1; i<=n; i++)
                for (int j=1; j<=n; j++)
                    if (a[i][j]=='O' || a[i][j]=='T') b[i][j] = 1;
            for (int i=1; i<=n; i++)
            if (CheckRow(i) || CheckCol(i))
            {
                Owin = true;
                break;
            }

            if (!Owin) if (CheckCross1() || CheckCross2()) Owin = true;
        }

        if (!Xwin && !Owin)
        {
            if (!finished) cout << "Game has not completed" << endl;
            else cout << "Draw" << endl;
        }
        else Xwin? cout << "X won" << endl : cout << "O won" << endl;
    }
    return 0;
}

void ReadFile()
{
    finished = true;
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
        {
            cin >> a[i][j];
            if (a[i][j]=='.') finished = false;
        }
}

bool CheckRow(int row)
{
    return (b[row][1]+b[row][2]+b[row][3]+b[row][4]==4);
}

bool CheckCol(int col)
{
    return (b[1][col]+b[2][col]+b[3][col]+b[4][col]==4);
}

bool CheckCross1()
{
    return (b[1][1]+b[2][2]+b[3][3]+b[4][4]==4);
}

bool CheckCross2()
{
    return (b[1][4]+b[2][3]+b[3][2]+b[4][1]==4);
}
