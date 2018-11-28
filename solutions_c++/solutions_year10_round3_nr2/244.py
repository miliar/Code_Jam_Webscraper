#include <iostream>
#include <math.h>

using namespace std;

long long a,b,c,kol;

int main()
{
    long long q,t,z,r;
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>a>>b>>c;
        //cout<<a<<" "<<b<<" "<<c<<endl;
        kol=0;
        z=0;
        while (b>a)
        {
           r=b%c;
           b=b/c;
           if (r>0) b++;
           z++;
        }
        //cout<<"!!!!!!!!"<<endl;
        //cout<<z<<endl;
        kol=log(z)/log(2);
        if (log(z)/log(2)>(double)kol+0.001) kol++;
        printf("Case #%d: ",q+1);
        cout<<kol<<endl;
    }
    return 0;
}
