#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

char s[100];
int a[100];
long long ans;
bool b;

void dfs(int x, long long y)
{
     if (x==strlen(s))
     {
         long long t=(long long)(sqrt(y));
         if (t*t==y)
         {
             b=true;
             ans=y;
         }
         return;
     }
     if (s[x]=='?')
     {
         dfs(x+1,y<<1);
         if (b) return;
         dfs(x+1,(y<<1)+1);
     }
     else
         dfs(x+1,(y<<1)+(long long)(s[x]-'0'));
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T;
    scanf("%d",&T);
    getchar();
    for (int cas=1;cas<=T;cas++)
    {
        gets(s);
        b=0;
        dfs(0,0);
        printf("Case #%d: ",cas);
        int t=0;
        while (ans)
        {
              a[++t]=ans&1;
              ans>>=1;
        }
        
        for (int i=t;i;i--) printf("%d",a[i]);
        printf("\n");
    }
    return 0;
}       
   
    
