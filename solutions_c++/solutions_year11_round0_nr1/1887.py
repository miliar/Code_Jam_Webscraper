#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN=105;
struct State
{
  char color;
  int pos;
};
State states[MAXN];
int abs(int a)
{
    if(a<0) return -a;
    return a;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int cas,cnt,n,i,j,ans,p1,p2,t1,t2,m;
    char str[3];
    scanf("%d",&cas);
    for(cnt=1;cnt<=cas;cnt++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s %d",str,&states[i].pos);
            states[i].color=str[0];
        }
        p1=p2=1;
        ans=0;
        for(i=0;i<n;i++)
        {
            if(states[i].color=='O')
            {
               t1=abs(states[i].pos-p2)+1;
               ans+=t1;
               p2=states[i].pos;
               for(j=i+1;j<n;j++) if(states[j].color=='B') break;
               if(j<n)
               {
                   t2=abs(states[j].pos-p1)+1;
                   if(t2>t1) m=t1;
                   else m=t2-1;
                   if(states[j].pos>p1) p1+=m;
                   else p1-=m;
               }
            }
            else
            {
               t1=abs(states[i].pos-p1)+1;
               ans+=t1;
               p1=states[i].pos;
               for(j=i+1;j<n;j++) if(states[j].color=='O') break;
               if(j<n)
               {
                   t2=abs(states[j].pos-p2)+1;
                   if(t2>t1) m=t1;
                   else m=t2-1;
                   if(states[j].pos>p2) p2+=m;
                   else p2-=m;
               }
            }
        }
        printf("Case #%d: %d\n",cnt,ans);
    }
}
