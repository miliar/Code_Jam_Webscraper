/* TASK:
   LANG: C
   AUTHOR:
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
int T,n;
struct node
{
    int but[105],push[105],cnt,num[105];
}ho,hb;
int q[2][1005],que[1005],opos,bpos,rear,t;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k,l,x;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
        char temp[2];
        opos=1;
        bpos=1;
        hb.cnt=0;
        ho.cnt=0;
        rear=0;
        t=0;
        int t1,t=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",temp);
            scanf("%d",&t1);
            if(temp[0]=='O')
            {
                //ho.but[cnt]=t1;
                que[rear]=1;
                q[1][ho.cnt]=t1;
                ho.cnt++;
                rear++;
            }
            else if(temp[0]=='B')
            {
                //hb.but[cnt]=t1;
                que[rear]=2;
                q[2][hb.cnt]=t1;
                hb.cnt++;
                rear++;
            }
        }
        int now=0;
        ho.cnt=0;
        hb.cnt=0;
        for(i=0;i<rear;i++)
        {
            if(que[i]==1)
            {
                int use;
                use=abs(q[1][ho.cnt]-opos)+1;
                opos=q[1][ho.cnt];
                t+=use;
                if(bpos<q[2][hb.cnt])
                {
                    bpos+=use;
                    if(bpos>q[2][hb.cnt])
                        bpos=q[2][hb.cnt];
                }
                if(bpos>q[2][hb.cnt])
                {
                    bpos-=use;
                    if(bpos<q[2][hb.cnt])
                        bpos=q[2][hb.cnt];
                }
                ho.cnt++;
                //printf("t = %d O = %d\n",t,q[1][ho.cnt-1]);
            }
            if(que[i]==2)
            {
                int use;
                use=abs(q[2][hb.cnt]-bpos)+1;
                bpos=q[2][hb.cnt];
                t+=use;
                if(opos<q[1][ho.cnt])
                {
                    opos+=use;
                    if(opos>q[1][ho.cnt])
                        opos=q[1][ho.cnt];
                }
                if(opos>q[1][ho.cnt])
                {
                    opos-=use;
                    if(opos<q[1][ho.cnt])
                        opos=q[1][ho.cnt];
                }
                hb.cnt++;
                //printf("t = %d B = %d\n",t,q[2][hb.cnt-1]);
            }
        }
        printf("Case #%d: %d\n",j,t);
    }
    scanf(" ");
}
