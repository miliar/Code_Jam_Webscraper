#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int n,l,r;
int num[101];
int main()
{
    freopen("ass.in","r",stdin);
    freopen("ass.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>n>>l>>r;
        for(int i=0;i<n;i++)
            cin>>num[i];
        cout<<"Case #"<<t<<": ";
        int res=-1;
        for(int i=l;i<=r;i++)
        {
            bool flag=true;
            for(int k=0;k<n;k++)
            {
                if(i%num[k]!=0 && num[k]%i!=0)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)
            {
                res=i;
                break;
            }
        }
        if(res!=-1)
            cout<<res<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
