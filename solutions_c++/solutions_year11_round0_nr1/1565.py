#include"iostream"
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
using namespace std;
char s[5];
int main()
{
    int T,i,j,k,n;
    int pos1,pos2,pos;
    int t1,t2,t,now,cas=1;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        t1=0;
        t2=0;
        pos1=1;
        pos2=1;
        t=0;
        now=0;
        for(i=0;i<n;i++)
        {
            scanf("%s%d",&s,&pos);
            if(s[0]=='O')
            {
                now=abs(pos-pos1)+1;
                if(t1+now>t)
                    t=t1+now;
                else
                    t=t+1;
                t1=t;
                pos1=pos;
            }
            else
            {
                now=abs(pos-pos2)+1;
                if(t2+now>t)
                    t=t2+now;
                else
                    t=t+1;
                t2=t;
                pos2=pos;
            }
        }
        printf("Case #%d: %d\n",cas++,t);
    }
    return 0;
}
