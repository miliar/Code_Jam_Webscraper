#include<iostream>
#include<string.h>
#include<cstring>
#include<algorithm>
using namespace std;
char c[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'},s[500];
long tst,i,j;
int main()
{
    freopen("Ain.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    for (scanf("%ld\n",&tst),j=1;  j<=tst;  j++)
    {
        gets(s);
        for (i=0;i<strlen(s);i++) if (s[i]>='a' && s[i]<='z') s[i]=c[s[i]-97];
        printf("Case #%ld: %s\n",j,s);
    }
    return 0;
}
