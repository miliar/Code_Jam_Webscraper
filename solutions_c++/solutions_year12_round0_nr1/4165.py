#include<stdio.h>
int main()
{
    int T,t,i;
    char tr[]="yhesocvxduiglbkrztnwjpfmaq",s[101];
    scanf("%d\n",&T);
    for(t=1;t<=T;t++)
    {
        gets(s);
        printf("Case #%d: ",t);
        for(i=0;s[i];i++)
            putchar(s[i]==' '?' ':tr[s[i]-'a']);
        putchar('\n');
    }
}
