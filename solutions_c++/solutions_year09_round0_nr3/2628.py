#include <cstdio>
#include <cstring>

using namespace std;

char *pattern = "welcome to code jam";
const int patlen = 19;
const int max_textlen = 510;

int results[max_textlen][patlen + 1];

char text[max_textlen];

int main()
{
    int n;

    scanf("%d\n", &n);

    for (int i = 1; i <= n; ++i)
    {
        fgets(text, max_textlen, stdin);
        int len = strlen(text);

        for (int j = 0; j <= len; ++j)
            results[j][0] = 1;
        for (int j = 1; j <= patlen; ++j)
            results[0][j] = 0;

        for (int j = 1; j <= len; ++j)
            for (int k = 1; k <= patlen; ++k)
                if (text[j - 1] == pattern[k - 1])
                    results[j][k] = (results[j - 1][k] + results[j - 1][k - 1]) % 10000;
                else
                    results[j][k] = results[j - 1][k];

        printf("Case #%d: %04d\n", i, results[len][patlen]);
    }

    return 0;
}
