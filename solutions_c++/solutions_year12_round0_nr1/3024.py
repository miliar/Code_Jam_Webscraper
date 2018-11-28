#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char map[26]= {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[10000];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t;
    scanf("%d",&t);
    getchar();
    for (int j=0; j<t; ++j)
    {
        gets(str);
        int len=strlen(str);
        printf("Case #%d: ",j+1);
        for (int i=0; i<len; ++i)
        {
            if ( (str[i]>='a' && str[i<='z']) ||  (str[i]>='A' && str[i<='Z']) )
                printf("%c",map[str[i]-'a']);
            else
                printf("%c",str[i]);
        }

        printf("\n");
    }
    return 0;
}
