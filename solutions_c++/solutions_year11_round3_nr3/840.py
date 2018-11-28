#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output","w",stdout);
    int T,TT=0;
    cin>>T;
    while(T--)
    {
        TT++;
        cout<<"Case #"<<TT<<": ";

        int n,l,h,i,j,flag = 1,a[200],ans=0;

        cin>>n>>l>>h;

        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }

        for(i=l;i<=h;i++)
        {
            flag=1;
            for(j=0;j<n;j++)
            {
                if((a[j]%i == 0) || (i%a[j]==0))
                continue;
                else
                {
                    flag = 0;
                    break;
                }
            }
            if(flag == 1)
            {
                ans = i;
                break;
            }

        }

        if(!flag)
        cout<<"NO\n";
        else
        {
            cout<<ans<<endl;
        }
    }
    return 0;
}
