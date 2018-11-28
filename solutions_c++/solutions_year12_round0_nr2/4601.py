#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int calc(int a,int p)
{
    if (a<p)
        return 2;
    else if(a>=3*p-2)
            return 0;
    if(a<3*p-2 && a>=3*p-4)
        return 1;
    else return 2;
}
int main()
{
    int t;
    cin>>t;
    int ans[100];
    for(int i=0;i<t;i++)

    {
        int n,s,p;
        int a[3]={0,0,0};
        cin>>n>>s>>p;
        for(int j=0;j<n;j++)
        {
            int inp;
            cin>>inp;
            a[calc(inp,p)]++;
        }
        if(a[1]>=s)
            a[0]+=s;
        else
            a[0]+=a[1];
        ans[i]=a[0];
    }
    for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
}
