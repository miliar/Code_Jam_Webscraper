#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <iomanip>
#define N 20

using namespace std;

double a[N];
double b[N];
bool f(double s,double t)
{
    return s>t;
}

int main(int argc, char *argv[])
{
    int t,n;
    int i,j,k;
    int z;
    double x,y;
    double p,q,r;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.out", "w", stdout);
    z=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for(i=0,x=0;i<n;i++)
        {
            cin>>a[i];
            b[i]=a[i];
            x=x+a[i];
        }
        sort(a,&a[n],f);
        y=x*2/n;
        for(i=0,p=0;i<n;i++)
        {
            if(a[i]<=y)
                break;
            p=p+a[i];
        }
        k=i;
        q=(x*2-p)/(n-k);
        cout<<"Case #"<<z<<": ";
        for(i=0;i<n;i++)
        {
            if(i!=0)
                cout<<" ";
            if(b[i]>=y)
                cout<<"0.000000";
            else
                cout<<fixed<<setprecision(6)<<(q-b[i])/x*100;
            //cout<<(y-a[i])/x*100;
        }
        z++;
        cout<<endl;
    }
   // system("PAUSE");
    return 0;
}
