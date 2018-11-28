#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;
int T,n;
const int INF=0x3f3f3f3f;
int myabs(int x)
{
    return x>0?x:(-x);
}
int main()
{
    freopen("CL.in","r",stdin);
    freopen("cout1.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>n;
        cout<<"Case #"<<t<<": ";
        int sum=0;
        int min=INF;
        int sum1=0;
        int tmp;
        for(int i=1;i<=n;i++)
        {
            cin>>tmp;
            if(tmp<min)
                min=tmp;
            sum^=tmp;
            sum1+=tmp;
        }
        if(sum!=0)
            cout<<"NO"<<endl;
        else cout<<sum1-min<<endl;
    }
    return 0;
}
