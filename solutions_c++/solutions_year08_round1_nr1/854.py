#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int n;
cin>>n;
int c=0;
while(n--)
{
    int s;
    cin>>s;
    int x[s],y[s];
    for(int i=0;i<s;i++)
    cin>>x[i];
    for(int j=0;j<s;j++)
    cin>>y[j];
    //cout<<"*********\n";
    sort(x,x+s);
    sort(y,y+s);
    //cout<<"*********\n";
    long long sum=0;
    for(int i=0;i<s;i++)
    {
    sum+=x[i]*y[s-i-1];
    }
    cout<<"Case #"<<++c<<": "<<sum<<"\n";
}
}
