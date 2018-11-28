#include <fstream>
#include <iostream>
using namespace std;

fstream fin,fout;
int T;

char c;
int a[4][4];
int ok;

bool xx(int a, int b)
{
    if (a != 3 && a != b) return true;
    return false;
}


bool find(int x)
{
    int check = 1;
    for (int i = 0; i < 4; i++) if (xx(a[i][i],x)) check = 0;
    if (check) { return true;}
    check = 1;
    for (int i = 0; i < 4; i++) if (xx(a[i][3-i],x)) check = 0;
    if (check) { return true;}
    for (int i = 0; i < 4; i++)
    {
        check = 1;
        for (int j = 0; j < 4; j++) if (xx(a[i][j],x)) check = 0;
        if (check) { return true;}
        check = 1;
        for (int j = 0; j < 4; j++) if (xx(a[j][i],x)) check = 0;
        if (check) { return true;}
    }
    return false;
}

int main()
{
    fin.open("A-large (1).in",ios::in);
    fout.open("test1.txt",ios::out);
    fin >> T;
    for (int k = 0; k < T; k++)
    {
        ok = 1;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                    fin >> c;
                    a[i][j] = 0;
                    if (c == 'X') a[i][j] = 1;
                    else if (c == 'O') a[i][j] = 2;
                    else if  (c == 'T') a[i][j] = 3;
                    if (a[i][j] == 0) ok = 0;
            }
        }
        if (find(1)) fout << "Case #"<< k+1 << ": X won" << endl;
        else if (find(2)) fout << "Case #"<< k+1 << ": O won" << endl;
        else if (ok) fout << "Case #"<< k+1 << ": Draw" << endl;
        else fout << "Case #"<< k+1 << ": Game has not completed" << endl;
    }
    fout.close();
    return 0;
}
