#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int nn,ll,rr;
int number[101];
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
        cin>>nn>>ll>>rr;
        for(int i=0;i<nn;i++)
            cin>>number[i];
        cout<<"Case #"<<t<<": ";
        int ans=-1;
        for(int i=ll;i<=rr;i++)
        {
            bool flag=true;
            for(int j=0;j<nn;j++)
            {
                if(i%number[j]!=0 && number[j]%i!=0)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)
            {
                ans=i;
                break;
            }
        }
        if(ans!=-1)
            cout<<ans<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

