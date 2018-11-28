#include<stdio.h>
#include<iostream.h>
#include<string.h>
using namespace std;
int main()
{
    char g[30]={'y','h','e','s','o','c','v','x','d','u','i','g',
    'l','b','k','r','z','t','n','w','j','p','f','m','a','q'},f[300];
    int i,t,c;
    freopen("A-small-attempt3.in","r",stdin);
     freopen("AKN_NRN","w",stdout);
    scanf("%d\n",&t);
    for(i=0;i<t;i++)
    {
                   gets(f);
                    printf("Case #%d: ",(i+1));
                    for(c=0;f[c]!='\0';c++)
                    if(f[c]!=' ')
                    printf("%c",g[f[c]-'a']);
                    else
                    printf(" ");
                    printf("\n");
                    }
                    }
    
