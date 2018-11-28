/*
ID: ytytyt12
PROG: 
LANG: C++
*/

#include <fstream>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("D-large.out");

int main()
{
    int t,ti,n,s,a,i;
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        s=0;
        fin>>n;
        for(i=1;i<=n;i++)
        {
            fin>>a;
            if(a!=i) s++;
        }
        fout<<"Case #"<<ti<<": "<<s<<".000000"<<endl;
    }
    return 0;
}
