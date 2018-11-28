#include<iostream>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<string>
using namespace std;

string s1,s2;
int len,i,j,T;
char dic[30],buff[1000];
bool done[30];

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    s2="our language is impossible to understand";
    len=s1.length();
    for (i=0;i<len;i++)
    {
        if (s1[i]==' ') continue;
        dic[s1[i]-'a']=s2[i];
    }
    s1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    s2="there are twenty six factorial possibilities";
    len=s1.length();
    for (i=0;i<len;i++)
    {
        if (s1[i]==' ') continue;
        dic[s1[i]-'a']=s2[i];
    }
    s1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    s2="so it is okay if you want to just give up";
    len=s1.length();
    for (i=0;i<len;i++)
    {
        if (s1[i]==' ') continue;
        dic[s1[i]-'a']=s2[i];
    }
    dic[25]='q';
    dic[16]='z';
    scanf("%d",&T); gets(buff);
    for (int tt=1;tt<=T;tt++)
    {
        gets(buff);
        len=strlen(buff);
        printf("Case #%d: ",tt);
        for (i=0;i<len;i++)
            if (buff[i]>='a'&&buff[i]<='z') printf("%c",dic[buff[i]-'a']);
            else printf(" ");
        printf("\n");
    }
    return 0;
}
