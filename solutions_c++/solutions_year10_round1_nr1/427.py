#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

void pGrid(vector<string> &g)
{
    for (int i = 0;i < g.size();i++)
    {
        cout << g[i] << endl;
    }
}

bool checkRow(vector<string> &g,int K,char c)
{
    int N = g.size();
    for (int i = 0;i < N;i++)
    {
        for (int j = 0;j <= N-K;j++)
        {
            bool found = true;
            for (int k = 0;k < K;k++)
            {
                if (g[i][j+k] != c)
                {
                    found = false;
                    break;
                }
            }
            if (found)
                return true;
        }
    }
}

bool checkCol(vector<string> &g,int K,char c)
{
    int N = g.size();
    for (int j = 0;j < N;j++)
    {
        for (int i = 0;i <= N-K;i++)
        {
            bool found = true;
            for (int k = 0;k < K;k++)
            {
                if (g[i+k][j] != c)
                {
                    found = false;
                    break;
                }
            }
            if (found)
                return true;
        }
    }
}

bool checkdCross(vector<string> &g,int K,char c)
{
    int N = g.size();
    for (int i = 0;i <= N-K;i++)
    {
        for (int j = 0;j <= N-K;j++)
        {
            bool found = true;
            for (int k = 0;k < K;k++)
            {
                if (g[i+k][j+k] != c)
                {
                    found = false;
                    break;
                }
            }
            if (found)
                return true;
        }
    }
}

bool checkuCross(vector<string> &g,int K,char c)
{
    int N = g.size();
    for (int i = 0;i <= N-K;i++)
    {
        for (int j = K-1;j <= N-1;j++)
        {
            bool found = true;
            for (int k = 0;k < K;k++)
            {
                if (g[i+k][j-k] != c)
                {
                    found = false;
                    break;
                }
            }
            if (found)
                return true;
        }
    }
}

inline bool check(vector<string> &g,int K,char c)
{
    return (checkRow(g,K,c) || checkCol(g,K,c) || checkdCross(g,K,c) || checkuCross(g,K,c));
}

int main()
{
    int T = 0;
    cin >> T;
    for (int t = 1;t <= T;t++)
    {
        int N = 0,K = 0;
        cin >> N >> K;
        vector<string> grid;
        for (int n = 0;n < N;n++)
        {
            string s;
            cin >> s;
            grid.push_back(s);
        }

        for (int i = 0;i < N;i++)
        {
            for (int j = 0;j < N-1;j++)
            {
                for (int k = N-2;k >= j;k--)
                {
                    if (grid[i][k] != '.' && grid[i][k+1] == '.')
                    {
                        char c = grid[i][k];
                        grid[i][k] = grid[i][k+1];
                        grid[i][k+1] = c;
                    }
                }
            }
        }

        //pGrid(grid);

        // check
        bool r = check(grid,K,'R');
        bool b = check(grid,K,'B');

        if (r && b)
        {
            printf("Case #%d: Both\n",t);
        }
        else if (r)
        {
            printf("Case #%d: Red\n",t);
        }
        else if (b)
        {
            printf("Case #%d: Blue\n",t);
        }
        else
        {
            printf("Case #%d: Neither\n",t);
        }
    }

    return 0;
}
