#include <cstdio>
#include <cstdlib>

using namespace std;

char change[30]="yhesocvxduiglbkrztnwjpfmaq";

void oku()
{
    int N,i;
    char ch;
    scanf(" %d",&N);
    scanf("%c",&ch);
    for(i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        while(scanf("%c",&ch),ch!='\n')
        {
            if(ch!=' ')
                printf("%c",change[ch-'a']);
            else printf(" ");
        }
        printf("\n");
    }
}

int main()
{
    oku();
    return 0;
}
