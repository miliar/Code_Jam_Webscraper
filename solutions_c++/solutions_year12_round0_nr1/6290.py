#include<stdio.h>
#include <string.h>
int main()
{
    
    int t,i,j,k,l=0;
    char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    char b[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char g[102];
    scanf("%d",&t);
    fgets(g,102,stdin);
    for(i=0;i<t;i++)
    {
                     fgets(g,102,stdin);
                     l=strlen(g); 
                     g[l-1]='\0';
                     for(j=0;g[j]!='\0';j++)
                     {
                                            for(k=0;k<26;k++)
                                            {
                                                             if(g[j]==a[k])
                                                             {
                                                             g[j]=b[k];
                                                             break;
                                                             }
                                            }
                      }
                                                             printf("Case #%d: %s",(i+1),g);
                                                             printf("\n");
       }
                                  
return 0;
}

