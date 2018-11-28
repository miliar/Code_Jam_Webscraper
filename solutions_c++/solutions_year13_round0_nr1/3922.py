#include <iostream>
#include <fstream>
using namespace std;
char isSame(char a, char b, char c, char d)
{
    if(a=='T' && b==c && c==d) return b;
    if(b=='T' && a==c && c==d) return a;
    if(c=='T' && a==b && b==d) return a;
    if(d=='T' && a==b && b==c) return a;
    if(a==b && b==c && c==d) return a;
    return 0;
}
int main(int argc, char *argv[])
{
    char c[4][4], a;
    int t;
    //cin >> t;
    ifstream fin("A-large.in", ios::in);
    ofstream fout("A.out", ios::out);
    fin >> t;
    for(int k=1; k<=t; k++)
    {
        int flag = 0;
        for(int i=0; i<4; i++) fin >> c[i];
        for(int i=0; i<4; i++)
        {
            a = isSame(c[i][0], c[i][1], c[i][2], c[i][3]);
            if(a=='X') 
            {
                fout << "Case #" << k << ": X won" << endl;
                flag = 1;
                break;
            }
            if(a=='O') 
            {
                fout << "Case #" << k << ": O won" << endl;
                flag = 1;
                break;
            }
            a = isSame(c[0][i], c[1][i], c[2][i], c[3][i]);
            if(a=='X') 
            {
                fout << "Case #" << k << ": X won" << endl;
                flag = 1;
                break;
            }
            if(a=='O') 
            {
                fout << "Case #" << k << ": O won" << endl;
                flag = 1;
                break;
            }
        }
        if(!flag)
        {
            a = isSame(c[0][0], c[1][1], c[2][2], c[3][3]);
            if(a=='X') 
            {
                fout << "Case #" << k << ": X won" << endl;
                flag = 1;
            }
            if(a=='O') 
            {
                fout << "Case #" << k << ": O won" << endl;
                flag = 1;
            }
        }
        if(!flag)
        {
            a = isSame(c[0][3], c[1][2], c[2][1], c[3][0]);
            if(a=='X') 
            {
                fout << "Case #" << k << ": X won" << endl;
                flag = 1;
            }
            if(a=='O') 
            {
                fout << "Case #" << k << ": O won" << endl;
                flag = 1;
            }
        }
        if(!flag)
        {
            for(int i=0; i<4; i++)
            {
                for(int j=0; j<4; j++)
                {
                    if(c[i][j]=='.') 
                    {
                        fout << "Case #" << k << ": Game has not completed" << endl;
                        flag = 1;
                        break;
                    }
                }
                if(flag) break;
            }
            if(!flag) fout << "Case #" << k << ": Draw" << endl;
        }
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
