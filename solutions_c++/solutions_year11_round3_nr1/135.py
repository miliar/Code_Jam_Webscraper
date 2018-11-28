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

#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
#define vi vector<int>
#define vs vector<string>

using namespace std;


int main()
{
    int T;
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        int R, C;
        cin >> R >> C;
        
        char tiles[60][60];
        for(int i = 0; i < R; i++)
            cin >> tiles[i];
            
        bool poss = true;
        for(int i = 0; i < R && poss; i++)
        {
            for(int j = 0; j < C && poss; j++)
            {
                if(tiles[i][j] == '#')
                {
                    if(i + 1 < R && j + 1 < C && tiles[i][j + 1] == '#' && tiles[i+1][j] == '#' && tiles[i+1][j+1] == '#')
                        poss = true;
                    else
                        poss = false;
                        
                    if(poss)
                    {
                        tiles[i][j] = '/';
                        tiles[i][j + 1] = '\\';
                        tiles[i+1][j] = '\\';
                        tiles[i+1][j+1] = '/';
                    }
                }
            }
        }
       
        cout << "Case #" << t + 1 << ": " << endl;
        if(poss)
        {
            for(int i = 0; i < R; i++)
                cout << tiles[i] << endl;
        }
        else
        {
            cout << "Impossible" << endl;
        }
    }
    return 0;
}
