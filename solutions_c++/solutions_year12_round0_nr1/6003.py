#include<stdio.h>
#include<stdlib.h>
#include<cstring>
char table[30]={"yhesocvxduiglbkrztnwjpfmaq"};
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    scanf("%d",&t);
    getchar();
    char in[150];
    for(int i=0;i<t;i++)
    {
        printf("Case #%d: ",i+1);
        gets(in);
        for(int j=0;j<strlen(in);j++)
        {
            char gc = in[j];
            if(gc == ' ')
            {
                printf(" ");
                continue;
            }
            int idx = gc - 'a';
            char eng = table[idx];
            printf("%c",eng);
        }
        printf("\n");
    }
    return 0;
}
