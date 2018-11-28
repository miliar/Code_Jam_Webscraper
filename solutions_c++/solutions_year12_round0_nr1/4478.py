#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;
string s1[3]={
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
string s2[3]={
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};
map<char,char> pt;
void deal()
{
    int i,j;
    pt.clear();
    for (i=0;i<3;i++)
    {
        for (j=0;j<s1[i].length();j++)
        {
            if (isalpha(s1[i][j]))
            {
               if (pt[s1[i][j]]==0)
                    pt[s1[i][j]]=s2[i][j];
            }
        }
    }
    pt['z']='q';
    pt['q']='z';
}
int main()
{
    deal();
    freopen("E:\\A-small-attempt1.in","r",stdin);
    freopen("E:\\A.out","w",stdout);
    int line=0;
    scanf("%d",&line);
    getchar();
    for (int ca=1;ca<=line;ca++)
    {
        char st[105];
        gets(st);
        printf("Case #%d: ",ca);
        for (int i=0;i<strlen(st);i++)
        {
            if (isalpha(st[i]))
                putchar(pt[st[i]]);
            else
                putchar(st[i]);
        }
        printf("\n");
    }
    return 0;
}
