#include <iostream>
#include <cstdio>
using namespace std;
int a[10000];
int T,t;
int l,h,i,k,n;
bool flag;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (t=1; t<=T; t++)
    {
        cin>>n>>l>>h;
        for (i=0; i<n; i++)
         cin>>a[i];
        for (k=l; k<=h;k++)
         {
            flag=true;
            for (i=0; i<n; i++)
            {
             if (a[i]==0) continue;
             if (a[i]%k==0||k%a[i]==0) continue;
             flag=false;
             break;
            }
            if (flag) {
                cout<<"Case #"<<t<<": "<<k<<endl;
                break;
            }
         }
         if (!flag) cout<<"Case #"<<t<<": "<<"NO"<<endl;
    }

    return 0;
}
