#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int i,j,k,n;
char ch[1000];
char ch2[28]="yhesocvxduiglbkrztnwjpfmaq\n";
/*                            1        2*/
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a1.out","w",stdout);
    scanf("%d ",&n);
    for (i=1;i<=n;i++)
    {
        memset(ch,0,sizeof(ch));
        gets(ch);
        printf("Case #%d: ",i);
            for (j=0;j<strlen(ch);j++)
            {
                char ch1=ch[j];
                if (ch1>='a'&&ch1<='z')
                {  ch1=ch2[ch1-'a'];
                }
                printf("%c",ch1);
            }
            printf("\n");

    }
    return 0;
}
