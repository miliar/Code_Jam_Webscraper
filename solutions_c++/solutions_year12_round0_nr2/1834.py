#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Answer.txt","w",stdout);
    int t,n,s,p,r;
    cin>>t;
    bool fn1,fn2;
    for(int q=1;q<=t;q++)
    {
        cin>>n>>s>>p;
        int ans=0;
        for(int w=0;w<n;w++)
        {
            cin>>r;
            fn1=fn2=false;
            for(int i=0;i<=10;i++)
                for(int j=max(i-2,0);j<=i;j++)
                    for(int k=max(i-2,0);k<=i;k++)
                        if (i+j+k==r && i>=p)
                        {
                            if (j==i-2 || k==i-2)
                                fn2=true;
                            else
                                fn1=true;
                        }
            if (fn1)
                ans++;
            else if (fn2 && s)
            {
                ans++;
                s--;
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<endl;
    }
    return 0;
}
