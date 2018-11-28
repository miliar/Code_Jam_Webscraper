#include <fstream>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

int n,t,ti,j,s,sum,mina,a;

int main()
{
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        s=0; sum=0; mina=10000000;
        fin>>n;
        for(j=1;j<=n;j++) { fin>>a; s^=a; sum+=a; mina=min(mina,a); }
        fout<<"Case #"<<ti<<": ";
        if(s!=0) fout<<"NO"<<endl;
        else fout<<sum-mina<<endl;
    }
    return 0;
}
