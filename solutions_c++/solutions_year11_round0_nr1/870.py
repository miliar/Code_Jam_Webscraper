#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int CAS,num;
char c;
int p,po,pb,otime,btime;
int absx(int x)
{
    if(x < 0) return -x;
    return x;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d",&num);
        po = pb = 1;
        otime = btime = 0;
        for(int i = 0;i < num;i++)
        {
            while(scanf("%c",&c) && (c != 'B' && c != 'O'));
            scanf("%d",&p);
            if(c == 'O')
            {
                if(otime + absx(p-po) >= btime)
                    otime = otime + absx(p - po) + 1;
                else otime = btime + 1;
                po = p;
            }
            else
            {
                if(btime + absx(p - pb) >= otime)
                    btime = btime + absx(p - pb) + 1;
                else btime = otime + 1;
                pb = p;
            }
            //printf("po:%d otime:%d pb:%d btime:%d\n",po,otime,pb,btime);
        }
        if(otime > btime)
            printf("Case #%d: %d\n",cas,otime);
        else
            printf("Case #%d: %d\n",cas,btime);
    }
    fclose(stdin);
    fclose(stdout);
}
