#include <iostream>
using namespace std;
int main()
{
    int i,j,t,s1,s2,c,minc,n,w;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>n;
        w=0;s1=0;s2=0;
        for (j=1;j<=n;j++)
        {
            cin>>c;
            if (j==1) minc=c;
            if (minc>=c) minc=c;
            s1+=c;
            s2^=c;
        }
        if (s2) cout<<"Case #"<<i<<": NO"<<endl;
        else cout<<"Case #"<<i<<": "<<s1-minc<<endl;
    }
}
