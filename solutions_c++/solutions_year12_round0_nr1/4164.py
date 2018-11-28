#include<stdio.h>
#include<string.h>

int main(){
    char c[40][200];
    char alpha[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int n,i=0;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&n);
    for(i=0; i<n; i++)
             scanf(" %[^\n]%*c",c[i]);
             
    for(int j=0;j<i;j++)
    {
        printf("Case #%d: ",j+1);
        for(int k=0;k<strlen(c[j]);k++)
        {       if(c[j][k]==' ')
                              printf(" ");
                else              
                              printf("%c",alpha[c[j][k]-'a']);
                
        }
        printf("\n");
    }
    
    return 0;    
}
