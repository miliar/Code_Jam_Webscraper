#include <cctype>
#include <cstdio>

using namespace std;

char code[] = { 'y',
'h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int T, ii, jj;
char buffer[1000];

int main(void)
{
    scanf("%d\n", &T);
    for (ii = 1; ii <= T; ii++)
    {
        scanf("%[^\n]\n", buffer);
        printf("Case #%d: ", ii);
        for (jj = 0; buffer[jj] != 0; jj++)
            if (isalpha(buffer[jj]))
                printf("%c", code[buffer[jj] - 'a']);
            else
                printf("%c", buffer[jj]);
        printf("\n");
    }
    return 0;
}
