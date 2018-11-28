#include<stdio.h>
#include<string.h>

char s1[40]="abcdefghijklmnopqrstuvwxyz";
char s2[40]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
    freopen("A-small-attempt0.in.","r",stdin);
    freopen("out.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    char str[105];
    gets(str);
    for (int i=1;i<=amm;i++)
    {
        gets(str);
        printf("Case #%d: ",i);
        int len=strlen(str);
        for (int j=0;j<len;j++)
        {
            if (str[j]==' ')printf(" ");
            else printf("%c",s2[str[j]-'a']);    
        }
        printf("\n");
    
    }
    return 0;   
}
