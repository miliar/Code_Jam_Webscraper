#include "cstdio"

using namespace std;

int main(void)
{
    int o,o1,o2,b,b1,b2,t,i,ta,time,j,a,bufi,tasko[110],taskb[110],taskn[110];
    char bufc,taskc[110];
    bool moveo,moveb;

    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        time=0;
        o=0;
        b=0;

        scanf("%d",&a);

        for(j=0;j<a;j++)
        {
            //if(j<a-1)scanf(" %c %d",&bufc,&bufi);
            //else scanf("%c %d",&bufc,&bufi);

            scanf("%c",&bufc);
            while(bufc==' ')scanf("%c",&bufc);

            scanf("%d",&bufi);
            
            taskc[j]=bufc;
            taskn[j]=bufi;

            if(bufc=='O')tasko[o++]=bufi;
            else taskb[b++]=bufi;

            //printf("%c %d\n",bufc,bufi);
        }

        o1=1;
        b1=1;

        o2=0;
        b2=0;

        ta=0;

        for(time=0;time<10000;time++)
        {
            if(ta==a)break;

            moveo=moveb=true;

            if(taskc[ta]=='O' && o1==taskn[ta])
            {
                ta++;
                o2++;
                moveo=false;
            }
            else if(taskc[ta]=='B' && b1==taskn[ta])
            {
                ta++;
                b2++;
                moveb=false;
            }

            if(o2<o && o1<tasko[o2] && moveo)o1++;
            else if(o2<o && o1>tasko[o2] && moveo)o1--;

            if(b2<b && b1<taskb[b2] && moveb)b1++;
            else if(b2<b && b1>taskb[b2] && moveb)b1--;
        }

        printf("Case #%d: %d\n",i,time);
    }
    
    return 0;
}
