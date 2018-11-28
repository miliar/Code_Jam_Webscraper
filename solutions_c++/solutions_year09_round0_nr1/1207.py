#include <stdio.h>
#include <string.h>

inline int getChar(char x) {return x-'a';}


int main()
{
    int L, D, N, i, j;
    char words[5000][20];
    scanf("%d%d%d", &L, &D, &N);

    for (i=0;i<D;i++)
    {
        scanf("%s", words[i]);
    }

    for (int test = 1;test<=N;test++)
    {
        bool st[15][26];
        for (i=0;i<15;i++)
            for (j=0;j<26;j++)
                st[i][j] = false;

        char patt[1024];
        scanf("%s", patt);
        bool group = false;
        int pos = 0, len = strlen(patt);
        for (i=0;i<len;i++)
        {
            char c = patt[i];
            if (c == '(') group = true;
            else if (c == ')')
            {
                group = false;
                pos++;
            }
            else if (c>='a' && c<='z')
            {
                st[pos][getChar(c)] = true;
                if (!group) pos++;
            }
        }

        int res = 0;
        for (i=0;i<D;i++)
        {
            for (j=0;j<L && st[j][getChar(words[i][j])];j++);

            if (j==L) res++;
        }
        printf("Case #%d: %d\n", test, res);

    }

    return 0;
}
