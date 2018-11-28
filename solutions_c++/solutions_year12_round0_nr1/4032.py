#include<stdio.h>
int main(){
    
    char replacement[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r','z','t','n','w','j','p','f','m','a','q'};
    
    int cases,i,j;
    char g[101];
    
    scanf("%d",&cases);
    gets(g);
    for(j=1; j<=cases; j++){
                   
                   gets(g);
                   printf("Case #%d: ",j);
                   for(i=0; g[i]!='\0'; i++){
                            
                            if(g[i]==' ') putchar(' ');
                            else putchar(replacement[g[i]-'a']);
                        }
                   printf("\n");
          }
    
    return 0;
    }
