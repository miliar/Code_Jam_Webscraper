#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char map[]={'y','h','e','s','o','c','v','x','d','u',
                            'i','g','l','b','k','r','z','t','n','w',
                                'j','p','f','m','a','q'};


char str[200];
int n;
int main()
{
    freopen("D:\\A-small-attempt0.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    scanf("%d\n",&n);
    for(int i=1;i<=n;i++)
    {
        gets(str);
        int size=strlen(str);
        printf("Case #%d: ",i);
        for(int j=0;j<size;j++)
        {
            if(str[j]==' ')
                printf(" ");
            else
                printf("%c",map[str[j]-'a']);
        }
        printf("\n");
    }
}
