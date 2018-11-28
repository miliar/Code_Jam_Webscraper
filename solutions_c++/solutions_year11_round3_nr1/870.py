#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

typedef pair<int, int> PI;
typedef long long LL;

int R, C;
char input[64][64];

void solve()
{
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
        {
            if (input[i][j] == '.') continue;    
            if (j + 1 < C && i + 1 < R && input[i][j] == '#' && input[i][j + 1] == '#'
             && input[i + 1][j] == '#' && input[i + 1][j + 1] == '#')
             {
                 input[i][j] = '/';
                 input[i][j + 1] = '\\';       
                 input[i + 1][j] = '\\';       
                 input[i + 1][j + 1] = '/';       
             }
        }
        
    bool can = true;    
     for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (input[i][j] == '#') can = false;
    
    if (!can)
    {
       cout << "Impossible" << endl;
       return;
    }
    
    for (int i = 0; i < R; i++)
        cout << input[i] << endl;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> R >> C;
        
        for (int i = 0; i < R; i++)
            cin >> input[i];
        
        cout << "Case #" << t << ":" << endl;
        solve();
    }
    
    return 0;
}
