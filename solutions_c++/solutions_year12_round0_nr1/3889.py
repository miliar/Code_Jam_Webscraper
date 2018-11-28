#include<cstdio>
#include<cstring>
char samin[]={"ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"};
char samout[]={"our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"};
char dict[128];
char g[128];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    for(int i=0;samout[i];i++)
         dict[samin[i]]=samout[i];
    //for(int i=0;i<26;i++)
    //   printf("%c %c\n",'a'+i, dict['a'+i]);
    dict['q']='z';
    dict['z']='q';
    int T;
    scanf("%d",&T);
    getchar();
    for(int tt=1;tt<=T;tt++)
    {
         printf("Case #%d: ",tt);
         gets(g);
         for(int i=0;g[i];i++)
             if(g[i]>='a' && g[i]<='z')
             {    
                 putchar(dict[g[i]]);
             }
             else putchar(g[i]);
         puts("");
    }
}
