#include <iostream>
#include <cstdio>
#include <utility>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int r, c;
int blocks;
char map[12][12];

int caseNum;

#define DEBUG -1

typedef struct
{
    bool block[12][12];
    vector<pair<int, int> > pos;
    bool dangerous;

    void print()
    {
        if (caseNum != DEBUG)
            return;
        for (int y = 0; y < r; y++)
        {
            for (int x = 0; x < c; x++)
                if (block[x][y])
                    cerr << "X";
                else
                {
                    if (map[x][y] == '#')
                        cerr << '#';
                    else
                        cerr << ".";
                }
            cerr << endl;
        }
    }
} Config;

long long encode(Config conf)
{
    long long value = 0;
    long long mult = r * c - 1;
    long long count = 0;
    for (int y = 0; y < r; y++)
    {
        for (int x = 0; x < c; x++)
        {
            if (conf.block[x][y]) {
                value += ((long long) (y * c + x - count));
                if (count < (blocks - 1))
                    value *= mult;
                mult--;
                count++;
            }
        }
    }
    value = value * 2;
    if (conf.dangerous)
        value++;
    return value;
}

void decode(long long value, Config &conf)
{
    memset(conf.block, 0, sizeof(conf.block));
    long long mult = r * c - blocks + 1;
    conf.dangerous = (value % 2 == 1);
    value /= 2;
    for (int i = 0; i < blocks; i++)
    {
        long long z = (value % mult) + blocks - i - 1;
        int x = z % c;
        int y = z / c;
        conf.block[x][y] = true;
        conf.pos[i] = make_pair(x, y);
        value /= mult;
        mult++;
    }
}

int cx[4] = {-1, 1, 0, 0};
int cy[4] = {0, 0, -1, 1};

int main()
{
    int caseCount;
    cin >> caseCount;
    for (caseNum = 1; caseNum <= caseCount; caseNum++)
    {
        priority_queue<pair<int, long long>, vector<pair<int, long long> >, greater<pair<int, long long> > > q;

        Config start, goal;
        start.dangerous = goal.dangerous = false;
        cin >> r >> c;
        start.pos.clear(); goal.pos.clear();
        blocks = 0;
        memset(start.block, 0, sizeof(start.block));
        memset(goal.block, 0, sizeof(goal.block));
        for (int y = 0; y < r; y++)
        {
            cin >> ws;
            for (int x = 0; x < c; x++)
            {
                char c;
                cin >> c;
                switch (c)
                {
                case 'o':
                    start.pos.push_back(make_pair(x, y));
                    start.block[x][y] = true;
                    blocks++;
                    break;
                case 'x':
                    goal.pos.push_back(make_pair(x, y));
                    goal.block[x][y] = true;
                    break;
                case 'w':
                    start.pos.push_back(make_pair(x, y));
                    goal.pos.push_back(make_pair(x, y));
                    start.block[x][y] = true;
                    goal.block[x][y] = true;
                    blocks++;
                default:
                    break;
                }
                map[x][y] = c;
            }
        }
        cin >> ws;

        long startNum = encode(start);
        q.push(make_pair(0, startNum));
        long long goalNum = encode(goal);

        if (caseNum == DEBUG)
        {
            cerr << "Start: " << startNum << endl;
            start.print();
            cerr << "Goal: " << goalNum << endl;
            goal.print();
        }

        int numMoves = -1;
        Config cur, next;
        cur.pos.resize(blocks);
        next.pos.resize(blocks);
        set<long long> done;
        done.insert(startNum);
        while (!q.empty())
        {
            int moves = q.top().first;
            long long code = q.top().second;

            if (caseNum == DEBUG)
                cerr << moves << " " << code << endl;

            q.pop();

            if (code == goalNum)
            {
                numMoves = moves;
                break;
            }

            decode(code, cur);

            cur.print();

            for (int i = 0; i < blocks; i++)
            {
                int x = cur.pos[i].first;
                int y = cur.pos[i].second;
                for (int c1 = 0; c1 < 4; c1++)
                {
                    int px = x + cx[c1];
                    int py = y + cy[c1];
                    int dx = x - cx[c1];
                    int dy = y - cy[c1];

                    if (px < 0 || px >= c || py < 0 || py >= r || dx < 0 || dx >= c || dy < 0 || dy >= r || cur.block[px][py] || map[px][py] == '#' || cur.block[dx][dy] || map[dx][dy] == '#')
                        continue;

                    memcpy(next.block, cur.block, sizeof(next.block));
                    next.block[x][y] = false;
                    next.block[dx][dy] = true;

                    bool reached[r][c];
                    memset(reached, 0, sizeof(reached));
                    int reachCount = 1;
                    vector<pair<int, int> > reach;
                    reach.push_back(make_pair(dx, dy));
                    reached[dx][dy] = true;
                    while (!reach.empty())
                    {
                        int rx = reach.back().first;
                        int ry = reach.back().second;
                        reach.pop_back();
                        for (int c2 = 0; c2 < 4; c2++)
                        {
                            int r2x = rx + cx[c2];
                            int r2y = ry + cy[c2];
                            if (r2x < 0 || r2x >= c || r2y < 0 || r2y >= r || !next.block[r2x][r2y])
                                continue;

                            if (!reached[r2x][r2y])
                            {
                                reachCount++;
                                reach.push_back(make_pair(r2x, r2y));
                                reached[r2x][r2y] = true;
                            }
                        }
                    }

                    next.dangerous = (reachCount != blocks);

                    if (!cur.dangerous || !next.dangerous)
                    {
                        next.pos = cur.pos;
                        next.pos[i] = make_pair(dx, dy);
                        long long codeNext = encode(next);

                        if (done.find(codeNext) == done.end())
                        {
                            if (caseNum == DEBUG)
                                cerr << x << " " << y << " " << dx << " " << dy << " " << codeNext << endl;
                            next.print();
                            done.insert(codeNext);
                            q.push(make_pair(moves + 1, codeNext));
                        }
                    }
                }
            }
        }

        cout << "Case #" << caseNum << ": " << numMoves << endl;
    }

    return 0;
}
