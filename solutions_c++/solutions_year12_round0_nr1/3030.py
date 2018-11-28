#include <stdio.h>
#include <string.h>

char cc[103],s[27]={"yhesocvxduiglbkrztnwjpfmaq"};
int main()
{
    int cas,i,t,len;
    scanf("%d",&t);
    getchar();
    for(cas=1;cas<=t;cas++)
    {
        gets(cc);
        printf("Case #%d: ",cas);
        len = strlen(cc);
        for(i=0;i<len;i++)
            if(cc[i]<='z'&&cc[i]>='a')
                printf("%c",s[cc[i]-'a']);
        else printf("%c",cc[i]);
        printf("\n");
    }
    return 0;
}
