#include <cstdio>
#include <cstring>
using namespace std;

#define N 256

int main()
{
        int m[N] = {0};
        int i, n, c, t;
        char s[128];

        char s1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z";
        char s2[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q";

        n = strlen(s1);
        for (i = 0; i < n; ++i)
        {
                c = s1[i];
                m[c] = s2[i];
        }

        scanf("%d\n", &t);
        int j = 0;
        while (scanf("%[^\n]\n", s) == 1)
        {
                ++j;
                printf("Case #%d: ", j);
                n = strlen(s);
                for (i = 0; i < n; ++i)
                {
                        c = s[i];
                        putchar(m[c]);
                }
                putchar('\n');
        }

        return 0;
}

