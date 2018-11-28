#include<cstdio>
#include<cstring>
char s[]="yhesocvxduiglbkrztnwjpfmaq",st[110];
int main()
{
    int t;
    scanf("%d",&t);
    gets(st);
    for(int c=1;c<=t;++c)
    {
        gets(st);
        printf("Case #%d: ",c);
        for(int i=0;i<strlen(st);++i)
        {
            if(st[i]!=' ')
            {
                printf("%c",s[st[i]-'a']);
            }
            else printf(" ");
        }
        printf("\n");
    }
    return 0;
}
