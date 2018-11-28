#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    freopen("a-small.in","r",stdin);
    freopen("a-small.out","w",stdout);

    char ch[]="yhesocvxduiglbkrztnwjpfmaq";
    int test,Case=1;
    char str[110];

    scanf("%d ",&test);

    while(test--)
    {
        gets(str);

        printf("Case #%d: ",Case++);

        int len = strlen(str);
        for(int i=0; i<len ; i++)
            if(str[i]==' ') printf("%c",str[i]);
            else printf("%c",ch[str[i]-'a']);
        printf("\n");
    }



    return 0;
}
