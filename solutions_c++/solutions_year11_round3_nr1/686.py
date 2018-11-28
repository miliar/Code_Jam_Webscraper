#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <cassert>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>
#define MP make_pair
#define X first
#define Y second

int main()
{
    int T, i, j, k, R, C;
    string grid[55];
    
    cin >> T;
    for(int caso=1; caso<=T; caso++) {
        cin >> R >> C;
        for(i=0; i<R; i++) cin >> grid[i];
        
        for(i=0; i<R-1; i++) {
            for(j=0; j<C-1; j++) {
                if(grid[i][j] == '#' && grid[i+1][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j+1] == '#') {
                    grid[i][j] = '/';
                    grid[i+1][j] = '\\';
                    grid[i][j+1] =  '\\';
                    grid[i+1][j+1] = '/';
                }
            }
        }
        
        int cont=0;
        for(i=0; i<R; i++) {
            for(j=0; j<C; j++) {
                if(grid[i][j] == '#') cont++;
            }
        }
        
        cout << "Case #" << caso << ":" << endl;
        if(cont > 0) cout << "Impossible\n";
        else {
            for(i=0; i<R; i++) cout << grid[i] << endl;
        }
    }
    return 0;
}
