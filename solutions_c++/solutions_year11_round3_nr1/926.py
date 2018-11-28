// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

int t;

int r, c;
VS g;

int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);

    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> t;
    for (int cc = 1; cc <= t; cc++)
    {
        g.clear();
        cin >> r >> c;
        for (int i = 0; i < r; i++)
        {
            string str;
            cin >> str;
            g.push_back(str);
        }

        bool is_ok = true;
        for (int y = 0; y < r; y++)
        {
            for (int x = 0; x < c; x++)
            {
                if (g[y][x] == '#')
                {
                    if (y + 1 < r && x + 1 < c)
                    {
                        if (g[y+1][x] == '#' && g[y+1][x+1] == '#' && g[y][x+1] == '#')
                        {
                            g[y][x] = '/';
                            g[y+1][x] = '\\';
                            g[y][x+1] = '\\';
                            g[y+1][x+1] = '/';
                        }
                        else
                        {
                            is_ok = false;
                        }
                    }
                    else
                    {
                        is_ok = false;
                    }
                }
            }
        }

        cout << "Case #" << cc << ":" << endl;
        if (!is_ok)
        {
            cout << "Impossible" << endl;
            continue;
        }

        for (int i = 0; i < r; i++)
        {
            cout << g[i] << endl;
        }
    }

    return 0;
}
