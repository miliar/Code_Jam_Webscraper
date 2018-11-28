#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,v[1005],x,max;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        x=0;
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cin>>v[j];
            x=x^v[j];
        }
        cout<<"Case #"<<i<<": ";
        if(x!=0)
            cout<<"NO\n";
        else
        {
            sort(v,v+n);
            max=0;
            for(int j=1;j<n;j++)
                max+=v[j];
            cout<<max<<endl;
        }
    }
    return 0;
}
