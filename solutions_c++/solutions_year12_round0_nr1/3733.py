#include <cstdio>
#include <string>
using namespace std;
string enc="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq";
string dec="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz";

char dc(char x)
{
    for(int i=0;i<enc.size();i++)
        if(enc[i]==x)
            return dec[i];
    return x;
}
int main()
{
    string inp;
    int t;
    scanf("%d ",&t);
    char s[500];
    for(int i=1;i<=t;i++)
    {
        gets(s);
        printf("Case #%d: ",i);
        for(int j=0;s[j];j++)
            s[j] = dc(s[j]);
        puts(s);
    }
}
