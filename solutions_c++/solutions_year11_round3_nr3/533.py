#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("ouptut.txt","wr",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        int a[100];
        int n,l,h;
        cin>>n>>l>>h;
        for(int i=0;i<n;i++)
            cin>>a[i];
        int ans=-1;
        for(int i=l;i<=h;i++)
        {
            bool good=true;
            for(int j=0;j<n;j++)
            if(a[j]%i!=0&&i%a[j]!=0)
            {
                good=false;
                break;
            }
            if(good)
            {
                ans=i;
                break;
            }
        }
        cout<<"Case #"<<test_case+1<<": ";
        if(ans==-1)cout<<"NO\n";
        else cout<<ans<<endl;
    }
    return 0;
}
