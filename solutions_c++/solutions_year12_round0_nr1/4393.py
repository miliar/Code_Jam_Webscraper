#include<iostream>
#include<cstdio>
#include<cstring>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("outA.txt","w",stdout);
    int num,n,k=1;
    char c,word[110],mm[30]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d",&num);
    scanf("%c",&c);
    while(num--)
    {
        gets(word);
        n=strlen(word);
        printf("Case #%d: ",k++);
        for(int i=0;i<n;i++)
        {
            if(word[i]!=' ')
            {
                printf("%c",mm[word[i]-'a']);
            }
            else
            {
                printf("%c",word[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
