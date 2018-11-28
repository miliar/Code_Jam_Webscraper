#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

char g[26][26];
vector <int> o[26];
int cnt[26];
char ans[200];

void init()
{
    int cas;

    scanf("%d", &cas);
    for (int k = 1; k <= cas; ++k)
    {
        int C, D, N;

        memset(g, 0, sizeof(g));
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < 26; ++i)
            o[i].clear();
        scanf("%d", &C);
        for (int i = 0; i < C; ++i)
        {
            char str[4];
            scanf("%s", str);
            g[str[0]-'A'][str[1]-'A'] = g[str[1]-'A'][str[0]-'A'] = str[2];
        }
        scanf("%d", &D);
        for (int i = 0; i < D; ++i)
        {
            char str[3];
            scanf("%s", str);
            o[str[0]-'A'].push_back(str[1]-'A');
            o[str[1]-'A'].push_back(str[0]-'A');
        }
        scanf("%d", &N);
        char s[200];
        int pos = -1;
        scanf("%s", s);
        for (int i = 0; i < N; ++i)
        {
            ans[++pos] = s[i];
            ++cnt[ans[pos]-'A'];
            if (pos > 0)
            {
                if (g[ans[pos]-'A'][ans[pos-1]-'A'])
                {
                    --cnt[ans[pos]-'A'];
                    --cnt[ans[pos-1]-'A'];
                    ans[pos-1] = g[ans[pos]-'A'][ans[pos-1]-'A'];
                    --pos;
                }
                for (int j = 0; j < o[ans[pos]-'A'].size(); ++j)
                    if (cnt[o[ans[pos]-'A'][j]] > 0)
                    {
                        pos = -1;
                        memset(cnt, 0, sizeof(cnt));
                    }
            }
        }
        printf("Case #%d: [", k);
        if (pos > -1)
        {
            printf("%c", ans[0]);
            for (int i = 1; i <= pos; ++i)
                printf(", %c", ans[i]);
        }
        printf("]\n");
    }
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    init();
    fclose(stdin);
    fclose(stdout);
    return 0;
}