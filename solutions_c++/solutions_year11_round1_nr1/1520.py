#include <fstream>

using namespace std;

ifstream fin("A-small-attempt3.in");
ofstream fout("A-small-attempt3.out");

int gcd(int a,int b)
{
    if(a%b==0) return b;
    else return gcd(b,a%b);
}

int t,ti,x1,x2,d,g,n;

int main()
{
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        fin>>n>>d>>g;
        if((g==100 && d!=100) || (g==0 && d!=0)) fout<<"Case #"<<ti<<": Broken"<<endl;
        else 
        if(d==0) 
        {
            if(g!=0)
            {
                x1=100/gcd(100,g);
                if(x1<=n) fout<<"Case #"<<ti<<": Possible"<<endl;
                else fout<<"Case #"<<ti<<": Broken"<<endl;
            }
            else fout<<"Case #"<<ti<<": Possible"<<endl;
        }
        else
        {
            x1=100/gcd(100,d);
            if(x1<=n) fout<<"Case #"<<ti<<": Possible"<<endl;
            else fout<<"Case #"<<ti<<": Broken"<<endl;
            //fout<<d<<' '<<x1<<endl;
        }
    }
    return 0;
}
