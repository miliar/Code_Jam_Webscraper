#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

vector<char> qu;
char combi[200][200];
char oppo[200];

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    int T;
    int cases = 0;
    int C, D, N;
    char c1, c2, c3;

    scanf("%d", &T);
    while(cases++ < T)
    {
        qu.clear();
        memset(combi, 0, sizeof(combi));
        memset(oppo, 0, sizeof(oppo));
        scanf("%d", &C);
        for (int i = 0; i < C; i++)
        {
            scanf(" %c%c%c", &c1, &c2, &c3);
            combi[c1][c2] = c3;
            combi[c2][c1] = c3;
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i++)
        {
            scanf(" %c%c", &c1, &c2);
            oppo[c1] = c2;
            oppo[c2] = c1;
        }
        scanf("%d", &N);
        getchar();
        for (int i = 0; i < N; i++)
        {
            scanf("%c", &c1);
            if (qu.empty())
            {
                qu.push_back(c1);
                continue;
            }
            c2 = qu.back();
            if (combi[c1][c2] != 0)
            {
                qu.pop_back();
                qu.push_back(combi[c1][c2]);
                continue;
            }
            if (oppo[c1] != 0)
            {
                if (find(qu.begin(), qu.end(), oppo[c1]) != qu.end())
                {
                    qu.clear();
                    continue;
                }
            }
            qu.push_back(c1);
        }
        printf("Case #%d: ", cases);
        printf("%c", '[');
        if (qu.size() == 1)
        {
            printf("%c", qu[0]);
        }
        else
        {
            for (int i = 0; i < qu.size(); i++)
            {
                if (i == 0)
                {
                    printf("%c,", qu[i]);
                }
                else if (i == qu.size() - 1)
                {
                    printf(" %c", qu[i]);
                }
                else
                {
                    printf(" %c,", qu[i]);
                }
            }
        }
        printf("%c\n", ']');
    }
}
