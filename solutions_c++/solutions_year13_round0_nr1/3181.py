#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main()	{
    int T, i, j, k, countX, countO;
    char grid[6][6];
    int sol;
    bool dot;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	scanf("%d", &T);
	for(i=1; i<=T; i++) {
        for(j=0; j<4; j++)
            scanf("%s", grid[j]);

        sol = -1; dot = false;
        for(j=0; j<4; j++)  {
            countX = countO = 0;
        // check each row
            for(k=0; k<4; k++)  {
                if(grid[j][k] == '.') { dot = true; break; }
                else if(grid[j][k] == 'X') countX++;
                else if(grid[j][k] == 'O') countO++;
                else { countX++; countO++; }
            }
            if(countX == 4) {
                sol = 1; break;
            } else if(countO == 4)  {
                sol = 2; break;
            }

            countX = countO = 0;
        // check each column
            for(k=0; k<4; k++)  {
                if(grid[k][j] == '.') { dot = true; break; }
                else if(grid[k][j] == 'X') countX++;
                else if(grid[k][j] == 'O') countO++;
                else { countX++; countO++; }
            }
            if(countX == 4) {
                sol = 1; break;
            } else if(countO == 4)  {
                sol = 2; break;
            }
        }
        if(sol == -1)   {
            // check the diagonals
            countO = countX = 0;
            for(j=0; j<4; j++)  {
                if(grid[j][j] == '.') { dot = true; break; }
                else if(grid[j][j] == 'X') countX++;
                else if(grid[j][j] == 'O') countO++;
                else { countX++; countO++; }
            }
            if(countX == 4)
                sol = 1;
            else if(countO == 4)
                sol = 2;
        }
        if(sol == -1)   {
            countO = countX = 0;
            for(j=0; j<4; j++)  {
                if(grid[j][3-j] == '.') { dot = true; break; }
                else if(grid[j][3-j] == 'X') countX++;
                else if(grid[j][3-j] == 'O') countO++;
                else { countX++; countO++; }
            }
            if(countX == 4)
                sol = 1;
            else if(countO == 4)
                sol = 2;
        }

        switch(sol) {
            case -1:    if(dot) printf("Case #%d: Game has not completed\n", i);
                        else printf("Case #%d: Draw\n", i);
                        break;
            case 1:     printf("Case #%d: X won\n", i);
                        break;
            case 2:     printf("Case #%d: O won\n", i);
                        break;
        }
	}

	return 0;
}
