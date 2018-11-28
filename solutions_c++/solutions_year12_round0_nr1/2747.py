#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("A-small-attempt8.in", "r", stdin);
    freopen("A-small-attempt8.out", "w", stdout);
    char Dict[26] = {'y', 'h', 'e', 's', 'o',
                     'c', 'v', 'x', 'd', 'u',
                     'i', 'g', 'l', 'b', 'k',
                     'r', 'z', 't', 'n', 'w',
                     'j', 'p', 'f', 'm', 'a', 'q'};
    char G[101];
    int T;

    scanf("%d", &T);
    getchar();
    int i = 1;
    while(T--)
    {
        printf("Case #%d: ", i++);
        memset(G, 0, sizeof(G));
        if(fgets(G, 101, stdin) != NULL)
        {
            for(int i=0; G[i]!='\n' && G[i]!=EOF && i<101; i++)
            {
                if(i==100)
                {
                    getchar();
                    continue;
                }
                if(G[i]!=' ' && G[i]!='\t')
                    putchar(Dict[G[i]-'a']);
                else
                    putchar(G[i]);
            }
            putchar('\n');
        }
    }
    return 0;
}
