#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
int mp[100]={0};
int main()
{
    char* s1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char* s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    char st[1000];
    int lp,tstcss,len,i;
    mp['y'-'a']='a'-'a';
    mp['e'-'a']='o'-'a';
    mp['q'-'a']='z'-'a';
    mp['z'-'a']='q'-'a';
    len=strlen(s1);
    for (i=0;i<len;i++)
    {
        if (s1[i]==' ') continue;
        mp[s1[i]-'a']=s2[i]-'a';
    }
    scanf("%d\n",&tstcss);
    for (lp=0;lp<tstcss;lp++)
    {
        gets(st);
        cout<<"Case #"<<lp+1<<": ";
        len=strlen(st);
        for (i=0;i<len;i++)
        {
            if (st[i]==' ') cout<<' '; else cout<<(char)(mp[st[i]-'a']+'a');
        }
        cout<<endl;
    }
    return 0;
}
