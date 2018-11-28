#include<iostream>
using namespace std;

int x[1003];
int y[1003];
int n;

bool asd(int i,int j)
{
    if(x[i]>x[j]&&y[i]<y[j])return 1;
    else if(x[i]<x[j]&&y[i]>y[j])return 1;
    return 0;
}
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{

    cin>>n;
    for(int i=1;i<=n;i++)cin>>x[i]>>y[i];
    int an=0;

    for(int i=1;i<n;i++)
    {
    for(int j=i+1;j<=n;j++)
    {
        if(asd(i,j))an++;
    }
    }
    cout<<"Case #"<<i<<": "<<an<<endl;
}

return 0;
}
