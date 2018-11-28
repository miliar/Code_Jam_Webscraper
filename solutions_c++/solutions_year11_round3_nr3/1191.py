#include <iostream>
using namespace std;
int main()
{
    int j,k,t,n,s,end;
    double i,l,h,a[10001];
    cin>>t;
    for (k=1;k<=t;k++)
    {
        end=0;
        cin>>n>>l>>h;
        for (j=1;j<=n;j++) cin>>a[j];
        cout<<"Case #"<<k<<": ";
        for (i=l;i<=h;i++)
        {
            s=0;
            for (j=1;j<=n;j++)
            {
                if (s) break;
                if ((int(i/a[j])!=i/a[j])&&(int(a[j]/i)!=a[j]/i)) s=1;
            }
            if (!s) {cout<<i<<endl;end=1;break;}
        }
        if (!end) cout<<"NO"<<endl;
    }
}
                
