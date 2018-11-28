#include <cstdio>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

const char *message = "welcome to code jam";

int ways[2][19];
char line[512];

int main()
{
    int tc;
    scanf("%d", &tc);
    fgets(line, 511, stdin);
    for (int i = 1; i <= tc; ++i)
    {
        fgets(line, 511, stdin);
        int s = 0, t = 1;
        memset(ways, 0, sizeof(ways));
        int len = strlen(line);
        for (int p = 0; p < len; ++p)
        {
            for (int j = 0; j < 19; j++)
            {
                if (message[j] == line[p])
                {
                    ways[t][j] = ways[s][j] + (j > 0 ? ways[s][j - 1] : 1);
                    if (ways[t][j] > 10000)
                    {
                        ways[t][j] -= 10000;
                    }
                }
                else
                {
                    ways[t][j] = ways[s][j];
                }
            }
            s ^= 1, t ^= 1;
        }
        printf("Case #%d: %04d\n", i, ways[s][18]);
    }
    return 0;
}
