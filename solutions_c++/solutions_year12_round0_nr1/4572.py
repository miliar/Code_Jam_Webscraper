#include <cstdio>
#include <iostream>
#define maxn 1111

using namespace std;

const char cmap[27]="yhesocvxduiglbkrztnwjpfma";

int n;
char a[maxn + 1];

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%d\n",&n);
    for (int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        char ch;
        fprintf(stderr,"%c\n",cmap[17]);
        while ((ch = getchar())!='\n'){
            if (ch!=' ')
                printf("%c",cmap[ch - 'a']);
            else
                printf(" ");
        }
        printf("\n");
    }
    return 0;
}
