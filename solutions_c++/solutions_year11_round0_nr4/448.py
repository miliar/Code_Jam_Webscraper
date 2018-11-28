#include<iostream>

using namespace std;

int T;
int N;
int a[1010];
bool v[1010];
int k,ans;
int tmp;
//double ans2,tmp2;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin >> T;
    for(int num=1;num<=T;num++)
    {
        cout<<"Case #"<<num<<": ";
        cin >> N;
        for(int i=1;i<=N;i++)
        cin>>a[i];
/*
        cout<<N<<endl;
        for(int i=1;i<=N;i++)
        cout<<a[i]<<" ";
        cout<<endl;
*/
        ans=0;
        memset(v,0,sizeof(v));
        for(int i=1;i<=N;i++)
        {
            if(a[i]==i || v[i]) continue;
            v[i]=1;tmp=a[i];k=0;
            while(!v[tmp])
            {
                v[tmp]=1;
                tmp=a[tmp];
                k++;
            }
            ans+=k+1;
        }
        cout << ans  <<".000000"<<endl;
    }
    return 0;
}

