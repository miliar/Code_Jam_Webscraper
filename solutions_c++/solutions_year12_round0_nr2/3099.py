#include <iostream>
#include <fstream>
using namespace std;

int n,s,p;
int x,y;
int a;
ifstream fin("2.in");
ofstream fout("2.out");

int main()
{
    int t,i;
    fin >> t;
    for (i=1;i<=t;i++)
    {
        fin >> n >> s >> p;
        x = y = 0;
        for (int j=0;j<n;j++)
        {
            fin >> a;
            int b,c;
            b = a/3;
            c = a%3;
            switch (c)
            {
                case 0: if (b>=p) x++; else if ((b+1==p)&&(b>0)) y++; break;
                case 1: if (b+1>=p) x++; break;
                case 2: if (b+1>=p) x++; else if (b+2==p) y++; break;
            }
        }
        if (y<=s) x+=y; else x+=s;
        fout << "Case #" << i << ": " << x << endl;
    }
    return 0;
}
