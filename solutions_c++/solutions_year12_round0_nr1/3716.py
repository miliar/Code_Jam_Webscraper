#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char a[]={"abcdefghijklmnopqrstuvwxyz"};
char b[]={"yhesocvxduiglbkrztnwjpfmaq"};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_ans.out","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    char input[10000];
    getchar();
    for(i=0;i<t;++i)
    {
        printf("Case #%d: ",i+1);
        gets(input);
        int l=strlen(input);
        for(j=0;j<l;++j)
        {
            for(k=0;k<26;++k)
            {
                if(input[j]==a[k])
                {
                    input[j]=b[k];
                    break;
                }
            }
            printf("%c",input[j]);
        }
        putchar('\n');
    }
    return 0;
}
