#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int a[1002],b[1002],ta[1002],tb[1002];
int num,p,T,n;
char tmp;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d",&n);
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        memset(ta,0,sizeof(ta));
        memset(tb,0,sizeof(tb));
        p=0;
        for (int i=1;i<=n;i++){
            scanf("%c%c",&tmp,&tmp);
            scanf("%d",&num);
            if (tmp=='O') {a[++p]=num;ta[p]=num;}else {b[++p]=num;tb[p]=num;}
        }
        for (int i=p;i>=1;i--){
            if (!a[i]) ta[i]=ta[i+1];
            if (!b[i]) tb[i]=tb[i+1];
        }
        scanf("\n");
        int nowx=1,nowy=1;
        int ans=0;
        for (int i=1;i<=p;i++)
            if (a[i]){
               int time=abs(nowx-a[i])+1;
               ans+=time;nowx=a[i];
               if (tb[i]>nowy){
                  if (nowy+time>tb[i]) nowy=tb[i];else nowy+=time;}else{
                  if (nowy-time<tb[i]) nowy=tb[i];else nowy-=time;}
            }else{
               int time=abs(nowy-b[i])+1;
               ans+=time;nowy=b[i];
               if (ta[i]>nowx){
                  if (nowx+time>ta[i]) nowx=ta[i];else nowx+=time;}else{
                  if (nowx-time<ta[i]) nowx=ta[i];else nowx-=time;}
            }
        printf("Case #%d: %d\n",Case,ans);
    }
}
