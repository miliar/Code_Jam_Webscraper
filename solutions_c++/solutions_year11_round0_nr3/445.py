#include<iostream>
#include<cstdio>

using namespace std;

int ans;
int T;
int a[1010];
int N;
int tmp;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int num=1;num<=T;num++)
    {
        cout<<"Case #"<<num<<": ";
        cin>>N;ans=0;
        for(int i=1;i<=N;i++)
        {
            cin >>a[i];
            ans=ans^a[i];
        }
        if(ans!=0)
            cout<<"NO"<<endl;
        else
        {
            tmp = 1000010;
            for(int i=1;i<=N;i++)
            {
                ans+=a[i];
                if(tmp>a[i])tmp=a[i];
            }
            ans-=tmp;
            cout<<ans<<endl;
        }
    }
    return 0;
}
