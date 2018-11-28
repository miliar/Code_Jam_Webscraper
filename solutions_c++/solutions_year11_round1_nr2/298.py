#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstdio>

#define MAXLEN 10
#define ALPHA 26

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N, M;
        scanf("%d%d", &N, &M);
        vector<string> dict(N);
        vector<int> kinds(N);
        for (int i = 0; i < N; ++i)
        {
            char w[MAXLEN + 1];
            scanf("%s", w);
            dict[i] = w;
        }
        printf("Case #%d:", testcase);
        for (int i = 0; i < M; ++i)
        {
            char order[ALPHA + 1];
            scanf("%s", order);
            vector<int> orderRev(ALPHA);
            for (int j = 0; j < ALPHA; ++j)
                orderRev[order[j] - 'a'] = j;
            vector<int> ws(N);
            for (int j = 0; j < N; ++j)
                ws[j] = j;
            int maxCost = -1;
            int bestIdx = -1;
            for (int ans = 0; ans < N; ++ans)
            {
                vector<bool> possible(N);
                for (int j = 0; j < N; ++j)
                    possible[j] = (dict[j].size() == dict[ans].size());
                int hidden = dict[ans].size();
                int cost = 0;
                for (int j = 0; j < ALPHA; ++j)
                {
                    bool cand = false;
                    for (int k = 0; k < N; ++k)
                    {
                        if (!possible[k])
                            continue;
                        if (find(dict[k].begin(), dict[k].end(), order[j]) != dict[k].end())
                        {
                            cand = true;
                            break;
                        }
                    }
                    if (!cand)
                        continue;
                    bool penalty = true;
                    ITERATE (it, dict[ans])
                    {
                        if (*it == order[j])
                        {
                            penalty = false;
                            --hidden;
                        }
                    }
                    if (penalty)
                        ++cost;
                    if (hidden == 0)
                        break;
                    for (int k = 0; k < N; ++k)
                    {
                        if (!possible[k])
                            continue;
                        for (int l = 0; l < (int)dict[ans].size(); ++l)
                        {
                            if ((dict[ans][l] == order[j]) != (dict[k][l] == order[j]))
                            {
                                possible[k] = false;
                                break;
                            }
                        }
                    }
                }
                if (cost > maxCost)
                {
                    maxCost = cost;
                    bestIdx = ans;
                }
            }
            printf(" %s", dict[bestIdx].c_str());
        }
        putchar('\n');
    }
    return 0;
}
