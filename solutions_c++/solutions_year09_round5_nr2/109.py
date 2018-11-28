#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int N = 1005,INF = 1<<29;
const double eps = 1e-10;
const double pi = acos(-1.);
const long  P = 10009;
int n,m;
int t;
char s[105],str[105][105];
int ct[27];
char xt[1006];
long  cal(char *x)
{
  //  puts(x);
    memset(ct,0,sizeof(ct));
    for(int i=0;x[i];i++)
        ct[x[i]-'a']++;
    long  res = 0,tmp=0;
    for(int i=0;s[i];i++)
    {
        if(s[i]=='+')
        {
            res+=tmp;
            res%=P;
        }
        else
        {
            tmp=1;
            for(;s[i]&&s[i]!='+';i++)
            {
                tmp*=ct[s[i]-'a'];
                tmp%=P;
            }
            i--;
        }
    }
    res+=tmp;
    return res%P;
}
long long c[205][25];
long long C(int x,int y)
{
    if(x==y||y==0)return 1;
    if(c[x][y]!=-1)return c[x][y];
    c[x][y]=(C(x-1,y)+C(x-1,y-1))%P;
    return c[x][y];
}
long  ans[15];
int sta[100];
void dfs(int y)
{
    char st[1006];
    st[0]=0;
    for(int i=0;i<y;i++)
    {
        strcat(st,str[sta[i]]);
    }
    ans[y]+=cal(st);
    ans[y]%=P;
    if(y>=t)return;

    for(int i=0;i<n;i++)
    {
        sta[y]=i;
        dfs(y+1);
    }
}
int main()
{

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    memset(c,-1,sizeof(c));
    int T,K=1;
    int i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        memset(ans,0,sizeof(ans));
        printf("Case #%d:",K++);
        scanf("%s%d",s,&t);
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",str[i]);
        }
        dfs(0);
        for(i=1;i<=t;i++)printf(" %d",ans[i]);puts("");
        /*long long ans = 0;
        for(i=0;i<n;i++)
        {
            ans+=cal(i);
            ans%=P;
        }
        for(i=1;i<=t;i++)
        {
            printf(" %d",C(n-1,i-1)*ans%P);
        }
        puts("");*/
    }
    return 0;
}
