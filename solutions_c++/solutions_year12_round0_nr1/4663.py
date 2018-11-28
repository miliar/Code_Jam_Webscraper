#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,i,j,p;
    char a[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'},str[101];
    scanf("%d",&t);
    p=t;
 
  gets(str);
    while(t--)
    {
              gets(str);
              for(i=0;str[i]!='\0';i++)
              {
                              if(str[i]>=97 && str[i]<=122)
                              {
                                            str[i]=a[str[i]-97];
                              }
              }
              printf("Case #%d: ",p-t);
              puts(str);
    }
    
    return 0;
}
    
    
    
