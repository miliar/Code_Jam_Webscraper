#include <iostream>
#include <cassert>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

// N, W, E, S
int cx[4] = {0, -1, 1, 0};
int cy[4] = {-1, 0, 0, 1};

int main()
{
    int t;
    cin >> t;

    assert(1 <= t && t <= 100);

    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        int w, h;
        cin >> h >> w;
        assert(1 <= w && w <= 100);
        assert(1 <= h && h <= 100);

        int map[w][h];
        bool done[w][h];
        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++)
            {
                cin >> map[x][y];
                assert(0 <= map[x][y] && map[x][y] <= 10000);
                done[x][y] = false;
            }

        vector<int> flowFrom[w][h];
        vector<pair<int, int> > sinks;

        for (int x = 0; x < w; x++)
            for (int y = 0; y < h; y++)
            {
                int best = -1;
                int height = map[x][y];
                for (int c = 0; c < 4; c++)
                {
                    int nx = x + cx[c];
                    int ny = y + cy[c];

                    if (nx < 0 || nx >= w || ny < 0 || ny >= h)
                        continue;

                    if (map[nx][ny] < height)
                    {
                        height = map[nx][ny];
                        best = c;
                    }
                }

                if (best == -1)
                {
                    sinks.push_back(make_pair(x, y));
                }
                else
                {
                    int dx = x + cx[best];
                    int dy = y + cy[best];
                    flowFrom[dx][dy].push_back(best);
                }
            }

        char letters[26];
        assert(sinks.size() <= 26);
        for (unsigned int i = 0; i < sinks.size(); i++)
        {
            letters[i] = '*';
            queue<pair<int, int> > q;
            q.push(sinks[i]);

            while (!q.empty())
            {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();

                if (done[x][y])
                    continue;

                done[x][y] = true;
                map[x][y] = i;

                for (unsigned int j = 0; j < flowFrom[x][y].size(); j++)
                {
                    int nx = x - cx[flowFrom[x][y][j]];
                    int ny = y - cy[flowFrom[x][y][j]];
                    q.push(make_pair(nx, ny));
                }
            }
        }

        cout << "Case #" << caseNum << ":" << endl;
        char curLetter = 'a';
        for (int y = 0; y < h; y++)
        {
            for (int x = 0; x < w; x++)
            {
                int sink = map[x][y];
                if (letters[sink] == '*')
                    letters[sink] = curLetter++;
                if (x > 0)
                    cout << " ";
                cout << letters[sink];
            }
            cout << endl;
        }
    }

    return 0;
}
