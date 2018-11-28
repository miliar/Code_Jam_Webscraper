#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char hash[27] = "yhesocvxduiglbkrztnwjpfmaq";
char str[150];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i = 0;i < T;i++)
    {
        int len;
        do
        {
            gets(str);
            len = strlen(str);
        }while(len == 0);
        for(int j = 0;j < len;j++)
            if(str[j] != ' ')
                str[j] = hash[str[j]-'a'];
        printf("Case #%d: %s\n",i+1,str);
    }
    fclose(stdin);
    fclose(stdout);
}
