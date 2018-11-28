#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

char m[27];
char sf[3][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char sr[3][128] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

void init()
{
    memset(m, '\0', sizeof(m));

    m['y' - 97] = 'a', m['e' - 97] = 'o', m['q' - 97] = 'z', m['z' - 97] = 'q';

    for(int i = 0; i < 3; i++)
    {
        int ln = strlen(sf[i]);

        for(int j = 0; j < ln; j++)
        {
            if(sf[i][j] == ' ')
            {
                continue;
            }

            m[sf[i][j] - 97] = sr[i][j];
        }
    }
}

int main()
{
    int t, kase = 1;
    char str[128];

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    init();

    scanf("%d", &t);

    getchar();

    while(t--)
    {
        gets(str);

        int ln = strlen(str);

        printf("Case #%d: ", kase++);

        for(int i = 0; i < ln; i++)
        {
            if(str[i] == ' ')
            {
                printf(" ");
                continue;
            }

            printf("%c", m[str[i] - 97]);
        }

        printf("\n");
    }

    return 0;
}
