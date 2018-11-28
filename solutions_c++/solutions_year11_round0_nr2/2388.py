#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 111;

char combine[256][256];
bool opposed[256][256];

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "r", stdin);
        freopen("out", "w", stdout);
    #endif

    int countTest;
    scanf("%d", &countTest);
    for (int test = 1; test <= countTest; test++)
    {
        printf("Case #%d: ", test);

        memset(combine, 0, sizeof(combine));
        memset(opposed, 0, sizeof(opposed));

        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            char s[7];
            scanf("%s", s);
            combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
        }

        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            char s[7];
            scanf("%s", s);
            opposed[s[1]][s[0]] = opposed[s[0]][s[1]] = true;
        }
                 
        scanf("%d ", &n);
        char ans[MAXN];
        int m = 0;

        for (int i = 0; i < n; i++)
        {
            char c;
            scanf("%c", &c);
            ans[m++] = c;
            if (m > 1 && combine[ans[m - 2]][ans[m - 1]])
            {
                ans[m - 2] = combine[ans[m - 2]][ans[m - 1]];
                m--;
            }
            else
            {
                for (int j = 0; j < m; j++)
                    if (opposed[ans[j]][c])
                    {
                        m = 0;
                        break;
                    }
            }
        }
        ans[m] = 0;
        printf("[");
        for (int i = 0; i < m; i++)
        {
            if (i) printf(", ");
            printf("%c", ans[i]);
        }
        printf("]\n");
    }
    return 0;
}
