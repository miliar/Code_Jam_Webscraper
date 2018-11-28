#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("B1.in");
    ofstream fout("B.out");
    int t,n,s,p,z,i,j,a,m,r;
    fin>>t;
    for (i=1;i<=t;i++)
    {
        fin>>n>>s>>p;
        z=0,m=0;
        if (p<2)
        {
                 for (j=1;j<=n;j++)
                 {
                     fin>>a;
                     if (a>=p) z++;
                     if (a>=2) m++;
                 }
                 if (m>=s) r=z;
                 else r=0;
        }
        else
        {
            for (j=1;j<=n;j++)
            {
                fin>>a;
                if (p+(p-2)*2<=a&&a>0)
                {
                                      if (a<=3*(p-1)) m++;
                                      else z++;
                }
            }
            if (m<=s) r=z+m;
            else r=z+s;
        }
        fout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
