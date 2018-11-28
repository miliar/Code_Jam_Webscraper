#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

char s1[]={"ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"};
char s2[]={"our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"};


char m1[128],m2[128];
int T;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int len=strlen(s1);
    for(int i=0;i<len;i++)
    {
        m1[s1[i]]=s2[i];
        m2[s2[i]]=s1[i];
    }
    m1[113]=122;
    m1[122]=113;
    cin>>T;
    int ca=0;
    getchar();
    char s[200];
    while(T--)
    {
        ca++;
        gets(s);
        int l=strlen(s);
        for(int i=0;i<l;i++)
        {
            if(s[i]==' ') continue;
            s[i]=m1[s[i]];
        }
        cout<<"Case #"<<ca<<": ";
        puts(s);
    }
    return 0;
}







