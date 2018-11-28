#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
const int maxn=2222222;
bool vis[maxn];
int main()
{
//freopen("/home/wxf/C-large.in","r",stdin);
//freopen("/home/wxf/C-large.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<cas++<<": ";
        memset(vis,0,maxn);
        int a,b;
        int cnt=0;
        cin>>a>>b;
        for(int i=a;i<=b;i++)
        {
            int tmp=i,len=0,base=1;
            for(int j=i;j;j/=10,len++)base*=10;base/=10;
            int c[10],e=0;
            for(int j=0;j<len;j++)
            {
                tmp=tmp%10*base+tmp/10;
                if(tmp>i&&tmp>=a&&tmp<=b&&!vis[tmp]) c[e++]=tmp,vis[tmp]=1,cnt++;
            }
            for(int j=0;j<e;j++) vis[c[j]]=0;
        }
        cout<<cnt<<endl;
    }
}
