#include<iostream>
#include<stdio.h>
#include<string>
#include<cstring>
using namespace std;
int maps[26];
char sf[120],st[120];
int l=0;
void maping()
{
    int n=strlen(sf);
    for (int i=0;i<n;i++)
    if (sf[i]!=' ')
    maps[sf[i]-'a']=st[i]-'a';
}
void mainwork()
{
    l++;
    printf("Case #%d: ",l);
    string s;
    getline(cin,s,'\n');
    for (int i=0;i<s.length();i++)
    {
        char x=s[i];
        if (x!=' ')  x=maps[x-'a']+'a';
        printf("%c",x);
    }
    printf("\n");
}
int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("out1.txt","w",stdout);
    maps[0]='y'-'a';
    maps['o'-'a']='e'-'a';
    maps['z'-'a']='q'-'a';
    strcpy(sf,"ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(st,"our language is impossible to understand");
    maping();
    strcpy(sf,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(st,"there are twenty six factorial possibilities");
    maping();
    strcpy(sf,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(st,"so it is okay if you want to just give up");
    maping();
    maps[16]=25;
   // for (int i=0;i<26;i++)  cout<<maps[i]<<' ';
    int t;
    scanf("%d\n",&t);
    while (t--)
    mainwork();
    return 0;
}
