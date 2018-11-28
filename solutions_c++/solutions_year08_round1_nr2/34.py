#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

const int BufferSize = 10000;

int cases;
int n, m;
vector<int> edges[BufferSize];
vector<int> medges[BufferSize];
vector<int> back[BufferSize];
vector<int> mback[BufferSize];
int malt[BufferSize];
int sat[BufferSize];

int main()
{
    scanf("%d", &cases); 

    for (int index = 1; index <= cases; ++index)
    {
        scanf("%d %d", &n, &m);

        for (int i = 0; i < n; ++i)
        {
            back[i].resize(0);
            mback[i].resize(0);
            malt[i] = 0;
        }
        
        for (int i = 0; i < m; ++i)
        {
            edges[i].resize(0);
            medges[i].resize(0);
            sat[i] = 0;
        }

        queue<int> qu;
        for (int i = 0; i < m; ++i)
        {
            int t;
            scanf("%d", &t);

            for (int j = 0; j < t; ++j)
            {
                int x, y;
                scanf("%d %d", &x, &y);

                --x;
                if (y == 0)
                {
                    edges[i].push_back(x);
                    back[x].push_back(i);
                    ++sat[i];
                }
                else
                {
                    medges[i].push_back(x);
                    mback[x].push_back(i);
                }
            }

            if (sat[i] == 0)
            {
                qu.push(i);
            }
        }
        

        bool flag = true;
        while (flag && !qu.empty())
        {
            int v = qu.front();
            qu.pop();

            if (medges[v].size() == 0)
            {
                flag = false;
                break;
            }

            if (sat[v] > 0)
                continue;

            int x = medges[v][0];
            malt[x] = 1;
            for (int i = 0; i < mback[x].size(); ++i)
            {
                ++sat[mback[x][i]];
            }

            for (int i = 0; i < back[x].size(); ++i)
            {
                --sat[back[x][i]];
                if (sat[back[x][i]] == 0)
                    qu.push(back[x][i]);
            }
        }

        if (flag)
        {
            printf("Case #%d:", index);
            for (int i = 0; i < n; ++i)
                printf(" %d", malt[i]);
            printf("\n");
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", index);
        }
    }

    return 0;
}