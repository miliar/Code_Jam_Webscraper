#include<stdio.h>
#include<string.h>

int main()
{
    int n,i,len,j;
    char c[110];
    char *s="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d ",&n);
    for(i=1;i<=n;i++)
    {
        gets(c); 
        len=strlen(c);    
        printf("Case #%d: ",i);
        for(j=0;j<len;j++)
        {
            if(c[j]==' ')printf(" ");
            else printf("%c",s[c[j]-'a']);
        }          
        printf("\n");
    }   
    
}
