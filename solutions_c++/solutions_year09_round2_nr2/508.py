#include<iostream>
#include<string.h>
using namespace std;
#define myfor(i,c,d) for(i = (c);i<=(d);++i)
char st[2000];
void swap2(char &a,char &b)
{
    char tmp = a;
    a = b;
    b = tmp;
}
void work()
{
    int k,j,i,len,c;
    len = strlen(st);
    for(i = len-1;i;--i)
    {
        if(st[i]>st[i-1])
        {
            k = st[i];
            c = i;
            for(j = i;j<len;++j)
                if(st[j]<k&&st[j]>st[i-1])
                {
                    k = st[j];
                    c = j;
                }
           swap2(st[i-1],st[c]);
           for(j = i;j<len;++j)
               for(k = j+1;k<len;++k)
                   if(st[j]>st[k]) swap2(st[j],st[k]);
           printf("%s\n",st);
           return;
        }
    }
    i = len-1;
    while(st[i]=='0'&&i>=0)--i;
    if(i<0)++i;
    putchar(st[i]);
    int t;
    for(t = i;t<len;++t)putchar('0');
    for(t = i-1;t>=0;--t)putchar(st[t]);
    putchar('\n');
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,tcase;
    scanf("%d",&tcase);
    for(tt = 1;tt<=tcase;++tt)
    {
        scanf("%s",&st);
        printf("Case #%d: ",tt);
        work();
    }
}