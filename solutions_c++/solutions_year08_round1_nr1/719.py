#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    int n,ans;
    cin>>T;
    int a[1000],b[1000];
    for(int i=1;i<=T;i++)
    {
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cin>>a[j];
        }
        for(int j=0;j<n;j++)
        {
            cin>>b[j];
        }
        sort(a,a+n);
        sort(b,b+n);
        ans=0;
        for(int j=0;j<n;j++)
        {
            ans += a[j]*b[n-j-1];
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;

        
    }
    return 0;
}