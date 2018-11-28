#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> P;
int N;
int rec[109][109][109];
P goals[109];

typedef pair<int, P> PP;

int filt(int n, int size)
{
    return min(max(0, n), size);
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum <= T; testnum++)
    {
        int bound[2] = {};
        int N;
        scanf("%d", &N);
        for(int i = 0; i < N; i++)
        {
            int p;
            char c;
            scanf(" %c%d", &c, &p);
            goals[i] = P(c == 'B', p - 1);
            bound[c == 'B'] = max(bound[c == 'B'], p - 1);
        }

        queue<PP> que;
        
        
        memset(rec, 0, sizeof(rec));
        que.push(PP(0, P(0, 0)));
        int ans = -1;
        for(int step = 0; ans < 0 && que.size(); step++)
            for(int z = que.size(); z > 0; z--)
            {
                PP p = que.front();
                que.pop();

                if(p.first == N)
                {
                    ans = step;
                    break;
                }

                for(int d1 = -1; d1 <= 1; d1++)
                    for(int d2 = -1; d2 <= 1; d2++)
                    {
                        int inc = goals[p.first].first? (d1 == 0) && (goals[p.first].second == p.second.first)
                                                      : (d2 == 0) && (goals[p.first].second == p.second.second);
                        PP next = PP(p.first + inc, P(filt(p.second.first + d1, bound[1]), filt(p.second.second + d2, bound[0])));
                        int& r = rec[next.first][next.second.first][next.second.second];
                        if(!r)
                        {
                            r = step + 1;
                            que.push(next);
                        }
                    }
            }
        
    

        printf("Case #%d: ", testnum);
        printf("%d\n", ans);
    }

    return 0;
}
