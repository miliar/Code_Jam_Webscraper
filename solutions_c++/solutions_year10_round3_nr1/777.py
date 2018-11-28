#include<fstream>

using namespace std;

const char iname[]="A.in";
const char oname[]="A.out";
const int maxn=1005;

ifstream f(iname);
ofstream g(oname);

int a[maxn],n,i,rez,t,p,b[maxn],j;

int main()
{
    f>>t;
    for(p=1;p<=t;++p)
    {
        f>>n;
        rez=0;
        for(i=1;i<=n;++i)
        {
            f>>a[i]>>b[i];
            for(j=1;j<i;++j)
                if((a[i]>a[j]&&b[i]<b[j])||(a[i]<a[j]&&b[i]>b[j]))
                    ++rez;
        }
        g<<"Case #"<<p<<": "<<rez<<"\n";
    }

    return 0;
}
