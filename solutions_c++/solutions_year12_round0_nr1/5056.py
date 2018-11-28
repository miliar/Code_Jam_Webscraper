#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char ch[30];
char in[1000];
char out[1000];
char in1[1000]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char out1[1000]="our language is impossible to understand";
char in2[1000]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char out2[1000]="there are twenty six factorial possibilities";
char in3[1000]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
char out3[1000]="so it is okay if you want to just give up"; 
int main()
{
    int x[100];
    for(int i=0;i<26;i++)x[i]=-1;
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("outA.txt","w",stdout);
    for(int i=0;i<26;i++)
        ch[i]='*';
    int len;
    len=strlen(in1);
    for(int i=0;i<len;i++)
    {
        if(in1[i]!=' ')
            ch[in1[i]-'a']=out1[i];
    }
    len=strlen(in2);
    for(int i=0;i<len;i++)
    {
        if(in2[i]!=' ')
            ch[in2[i]-'a']=out2[i];
    }
    len=strlen(in3);
    for(int i=0;i<len;i++)
    {
        if(in3[i]!=' ')
            ch[in3[i]-'a']=out3[i];
    }
    //ch[0]='y';
    //ch['o'-'a']='e';
    ch['z'-'a']='q';
    ch['q'-'a']='z';
    int n;
    /*for(int i=0;i<26;i++)
    {
        x[ch[i]-'a']=1;
        printf("%c %c\n",i+'a',ch[i]);
    }
    for(int i=0;i<26;i++)
    {
        if(x[i]==-1)
            printf("%c\n",i+'a');
    }*/
    scanf("%d",&n);
    getchar();
    int cs=0;
    while(n--)
    {
        gets(in);
        len=strlen(in);
        for(int i=0;i<len;i++)
        {
            if(in[i]!=' ')
                out[i]=ch[in[i]-'a'];
            else
                out[i]=' ';
        }
        out[len]='\0';
        printf("Case #%d: ",++cs);
        puts(out);
    }
    return 0;
}
