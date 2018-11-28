#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char sol[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int t,i,j;
    char s[1000];
    scanf("%d%*c",&t);
    for(i=1;i<=t;i++)
    {
        gets(s);

        printf("Case #%d: ",i);
        for(j=0;j<strlen(s);j++)
        {
            if(s[j]==' ')
            {
                printf(" ");
            }
            else
            {
                printf("%c",sol[s[j]-'a']);
            }
        }
        printf("\n");
    }
    return 0;
}
