#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int p[5];
char str[10001];
char ss[10001];
int ll;
int K;

int get_len()
{
    int i,j;
    for(i=0;i<ll;i+=K)
    {
       for(j=0;j<K;j++)
         ss[i+p[j]]=str[i+j];
    }
    int ans=0;
    for(i=0;i<ll;)
    {
       for(i++;i<ll&&ss[i]==ss[i-1];i++);
       ans++;
    }
    return ans;
}

void solve()
{
     int i,ans,tt;
     for(i=0;i<K;i++)
        p[i]=i;
     ans=get_len();
     while(next_permutation(p,p+K))
     {
        tt=get_len();
        if(tt<ans)
           ans=tt;
     }
     printf("%d\n",ans);
}

int main()
{
    int i,T;
    //freopen("D.in","r",stdin);
    //freopen("D.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
       scanf("%d%s",&K,str);
       ll=strlen(str);
       printf("Case #%d: ",i);
       solve();
    }
    return 0;
}
