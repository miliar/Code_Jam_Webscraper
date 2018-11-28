#include <iostream>
#include <vector>

using namespace std;

const int maxh = 100;
const int maxw = 100;
const int maxa = 10000;
const int wall = maxa * 10;
int altitude[maxh+2][maxw+2];
char maplabel[maxh+2][maxw+2];
//int dir[4][2] = {0, -1, -1, 0, 1, 0, 0, 1};
int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int flowdir(int r, int c);
int initmap(int h, int w);
inline int unflaged(int r, int c) {return maplabel[r][c] < 4;}


int main()
{
    int t, h, w;
    int i, j, k, map;
    int r, c;
    int nr, nc;
    int direct;
    char label, curch;
    char nameset[26];
    vector<int> deallist;
    cin >> t;
    for (map = 1; map <= t; map++)
    {
        cin >> h >> w;
        initmap(h, w);
        label = 'a';

        for (r = 1; r <= h; r++)
        for (c = 1; c <= w; c++)
        {
            direct = flowdir(r, c);
            //cout << direct << ';';
            if (direct == -1) // sink
            {
                maplabel[r][c] = label++;
                deallist.push_back(r);
                deallist.push_back(c);
            }
            else
            {
                maplabel[r][c] = direct;
            }
        }

        while (!deallist.empty())
        {
            c = deallist.back();
            deallist.pop_back();
            r = deallist.back();
            deallist.pop_back();
            for (i = 0; i < 4; i++)
            {
                nr = r + dir[i][0];
                nc = c + dir[i][1];
                if (unflaged(nr, nc) && (maplabel[nr][nc] + i == 3))
                {
                    maplabel[nr][nc] = maplabel[r][c];
                    deallist.push_back(nr);
                    deallist.push_back(nc);
                }
            }
        }

        // rename label
        for (i = 0; i < 26; i++)
        {
            nameset[i] = '\0';
        }
        label = 'a';

        for (r = 1; r <= h; r++)
        for (c = 1; c <= w; c++)
        {
            curch = maplabel[r][c];
            if(nameset[curch - 'a'] == '\0')
            {
                nameset[curch - 'a'] = label++;
            }
        }

        cout << "Case #" << map << ":" << endl;
        for (r = 1; r <= h; r++)
        for (c = 1; c <= w; c++)
        {
            cout << nameset[maplabel[r][c] - 'a'];
            if (c == w)
                cout << endl;
            else
                cout << ' ';
        }
    }
    return 0;
}

// return -1 for sink
int flowdir(int r, int c)
{
    int lowest = altitude[r][c];
    int direct = -1;
    int t;
    for (int i = 0; i < 4; i++)
    {
        t = altitude[r+dir[i][0]][c+dir[i][1]];
        if (t < lowest)
        {
            lowest = t;
            direct = i;
        }
    }
    return direct;
}

int initmap(int h, int w)
{
    int r, c;
    for (r = 1; r <= h; r++)
    for (c = 1; c <= w; c++)
    {
        cin >> altitude[r][c];
    }
    for (r = 1; r <= h; r++)
    {
        altitude[r][0] = wall;
        maplabel[r][0] = '-';
        altitude[r][w+1] = wall;
        maplabel[r][w+1] = '-';
    }
    for (c = 1; c <= w; c++)
    {
        altitude[0][c] = wall;
        maplabel[0][c] = '-';
        altitude[h+1][c] = wall;
        maplabel[h+1][c] = '-';
    }
}

