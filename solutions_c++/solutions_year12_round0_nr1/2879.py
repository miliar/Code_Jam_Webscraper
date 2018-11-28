#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    char alphabet[27]="yhesocvxduiglbkrztnwjpfmaq";
    char word[101];
    int n;
    scanf("%d",&n);
    gets(word);
    for(int i=0;i<n;i++)
    {
        gets(word);
        for(int j=0;j<strlen(word);j++)
        {
            if(word[j]!=' ')
                word[j]=alphabet[word[j]-'a'];
        }
        printf("Case #%d: ",i+1);
        printf("%s\n",word);
    }
    //system("pause");
}
