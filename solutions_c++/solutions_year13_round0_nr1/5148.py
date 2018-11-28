#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
long long n,m,i,j,k,l,t;
char a[10][10],x[10];
bool prvi, drugi,tru;
int main()
{
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    fin>>t;
    for (int o=0; o<t; o++)
    {
        prvi=0;
        drugi=0;
        for (int i=0; i<4; i++)
        fin>>a[i];
        /*for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            fout<<a[i][j];
            fout<<endl;
        }*/
        for (int i=0; i<4; i++)
        {
            tru=1;
            for (int j=0; j<4; j++)
            if (!(a[i][j]=='X' || a[i][j]=='T')) tru=0;
            if (tru) prvi=1;
            tru=1;
            for (int j=0; j<4; j++)
            if (!(a[j][i]=='X' || a[j][i]=='T')) tru=0;
            if (tru) prvi=1;

            tru=1;
            for (int j=0; j<4; j++)
            if (!(a[i][j]=='O' || a[i][j]=='T')) tru=0;
            if (tru) drugi=1;
            tru=1;
            for (int j=0; j<4; j++)
            if (!(a[j][i]=='O' || a[j][i]=='T')) tru=0;
            if (tru) drugi=1;

        }
        tru=1;
        for (int i=0; i<4; i++)
            if (!(a[i][i]=='X' || a[i][i]=='T')) tru=0;
        if (tru) prvi=1;

        tru=1;
        for (int i=0; i<4; i++)
            if (!(a[3-i][i]=='X' || a[3-i][i]=='T')) tru=0;
        if (tru) prvi=1;

        tru=1;
        for (int i=0; i<4; i++)
            if (!(a[i][i]=='O' || a[i][i]=='T')) tru=0;
        if (tru) drugi=1;

        tru=1;
        for (int i=0; i<4; i++)
            if (!(a[3-i][i]=='O' || a[3-i][i]=='T' )) tru=0;
        if (tru) drugi=1;

        if (prvi) {fout<<"Case #"<<o+1<<": X won"<<endl;  continue;}
        if (drugi) {fout<<"Case #"<<o+1<<": O won"<<endl;  continue;}
        tru=1;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                if (a[i][j]=='.') tru=0;
        if (!tru) {fout<<"Case #"<<o+1<<": Game has not completed"<<endl;  continue;}
        fout<<"Case #"<<o+1<<": Draw"<<endl;
    }
    return 0;
}
