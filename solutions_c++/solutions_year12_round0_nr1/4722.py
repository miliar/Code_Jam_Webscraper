#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char ai[27];
void calc(char b[])
{
    for(int i=0;i<strlen(b);i++)
    {
        if(b[i]!=' ' && b[i]!='\0')
        {
            b[i]=ai[b[i]-97];
        }
    }
}
void call()
{
    ai[27]='\0';
    char s[]="y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvz";
    char g[]="a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upq";
    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]!=' ')
            ai[s[i]-97]=g[i];
    }
}
int main()
{
    char a[32][102];
    call();
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        fflush(stdin);
        cin.getline(a[i],101);
        calc(a[i]);
    }
    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<a[i]<<'\n';
    }
}
