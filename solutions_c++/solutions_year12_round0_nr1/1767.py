#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char f[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[1000];
char T;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++)
    {
        gets(s);
        printf("Case #%d: ",t);
        for (int k=0;k<strlen(s);k++)
        if (s[k]>96&&s[k]<97+26)
        {
            s[k]=f[s[k]-97];
        }
        puts(s);
    }
    return 0;
}
