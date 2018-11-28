#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

int R,C,D;

int grid[500][500];

int xsum(int x, int y, int k)
{
    int mul = 1-k;
    int ret = 0;
    for (int i = x; i < x + k; i++, mul+=2)
        for (int j = y; j < y + k; j++)
            ret += mul*grid[i][j];
    ret += (k-1) * grid[x][y];
    ret += (k-1) * grid[x][y+k-1];
    ret -= (k-1) * grid[x+k-1][y];
    ret -= (k-1) * grid[x+k-1][y+k-1];
    return ret;
}

int ysum(int x, int y, int k)
{
    int mul = 1-k;
    int ret = 0;
    for (int j = y; j < y + k; j++, mul += 2)
        for (int i = x; i < x + k; i++)
            ret += mul*grid[i][j];
    ret += (k-1) * grid[x][y];
    ret -= (k-1) * grid[x][y+k-1];
    ret += (k-1) * grid[x+k-1][y];
    ret -= (k-1) * grid[x+k-1][y+k-1];
    return ret;
}

int solve()
{
    for (int k = min(R,C); k >= 3; --k) {
        for (int y = 0; y <= R - k; y++) {
            for (int x = 0; x <= C-k; x++) {
                if (xsum(x,y,k) == 0 && ysum(x,y,k) == 0)
                    return k;
            }
        }
    }
    return -1;
}

int main(int argc, const char* argv[])
{
	int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> R >> C >> D;
        char c;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cin >> c;
                grid[i][j] = c - '0';
            //    cout << grid[i][j] << ' ';
            }
           // cout << endl;
        }
        int ret = solve();
        cout << "Case #" << (t+1) << ": ";
        if (ret >= 3)
            cout << ret << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
