#include <cstdio>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
using namespace std;

#define MP make_pair
#define FF first
#define CC second
#define SS size()
#define PB push_back
#define BB begin()
#define EE end()
#define all(x)  (x).begin(), (x).end()
#define for0(a,b) for (int a = 0; a < (b); ++a)
#define for1(a,b) for (int a = 1; a < (b); ++a)

typedef long long LL;
typedef vector<int> vint;
typedef pair<int, int> pii;

#define EPS (1e-7)



bool tryOffset(int x, int y, vector<vector<int> > &grid, int ek) {
    int gside = grid.SS;
    //printf("Grid side %d. Trying offset %d %d in ek %d\n", gside, x, y, ek);
    for0 (row, gside) {
        for0 (i, gside) {
            int xcell = x + i;
            int ycell = y + row;
            int mirror1_x = ycell;
            int mirror1_y = xcell;
            int mirror2_x = ek - ycell-1;
            int mirror2_y = ek - xcell-1;

            int m1x_grid = mirror1_x - x;
            int m1y_grid = mirror1_y - y;
            int m2x_grid = mirror2_x - x;
            int m2y_grid = mirror2_y - y;

            if (0 <= m1x_grid && m1x_grid < gside
            &&  0 <= m1y_grid && m1y_grid < gside) {
                if (grid[row][i] != grid[m1y_grid][m1x_grid]) {
                    //printf("%d %d not same as %d %d\n",
                    //        row, i, m1y_grid, m1x_grid);
                    return false;
                }
            }
            if (0 <= m2y_grid && m2y_grid < gside
            &&  0 <= m2x_grid && m2x_grid < gside) {
                if (grid[row][i] != grid[m2y_grid][m2x_grid]) {
                    //printf("%d %d not same as %d %d\n",
                    //        row, i, m2y_grid, m2x_grid);
                    return false;

                }
                
            }
        }
    }

    return true;
}


int main() {
    int t;

    cin >> t;

    for0 (tcase, t) {
        int k;

        cin >> k;

        vector<vector<int> > grid(k, vector<int>(k, -1));
        for0 (line, 2*k-1) {
            int sum = line;
            int start = 0;
            if (line >= k)
                start = line - k+1;
            for (int split = start; split <= sum-start; split++) {
                //fprintf(stderr, "Filling %d %d\n", sum-split, split);
                //fflush(stderr);
                int v;
                cin >> v;
                grid[sum-split][split] = v;
            }
        }

        /*
        for0 (line, k) {
            for0 (i, k) {
                cout << grid[line][i] << " ";
            }
            cout << endl;
        }
        */

        int found_ek = -1;
        for (int ek=k; ek < 4*k+1; ek++) {
            int side = ek-k;

            for (int x = 0; x <= side; x++) {
                if (tryOffset(x, 0, grid, ek)) {
                    found_ek = ek;
                    break;
                }
                if (tryOffset(x, side, grid, ek)) {
                    found_ek = ek;
                    break;
                }
            }
            if (-1 != found_ek)
                break;
            for (int y = 0; y <= side; y++) {
                if (tryOffset(0, y, grid, ek)) {
                    found_ek = ek;
                    break;
                }
                if (tryOffset(side, y, grid, ek)) {
                    found_ek = ek;
                    break;
                }
            }
            if (-1 != found_ek) {
                break;
            }
        }

        int diff = found_ek-k;
        printf("Case #%d: %d\n", tcase+1, found_ek*found_ek - k*k);

        
    }


    return 0;
}

