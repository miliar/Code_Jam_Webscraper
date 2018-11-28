#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef complex<ll> pt;

int T;
string grid[4];
int dx[] = {1, 1, 0, -1};
int dy[] = {0, 1, 1, 1};

bool owned(int i, int j, char play)
{
    return grid[i][j] == play || grid[i][j] == 'T';
}

bool valid(int i, int j)
{
    return 0 <= i && i < 4 && 0 <= j && j < 4;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        for (int i = 0; i < 4; ++i)
            cin >> grid[i];
        int empty = 0;
        char winner = 'T';
        for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            empty += grid[i][j] == '.';
            for (int d = 0; d < 4; ++d)
            if (valid(i+3*dx[d], j+3*dy[d]))
            {
                int x = 0, o = 0;
                for (int k = 0; k < 4; ++k)
                {
                    char c = grid[i+k*dx[d]][j+k*dy[d]];
                    if (c == 'X') x += 2;
                    if (c == 'O') o += 2;
                    if (c == 'T') ++x, ++o;
                }
                if (x >= 7) winner = 'X';
                if (o >= 7) winner = 'O';
            }
        }
        cout << "Case #" << z << ": ";
        if (winner != 'T')
            cout << winner << " won" << endl;
        else if (empty)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }
}
