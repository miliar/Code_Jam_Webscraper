#include <cstdio>
#include <cstring>
#include <functional>
#include <list>
#include <vector>

using namespace std;

typedef pair<char, int> loc;
typedef pair<list<loc>, vector<int> > node;

char vis[101][100][100];
char ro;
int T, N, po, yy, ii, jj, t1, t2, t3;
list<loc> goal;
list<node> q;
node cur;
int main(void)
{
    scanf("%d\n", &T);
    for (yy = 1; yy <= T; yy++)
    {
        scanf("%d\n", &N);
        for (ii = 0; ii < N; ii++)
        {
            scanf("%c %d\n", &ro, &po);
            goal.push_back(make_pair(ro, po));
        }
        memset(vis, 0, sizeof(vis));
        printf("Case #%d: ", yy);
        q.push_back(make_pair(goal, vector<int>(3, 1)));
        vis[q.front().first.size()][q.front().second[0] - 1][q.front().second[1] -
            1] = 1;
        while (!q.empty())
        {
            cur = q.front();
            q.pop_front();
            if (cur.second[0] == cur.first.front().second &&
                cur.first.front().first == 'O')
            {
                cur.first.pop_front();
                for (jj = -1; jj < 2; jj++)
                {
                    t1 = cur.second[0];
                    t2 = cur.second[1];
                    t3 = cur.second[2];
                    cur.second[1] += jj;
                    cur.second[2]++;
                    if (cur.second[0] >= 1 && cur.second[0] <= 100 &&
                        cur.second[1] >= 1 && cur.second[1] <= 100 &&
                        !vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1])
                    {
                        q.push_back(cur);
                        vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1] = 1;
                    }
                    cur.second[0] = t1;
                    cur.second[1] = t2;
                    cur.second[2] = t3;
                }
                if (cur.first.empty())
                {
                    printf("%d\n", cur.second[2]);
                    break;
                }
                continue;
            }
            else if (cur.second[1] == cur.first.front().second &&
                cur.first.front().first == 'B')
            {
                cur.first.pop_front();
                for (ii = -1; ii < 2; ii++)
                {
                    t1 = cur.second[0];
                    t2 = cur.second[1];
                    t3 = cur.second[2];
                    cur.second[0] += ii;
                    cur.second[2]++;
                    if (cur.second[0] >= 1 && cur.second[0] <= 100 &&
                        cur.second[1] >= 1 && cur.second[1] <= 100 &&
                        !vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1])
                    {
                        q.push_back(cur);
                        vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1] = 1;
                    }
                    cur.second[0] = t1;
                    cur.second[1] = t2;
                    cur.second[2] = t3;
                }
                if (cur.first.empty())
                {
                    printf("%d\n", cur.second[2]);
                    break;
                }
                continue;
            }
            //printf("%u %d %d\n", cur.first.size(), cur.second[0] - 1,
            //cur.second[1] - 1);
            for (ii = -1; ii < 2; ii++)
            {
                for (jj = -1; jj < 2; jj++)
                {
                    t1 = cur.second[0];
                    t2 = cur.second[1];
                    t3 = cur.second[2];
                    cur.second[0] += ii;
                    cur.second[1] += jj;
                    cur.second[2]++;
                    if (cur.second[0] >= 1 && cur.second[0] <= 100 &&
                        cur.second[1] >= 1 && cur.second[1] <= 100 &&
                        !vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1])
                    {
                        q.push_back(cur);
                        vis[cur.first.size()][cur.second[0] - 1][cur.second[1] -
                            1] = 1;
                    }
                    cur.second[0] = t1;
                    cur.second[1] = t2;
                    cur.second[2] = t3;
                }
            }
        }
        goal.clear();
        q.clear();
    }
    return 0;
}
