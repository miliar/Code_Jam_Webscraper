#include<iostream>
#include<stdio.h>
using namespace std;
int d[200];
int main()
{
    FILE *p,*in;
    p=fopen("out.txt","w");
    in=fopen("A-large.in","r");
    int t,i,base,count,COUNT1=1;
    long long sum=0,mut;
    char c[100];
    fscanf(in,"%d",&t);
    while(t--)
    {
        fscanf(in,"%s",c);
        memset(d,0xff,sizeof(d));
        count=1;base=0;
        for(i=0;c[i]!='\0';i++)
        {
            if(d[c[i]]==-1)
            {
                if(count==1) 
                {
                   d[c[i]]=count;
                   count=0;
                }
                else if(count==0)
                {
                    d[c[i]]=count;
                    count=2;
                }
                else
                {
                    d[c[i]]=count;
                    count++;
                }
            }
            base++;
        }
        if(count<2) count=2;
        base--;mut=1;sum=0;
        for(i=base;i>=0;i--)
        {
            sum+=mut*d[c[i]];
            mut*=count;
        }
        fprintf(p,"Case #%d: %I64d\n",COUNT1++,sum);
    }
    return 0;
}
                   
