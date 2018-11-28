#include <iostream>
#include <fstream>

using namespace std;
ifstream in("tik tak.in");
ofstream out("tik tak.out");

int a[4][4];

int work()
{
    for (int i = 0; i < 4; ++i){
        int t1 = a[i][0], t2 = a[0][i];
        if (t1 == 3) t1 = a[i][1];
        if (t2 == 3) t2 = a[1][i];
        bool oriz = 1, vert = 1;
        if (t1 == 0) oriz = 0;
        if (t2 == 0) vert = 0;
        for (int j = 0; j < 4; ++j){
            if (a[i][j] != t1 && a[i][j] != 3) oriz = 0;
            if (a[j][i] != t2 && a[i][j] != 3) vert = 0;
        }
        if (oriz) return t1;
        else if (vert) return t2;
    }

    int t = a[0][0];
    if (t==3) t = a[1][1];
    bool diag = 1;
    for (int i = 0; i < 4; ++i)
        if (a[i][i] != t && a[i][i] != 3) diag = 0;
    if (diag && t) return t;

    t = a[0][3];
    if (t==3) t = a[1][2];
    diag = 1;
    for (int i = 0; i < 4; ++i)
        if (a[i][3-i] != t && a[i][3-i] != 3) diag = 0;
    if (diag && t) return t;
    return -1;
}

void zero()
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        a[i][j] = 0;
}

int draw()
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        if (!a[i][j]) return 0;
    return 1;
}

int main()
{
    int n; in >> n;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
        {
            char t; in >> t;
            if (t == 'X') a[j][k] = 1;
            else if (t == 'O') a[j][k] = 2;
            else if (t == 'T') a[j][k] = 3;
        }
        int t = work();
        out << "Case #" << i+1 << ": ";
        if (t == 1) out << "X won\n";
        else if (t == 2) out << "O won\n";
        else if (t == -1 && draw()) out << "Draw\n";
        else out << "Game has not completed\n";
        zero();
    }
    return 0;
}
