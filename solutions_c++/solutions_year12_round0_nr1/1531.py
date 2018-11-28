#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <map>

using namespace std;

map<char,char> code;

const string dest[3]={"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

const string src[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

void init()
{
    for(int i=0;i<3;++i)
    {
        for(int j=0;j<src[i].length();++j)
        {
            if(src[i][j]>='a' && src[i][j]<='z')
                code[src[i][j]]=dest[i][j];
        }
    }
    code['z']='q';
    code['q']='z';
    //cout<<code.size()<<endl;
}
int t;

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    //freopen("t.txt","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    init();
    scanf("%d\n",&t);
    char a[110];
    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        gets(a);
        for(int j=0;j<strlen(a);++j)
        {
            if(a[j]>='a' && a[j]<='z')
                putchar(code[a[j]]);
            else
                putchar(a[j]);
        }
        printf("\n");
    }
}
