#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int n,S,P;
int f(int x,int y)
{
    int x2=x,y2=y;
    if(y==1000)
    {
        if(x==1||x==10||x==100)return 1;
        return 0;
    }
    int a[10],b[10];
    a[0]=x%10;x=x/10;
    a[1]=x%10;x=x/10;
    a[2]=x%10;x=x/10;
    b[0]=y%10;y=y/10;
    b[1]=y%10;y=y/10;
    b[2]=y%10;y=y/10;
    x=x2;y=y2;
    if(x/10==0)
    {
        if(y/100==0&&a[0]==b[1]&&b[0]==0)return 1;
        if(a[0]==b[2]&&!b[0]&&!b[1])return 1;
        return 0;
    }
    if(x/100==0&&y/100==0)
    {
    if(a[0]==b[1]&&a[1]==b[0])return 1;
    return 0;
    }
    if(x/100==0&&y/100!=0)
    {
        if(b[0]&&b[1]&&b[2])return 0;
        if(!b[0]&&b[1]==a[0]&&b[2]==a[1])return 1;
        if(!b[1]&&b[0]==a[1]&&b[2]==a[0])return 1;
        return 0;
    }
    if(a[0]==b[2]&&a[1]==b[0]&&a[2]==b[1])return 1;
    if(a[0]==b[1]&&a[1]==b[2]&&a[2]==b[0])return 1;
    return 0;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,k,m,n,l,t,cs=1,ans,a,b;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        scanf("%d%d",&a,&b);
        for(i=a;i<=b;i++)
        for(j=i+1;j<=b;j++)
        if(f(i,j))ans++;
        printf("Case #%d: %d\n",cs++,ans);
    }

}
