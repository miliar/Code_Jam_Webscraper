#include <fstream>
#include <cstring>
using namespace std;
int t,T,f,u,x,nr,cif,z,a,b,i;
long long sol;
bool used[2000010];
int main()
{
    ifstream fi("recycle.in");
    ofstream fo("recycle.out");
    fi>>T;
    for(t=1;t<=T;t++)
    {
        fi>>a>>b;
        memset(used,0,sizeof(used));
        sol=0;
        for(i=a;i<=b;i++)
        if(!used[i])
        {
            x=i;
            z=1; cif=0;
            while(x!=0) { z*=10; cif++; x/=10; } //numar cifrele
            x=i; cif--; z/=10;
            nr=0;
            used[x]=1; nr=1;
            while(cif--)
            {
                f=x/z;
                u=x%10;
                x=x/10;
                if(!u)  continue;
                x+=z*u;
                if(x>=a and x<=b and !used[x]) { used[x]=1; nr++; }
            }
            if(nr>1)
            sol+=1LL*nr*(nr-1)/2;
        }
        fo<<"Case #"<<t<<": "<<sol<<"\n";
    }
    return 0;
}
