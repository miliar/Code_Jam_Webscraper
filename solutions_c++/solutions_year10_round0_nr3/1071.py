/*

 */
#include <iostream>
#include <cstring>
#include <cstdio>
#define maxv(a,b) (a>=b ? a : b)
#define minv(a,b) (a<=b ? a : b)
using namespace std;
unsigned long long x,r,k,n,Case,g[1001],tim,ans,num[1001],sign[1001],loop,sum;
bool flag[1001];
unsigned long long work()
{
    unsigned long long sum=0;
    memset(flag,0,sizeof(flag));
    while (sum+g[x]<=k && !flag[x]) {
        flag[x]=true;
        sum+=g[x];
        x=(x+1)%n;
        }
    return sum;
}
void display()
{
    cin>>Case;
    for (int j=1;j<=Case;j++) {
        cout<<"Case #"<<j<<": ";
        cin>>r>>k>>n;
        for (int i=0;i<n;i++)
            cin>>g[i];
        memset(num,0,sizeof(num));
        memset(sign,0,sizeof(sign));
        x=0;tim=1;
        while (sign[x]==0) {
            sign[x]=tim;
            num[tim]=num[tim-1]+work();
            tim++;
            }
        loop=tim-sign[x],sum=num[tim-1]-num[sign[x]-1];
        ans=num[sign[x]-1];
        r-=(sign[x]-1);
        ans+=(r/loop)*sum;
        r%=loop;
        while (r--) {
            ans+=work();
            }
        cout<<ans<<endl;
        }
}
int main()
{
    //freopen("C-large2.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    display();
    return 0;
}

