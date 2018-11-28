#include<iostream>
using namespace std;

int x[10013];
int mm[10006][10006];
int ggg(int a,int b)
{
    if(mm[a][b]!=0)return mm[a][b];
    int c;
    int aa=a;
    int bb=b;
    while(b>0)
    {
        c=a;
        a=b;
        b=a%b;
    }
    mm[aa][bb]=a;
    mm[bb][aa]=a;
    return a;
}
int main()
{
    memset(mm,0,sizeof(mm));
int t;
cin>>t;

for(int ii=1;ii<=t;ii++)
{
int n,b,h;
cin>>n>>b>>h;

for(int i=1;i<=n;i++)cin>>x[i];

bool f=0;
int i;
    for(i=b;i<=h;i++)
    {
        f=0;
        for(int j=1;j<=n;j++)
        {
        if(x[j]%i==0||i%x[j]==0)
        {
            continue;
        }
        else
        {
            f=1;
            break;
        }
        }
        if(f==0)break;
    }
    cout<<"Case #"<<ii<<": ";
    if(i>h)cout<<"NO"<<endl;
    else cout<<i<<endl;
}
return 0;
}
