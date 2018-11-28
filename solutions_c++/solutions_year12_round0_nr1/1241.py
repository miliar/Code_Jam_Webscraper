#include"stdio.h"
char trans[27]={"yhesocvxduiglbkrztnwjpfmaq"},s[110];
int n,i,j;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    scanf("%d",&n);
    getchar();
    for(i=1;i<=n;i++)
    {
        gets(s);
        printf("Case #%d: ",i);
        for(j=0;s[j];j++)
            if(s[j]==' ') printf(" ");
            else printf("%c",trans[s[j]-97]);
        printf("\n");
    }
    //scanf(" ");
}
