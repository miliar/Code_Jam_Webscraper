#include <cstdio>

char t[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    int n;
    scanf("%d", &n);
    getchar();
    for(int i=1; i<=n; i++)
    {
        printf("Case #%d: ", i);
        char c;
        while( (c = getchar()) != (i != n ? '\n' : EOF) )
            printf("%c", c == ' ' ? ' ' : t[c-'a']);
        printf("\n");
    }
    return 0;
}