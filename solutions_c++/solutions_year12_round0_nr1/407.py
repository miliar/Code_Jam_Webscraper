#include <cstdio>
#include <cctype>
#include <cstring>

using namespace std;

char mat[256];

const char sample_input[3][128] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

const char sample_output[3][128] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

inline void init()
{
    memset(mat, 0, sizeof mat);
    mat['y'] = 'a'; mat['e'] = 'o'; mat['q'] = 'z'; mat['z'] = 'q';

    for (int i = 0; i < 3; ++i)
        for (int j = 0; sample_input[i][j]; ++j)
            mat[sample_input[i][j]] = sample_output[i][j];
}

char buffer_input[4096];
char buffer_output[4096];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int T, i;
    init();
    scanf("%d", &T);
    gets(buffer_input);

    for (int cs = 1; cs <= T; ++cs)
    {
        gets(buffer_input);

        for (i = 0; buffer_input[i]; ++i)
        {
            if (islower(buffer_input[i]))
                buffer_output[i] = mat[buffer_input[i]];
            else
                buffer_output[i] = buffer_input[i];
        }

        buffer_output[i] = '\0';

        printf("Case #%d: %s\n", cs, buffer_output);
    }

    return 0;
}
