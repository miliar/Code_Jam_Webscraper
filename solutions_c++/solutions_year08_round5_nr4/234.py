#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int H, W, R;
bool bad[128][128];

void read_one()
{
   int i, x, y;
   cin >> H >> W >> R;
  
   memset(bad, 0, sizeof(bad));
   
   for (i = 0; i < R; i++) {
        cin >> x >> y;
        bad[x][y] = true;
   }
}

int C[128][128];

void solve_one()
{
    int i, j;

    memset(C, 0, sizeof(C));

    C[1][1] = 1;

    for (i = 1; i <= H; i++)
    for (j = 1; j <= W; j++) {
        if (! bad[i][j]) {
        C[i + 1][j + 2] += C[i][j]; C[i + 1][j + 2] %= 10007;
        C[i + 2][j + 1] += C[i][j]; C[i + 2][j + 1] %= 10007;
        }
    }

    cout << C[H][W];
}

int main(void)
{
    int T, i;

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

