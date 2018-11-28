#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstring>
using namespace std;
string str;
int t,i,j,k,l,a,n,s,p,x,y,z;
int main()
{
    ofstream fout ("testout.txt");
    ifstream fin ("testin.txt");
    fin>>t;
    for (j=0; j<t; j++)
    {
        fin>>n>>s>>p;
        x=0;
        y=0;
        z=0;
        for (i=0; i<n; i++)
        {
            fin>>a;
            k=(a+2)/3;
            if (k>=p) {x++; continue;}
            if (p>=2 && a>=3*p-4) y++;
        }
        if (p==0) {fout<<"Case #"<<j+1<<": "<<n<<endl; continue;}
        fout<<"Case #"<<j+1<<": "<<x+min(s,y)<<endl;
    }
    return 0;

}
