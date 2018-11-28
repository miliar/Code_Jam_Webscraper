//#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>
using namespace std;

ifstream cin("C-small-attempt0.in");
ofstream cout("out.txt");

int index[1000][1000];

string rastavi(string t, int pos)
{
    string a,b;
    a=t.substr(0,pos);
    b=t.substr(pos);
    return b+a;
}

bool recycled(int a, int b)
{
    if (a==b) return true;
    if (index[a][b]!=0)
    {
        if (index[a][b]==1) return false;
        return true;
    }
    char t1[20],t2[20];
    itoa(a,t1,10);
    itoa(b,t2,10);
    string aa(t1),bb(t2);
    for (int i=1;i<aa.length();i++)
    {
        if (rastavi(aa,i)==bb || rastavi(bb,i)==aa) {index[a][b]=2;return true;}
        //cout << rastavi(aa,i) << "!=" << bb << "  " << rastavi(bb,i) << "!=" << aa << endl;
    }
    index[a][b]=1;
    return false;
}

int main()
{
    int a,b,t,r;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        cin >> a >> b;
        r=0;
        for (int k=a;k<b;k++)
        {
            for (int l=k+1;l<=b;l++)
            {
                if (recycled(k,l)) r++;
            }
        }
        cout << "Case #" << i+1 << ": " << r;
        if (i!=t-1) cout << endl;
    }
}
