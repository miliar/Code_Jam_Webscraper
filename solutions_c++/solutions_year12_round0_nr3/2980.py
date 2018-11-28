#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
typedef long long ll;
#define M 100005
#define INF 1<<30
int t,n,m;
int a[M],b[M];
bool ss[M];
int fk(int kk,int k)
{
   int ans=0,tmp=0;
   bool c;
   while(1)
   {
       int tm=a[k-1];
       for(int i=k-2;i>=0;i--)
       {
           a[i+1]=a[i];
       }
       a[0]=tm;
       tmp=0;
       c=0;
       for(int i=0;i<k;i++)
       {
           tmp=tmp*10+a[i];
       }
       if(tmp==kk) break;
       if(a[0]==0) continue;
       if(tmp>m) continue;
       if(tmp>kk)
       {
           ans++;
       }
   }
   return ans;
}
int gao()
{
    int ans=0;
    for(int i=n;i<=m;i++)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        int s=i;
        int j=0;
        while(s)
        {
            a[j]=s%10;
            s/=10;
            j++;
        }
        for(int k=0;k<j;k++)
        {
            b[k]=a[j-k-1];
        }
        for(int k=0;k<j;k++)
        a[k]=b[k];
//        if(!ss[i] && fk(i,j))
//        ans++;
        ans+=fk(i,j);
    }
    return ans;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d: ",cas);
        cout<<gao()<<endl;
    }
	return 0;
}
