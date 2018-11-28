#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

map <char,char> dic;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    dic.clear();
    dic['z']='q';
    dic['q']='z';

    string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string s2="our language is impossible to understand";
    for(int i=0;i<s1.length();i++)
    {
        dic[s1[i]]=s2[i];
    }

    s1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    s2="there are twenty six factorial possibilities";
    for(int i=0;i<s1.length();i++)
    {
        dic[s1[i]]=s2[i];
    }

    s1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    s2="so it is okay if you want to just give up";
    for(int i=0;i<s1.length();i++)
    {
        dic[s1[i]]=s2[i];
    }

 /*   char tmp=0;

    for(char a='a';a<='z';a++){
        tmp^=a;
        tmp^=dic[a];
        cout<<a<<" "<<dic[a]<<endl;}
    cout<<tmp<<endl;
    */
    int t,cas;
    scanf("%d",&t);
    getchar();
    char s[1005];
    for (cas=1;cas<=t;cas++)
    {
        gets(s);
        printf("Case #%d: ",cas);
        for(int i=0;s[i];i++)
        {
            printf("%c",dic[s[i]]);
        }
        printf("\n");
    }
    return 0;
}
