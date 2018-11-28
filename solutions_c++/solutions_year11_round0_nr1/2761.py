#include <iostream>
#include <cmath>
int Case,n,p[110][3],at[3],to[3];
char str[5];
int dest(int x,int y)
{
    for (int i=y;i<n;i++)
        if (p[i][0]==x) return p[i][1];
    return at[x];
}
void display()
{
     scanf("%d",&Case);
     for (int ca=1;ca<=Case;ca++) {
           scanf("%d",&n);
           for (int i=0;i<n;i++) {
               scanf("%s%d",str,&p[i][1]);
               p[i][0]=(str[0]=='O')?1:0;
               }
           at[0]=at[1]=1;
           int ret=0;
           for (int i=0;i<n;i++) {
               to[0]=dest(0,i);
               to[1]=dest(1,i);
               int x=p[i][0],y=(p[i][0]==1)?0:1;
               int cost=abs(at[x]-p[i][1])+1;
               ret+=cost;
               at[x]=p[i][1];
               if (to[y]>at[y]) at[y]=at[y]+cost>to[y]?to[y]:at[y]+cost;
               else at[y]=at[y]-cost<to[y]?to[y]:at[y]-cost;
           }
           printf("Case #%d: %d\n",ca,ret);
     }
} 
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    display();
    return 0;
}
