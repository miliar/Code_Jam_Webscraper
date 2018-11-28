#include<iostream>
using namespace std;
long long x[107700];
bool m[10077];
int asd(int d)
{
    int g=1;
    int ff=d;
    while(x[d]!=ff)
    {
        d=x[d];
        m[d]=1;
        g++;
    }
    return g;
}
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    int n;
    cin>>n;
    memset(m,0,sizeof(m));
    for(int i=1;i<=n;i++)cin>>x[i];
    int s=0;
    for(int j=1;j<=n;j++)
    {
        if(m[j]==0&&x[j]!=j)
        {
        s+=asd(j);
        m[j]=1;
        }
    }
         cout<<"Case #"<<i<<": "<<s<<endl;
}
return 0;
}
