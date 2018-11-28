#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int i,j,t,t0,n,s,p,ar[102],tmp,cs,mod;
    float div;
    FILE *fp,*fo;
    fp=fopen("B-large.in","r");
    fo=fopen("op.txt","w");
    fscanf(fp,"%d",&t);
    t0=t;
    t=1;
    while(t<=t0)
    {
        fscanf(fp,"\n%d %d %d",&n,&s,&p);
        for(i=0;i<n;i++)
            fscanf(fp," %d",&ar[i]);
        cs=0;
        for(i=0;i<n;i++)
        {
            mod=ar[i]%3;
            div=ar[i]/3.00;
            if(ar[i]==0)
             {
                if(p==0)
                    cs++;
                goto end;
             }
            if(div>(p-1))
            {
                cs++;
                goto end;
            }
            if(div==(p-1))
                if(s>0)
                {
                    s--;
                    cs++;
                    goto end;
                }
            if(div<(p-1)&&div>(p-2))
                if(mod==2&&s>0)
                {
                    s--;
                    cs++;
                    goto end;
                }
            end:;
        }
        fprintf(fo,"Case #%d: %d\n",t,cs);
        t++;
    }
    fclose(fo);
    fclose(fp);
    return 0;
}
