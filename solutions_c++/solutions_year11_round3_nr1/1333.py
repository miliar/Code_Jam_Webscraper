#include <cstdio>
#include <cmath>
#include <iostream>
#include <string.h>		// For memset function
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <bitset>
#include <sstream>
#include <map>



using namespace std;

#define FOR( i, L, U ) for(int i=(int)L ; i<=(int)U ; i++ )

typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

VS GRID;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int i, j, k;
    int TC, tc;
    int R, C;

    cin >> TC;

    FOR(tc, 1, TC) {
        cin >> R >> C;

        GRID = VS(R+2);

        FOR(i, 1, R) {
            cin >> GRID[i];

        }
/*
        FOR(i, 1, R) {
            GRID[i][C+1] = '.';
            GRID[R+1][i] = '.';
        }
*/

        bool is_possible = true;

        FOR(i, 1, R) {
            FOR(j, 0, C-1) {
                if(GRID[i][j] == '#') {
                    if(j == C-1 || i == R) is_possible = false;
                    else if(GRID[i][j+1] == '#' && GRID[i+1][j] == '#' && GRID[i+1][j+1] == '#') {
                        GRID[i][j] = '/';
                        GRID[i][j+1] = '\\';
                        GRID[i+1][j] = '\\';
                        GRID[i+1][j+1] = '/';
                    }

                    else is_possible = false;
                }
                if(is_possible == false) break;
            }
            if(is_possible == false) break;
        }

        cout << "Case #" << tc << ":\n" ;
        if(is_possible == true) {
            FOR(i, 1, R) {
                FOR(j, 0, C-1)  {
 //                   if(GRID[i][j] == '/' || GRID[i][j] == '\\')cout << "#";
                     cout << GRID[i][j];
                }
                cout << "\n";
            }
        }
        else cout << "Impossible\n";

        GRID.clear();

    }

	return 0;
}
