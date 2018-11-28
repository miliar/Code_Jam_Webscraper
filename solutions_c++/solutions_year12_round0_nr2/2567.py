#include <iostream>
#include <cstdio>
using namespace std;
int t,n,s,p,r;
bool f1,f2;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("tmp.txt","w",stdout);

    cin>>t;

    for(int q=1;q<=t;q++)
    {
        cin>>n>>s>>p;
        int ans=0;
        for(int w=0;w<n;w++)
        {
            cin>>r;
            f1 = false;
            f2 = false;
            for(int i=0;i<=10;i++)
                for(int j=max(i-2,0);j<=i;j++)
                    for(int k=max(i-2,0);k<=i;k++)
                        if (i+j+k==r && i>=p)
                        {
                            if (j==i-2 || k==i-2) f2=true;
                            else f1=true;
                        }
            if (f1) ans++;
            else if (f2 && s)
            {
                ans++;
                s--;
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<endl;
    }
    return 0;
}
