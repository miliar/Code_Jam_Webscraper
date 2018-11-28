#include<stdio.h>
#include <cstring>
#include <iostream>
using namespace  std;


int main()
{
    char a[110];
    char eng[26]={'y', 'h', 'e', 's', 'o', 'c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t,i, count=1;
    char ch;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("code1.txt","w",stdout);
    scanf("%d",&t);
    getchar();
    
    while (t--)
    {
               scanf("%[^\n][100]s", &a);
               getchar();
               printf("Case #%d: ", count);    
               for (i=0; i<strlen(a);i++)
               {
                   ch=a[i];
                   
                   if (ch==' ')
                   {         printf(" "); 
                         continue;}
                   if (ch<91)
                   {
                             printf("%c",eng[(ch-65)]);
                   }
                   else printf("%c", eng[(ch-97)]);
               }
    printf("\n");
    count++;              
    }

 getchar();
}                        
                   
               
