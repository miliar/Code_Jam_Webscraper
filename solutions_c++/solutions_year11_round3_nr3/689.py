#include <iostream>

using namespace std;

int a[1100];

int n,l,h;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>n>>l>>h;
        for(int i=0;i<n;i++)
        cin>>a[i];

        int ans=-1;
        for(int i=l;i<=h;i++)
        {
            int j;
            for(j=0;j<n;j++)
            {
                if(i%a[j]!=0&&a[j]%i!=0)
                break;
            }
            if(j==n){
            ans=i;break;}
        }


        if(ans==-1)
        cout<<"Case #"<<i<<": NO"<<endl;
        else
        cout<<"Case #"<<i<<": "<<ans<<endl;

    }
    return 0;
}
