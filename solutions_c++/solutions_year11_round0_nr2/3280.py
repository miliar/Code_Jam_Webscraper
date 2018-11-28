#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
using namespace std;

int T, t = 1;
int C, D, N;
char element[128];
char combine[32][32];
bool opp[32][32];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(scanf("%d", &T); T; --T)
    {
        memset(combine, 0, sizeof(combine));
        memset(opp, 0, sizeof(opp));

        scanf("%d", &C);
        for(int i = 0; i < C; ++i)
        {
            char str[4];
            scanf("%s", str);
            combine[str[0] - 'A'][str[1] - 'A'] = str[2];
            combine[str[1] - 'A'][str[0] - 'A'] = str[2];
        }
        
        scanf("%d", &D);
        for(int i = 0; i <D;++i)
        {
            char str[4];
            scanf("%s", str);
            opp[str[0] - 'A'][str[1] - 'A'] = 1;
            opp[str[1] - 'A'][str[0] - 'A'] = 1;
        }

        scanf("%d", &N);
        scanf("%s", element);
        vector<char> ans;

        for(int i = 0; i < N; ++i)
        {
            if(ans.size() == 0)
                ans.push_back(element[i]);
            else
            {
                if(combine[element[i] - 'A'][ans.back() - 'A'] != 0)
                {
                    ans[ans.size() - 1] = combine[element[i] - 'A'][ans.back() - 'A'];
                    continue;
                }
                for(int j = 0; j < ans.size(); ++j)
                {
                    if(opp[ans[j] - 'A'][element[i] - 'A'])
                    {
                        ans.clear();
                        break;
                    }
                }
                if(ans.size() > 0)
                    ans.push_back(element[i]);
            }
        }
        
        printf("Case #%d: [", t++);
        for(int i = 0; i < ans.size(); ++i)
        {
            printf("%c", ans[i]);
            if(i + 1 < ans.size())
                printf(", ");
        }
        printf("]\n");
    }
}