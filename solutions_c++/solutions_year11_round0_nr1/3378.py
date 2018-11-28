#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

int n;

int aabs(int n)
{
    if(n<0)
        return(-n);
    return n;
}

struct node
{
    int step,cnt,curPos,nextL;
    int pos[1000];
    int que[1000];
    void init()
    {
        cnt=0;
        step=0;
        curPos=1;
        memset(pos,0,sizeof(pos));
        pos[0]=1;
        memset(que,0,sizeof(que));
    }
    void press()
    {
        step++;
        nextL=aabs(pos[step]-pos[step-1])+1;
    }
}o,b;

void trans(char c,int num,int n)
{
    if(c=='O')
    {
        o.cnt++;
        o.pos[o.cnt]=num;
        o.que[o.cnt]=n;
    }
    else
    {
        b.cnt++;
        b.pos[b.cnt]=num;
        b.que[b.cnt]=n;
    }
}

int main()
{
    int t,tt,i,j,num,sum;
    char c;
    freopen("A-Large.in","r",stdin);
    freopen("A-Large.out","w",stdout);
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        scanf("%d",&n);
        b.init();o.init();
        for(i=0;i<n;i++)
        {
            scanf(" %c %d",&c,&num);
            trans(c,num,i);
        }
        b.press();o.press();sum=0;
        for(i=0;i<n;i++)
        {
            if((b.step>b.cnt)||((o.step<=o.cnt)&&(o.que[o.step]<b.que[b.step])))
            {
                sum+=o.nextL;
                b.nextL-=o.nextL;
                if(b.nextL<1)
                    b.nextL=1;
                o.press();
            }
            else
            {
                sum+=b.nextL;
                o.nextL-=b.nextL;
                if(o.nextL<1)
                    o.nextL=1;
                b.press();
            }
        }
        printf("Case #%d: %d\n",tt,sum);
    }
    return 0;
}
