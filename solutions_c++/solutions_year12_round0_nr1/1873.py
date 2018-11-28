#include<stdio.h>


char x[]= "zyeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char y[]= "qaoz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char map[300];
char ans[300],s[300];
int main()
{
    int i;
    for(i=0; i<300; i++)
        map[i]='.';
    for(i=0; y[i] ;i++)
    {
        map[x[i]] = y[i];
        map[x[i]-'a'+'A'] = y[i]-'a'+'A';
    }
            
    
    FILE *in=fopen("one.txt","r");
    FILE *out=fopen("output.txt","w");
    int q,qq;
    fscanf(in,"%d\n",&q);
    for(qq=1; qq<=q ;qq++)
    {
        int i=0;
        do{
        fscanf(in,"%c",&s[i]);
        }while(s[i++]==' ');
        s[0] = s[i-1];
        i=0;
        while(s[i++]!='\n')
            fscanf(in,"%c",&s[i]);
        s[i]=0;
        while(s[--i]==' ')
            s[i] = 0;
        for(i=0; s[i] ;i++)
            if((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z'))
                ans[i]= map[s[i]];
            else
                ans[i]= s[i];
        ans[i]=0;
        fprintf(out,"Case #%d: %s",qq,ans);
    }
    return 0;
}
