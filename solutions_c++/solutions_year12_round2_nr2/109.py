#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;

int flo[100][100];
int cei[100][100];

int go (int i0, int j0, int i1, int j1, int h)
{
    if (cei[i0][j0] - flo[i0][j0] < 50 ||
        cei[i1][j1] - flo[i1][j1] < 50 ||
        cei[i1][j1] - flo[i0][j0] < 50 ||
        cei[i0][j0] - flo[i1][j1] < 50)
        return -1; // never
    if (cei[i1][j1] - h >= 50)
        return 0; // now
    return 50 - (cei[i1][j1] - h);
}

int d[100][100];

int mosse[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

void elabora ()
{
    int n, m, h;
    cin >> h >> n >> m;

    for (int i = 0; i < n; i += 1)
        for (int j = 0; j < m; j += 1)
            cin >> cei[i][j];
    for (int i = 0; i < n; i += 1)
        for (int j = 0; j < m; j += 1)
            cin >> flo[i][j];

    memset(d, -120, sizeof(d));

    priority_queue< pair<int, pair<int,int> > > coda;
    deque< pair<int,int> > coda2;

    d[0][0] = h;
    coda.push(make_pair(h, make_pair(0, 0)));
    coda2.push_back(make_pair(0, 0));

    while (!coda2.empty())
    {
        pair<int,int> pos = coda2.front();
        coda2.pop_front();

        int i0 = pos.first;
        int j0 = pos.second;
        for (int i = 0; i < 4; i += 1)
        {
            int i1 = i0 + mosse[i][0];
            int j1 = j0 + mosse[i][1];
            if (0 <= i1 && i1 < n && 0 <= j1 && j1 < m && d[i1][j1] < h)
            {
                if (go(i0, j0, i1, j1, h) == 0)
                {
                    d[i1][j1] = h;
                    coda.push(make_pair(h, make_pair(i1, j1)));
                    coda2.push_back(make_pair(i1, j1));
                }
            }
        }
    }

    while (!coda.empty())
    {
        pair<int, pair<int,int> > pos = coda.top();
        coda.pop();

        if (d[pos.second.first][pos.second.second] == pos.first)
        {
            int i0 = pos.second.first;
            int j0 = pos.second.second;
            int h0 = pos.first;
            for (int i = 0; i < 4; i += 1)
            {
                int i1 = i0 + mosse[i][0];
                int j1 = j0 + mosse[i][1];
                if (0 <= i1 && i1 < n && 0 <= j1 && j1 < m)
                {
                    int t = go(i0, j0, i1, j1, h0);
                    if (t != -1)
                    {
                        int h1 = h0 - t - ((h0 - t) - flo[i0][j0] >= 20 ? 1 * 10 : 10 * 10);
                        if (d[i1][j1] < h1)
                        {
                            d[i1][j1] = h1;
                            coda.push(make_pair(h1, make_pair(i1, j1)));
                        }
                    }
                }
            }
        }
    }

    /*
    for (int i = 0; i < n; i += 1)
    {
        for (int j = 0; j < m; j += 1)
        {
            cout << d[i][j] << " " ;
        }
        cout << endl;
    }
    */

    cout << float(h - d[n-1][m-1]) / 10 << endl;
}

int main ()
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i += 1)
    {
        cout << "Case #" << i+1 << ": ";
        elabora();
    }
}
