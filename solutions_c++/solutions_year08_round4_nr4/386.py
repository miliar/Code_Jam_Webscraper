#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

const int BufferSize = 100000;
const int MaxNum = 1000000000;

int p[BufferSize];
char s[BufferSize];
char t[BufferSize];
int k;
int cases;
int minimum = 0;

void perm();

int main()
{
    scanf("%d", &cases);

    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %s", &k, s);

        for (int i = 0; i < k; ++i)
            p[i] = i;

        minimum = MaxNum;
        while (true)
        {
            perm();

            int count = 1;
            int last = t[0];
            for (int i = 1; t[i]; ++i)
            {
                if (last != t[i])
                {
                    ++count;
                    last = t[i];
                }
            }

            if (count < minimum)
            {
                minimum = count;
            }

            if (!next_permutation(p, p + k))
                break;
        }

        printf("Case #%d: %d\n", index, minimum);
    }

    return 0;
}

void perm()
{
    for (int i = 0; s[i]; i += k)
    {
        for (int j = 0; j < k; ++j)
        {
            t[i + j] = s[i + p[j]];
        }
        t[i + k] = '\0';
    }
}
