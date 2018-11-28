
#define _CRT_SECURE_NO_WARNINGS
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
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "A"
#define INPUT_SIZE "small" //"large" //  


int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);
		
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
  freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

  // Read inputs
	int T; 
	scanf("%d\n", &T); // remember to put \n

	rep(i,T) {
    char g[4][4];

		scanf("%c%c%c%c\n",  &g[0][0], &g[0][1], &g[0][2], &g[0][3]); // remember to put \n
		scanf("%c%c%c%c\n",  &g[1][0], &g[1][1], &g[1][2], &g[1][3]); // remember to put \n
		scanf("%c%c%c%c\n",  &g[2][0], &g[2][1], &g[2][2], &g[2][3]); // remember to put \n
		scanf("%c%c%c%c\n\n",&g[3][0], &g[3][1], &g[3][2], &g[3][3]); // remember to put \n
    // end input

    // processing
    // check if game ended
    bool gameEnded = true;
    rep(j,4) { rep (k, 4) { if ((g[j][0] == '.')) gameEnded = false; } }

    // Check each row
    bool XWon = false;
    bool OWon = false;
    rep(j,4) {
      // check each row for X
      if (
            ((g[j][0]=='X') || (g[j][0]=='T'))  
        &&  ((g[j][1]=='X') || (g[j][1]=='T'))
        &&  ((g[j][2]=='X') || (g[j][2]=='T'))
        &&  ((g[j][3]=='X') || (g[j][3]=='T'))
        ) { XWon = true; break; }

      // check each row for O
      if (
            ((g[j][0]=='O') || (g[j][0]=='T'))  
        &&  ((g[j][1]=='O') || (g[j][1]=='T'))
        &&  ((g[j][2]=='O') || (g[j][2]=='T'))
        &&  ((g[j][3]=='O') || (g[j][3]=='T'))
        ) { OWon = true; break; }

      // check each col for X
      if (
            ((g[0][j]=='X') || (g[0][j]=='T'))  
        &&  ((g[1][j]=='X') || (g[1][j]=='T'))
        &&  ((g[2][j]=='X') || (g[2][j]=='T'))
        &&  ((g[3][j]=='X') || (g[3][j]=='T'))
        ) { XWon = true; break; }

      // check each col for O
      if (
            ((g[0][j]=='O') || (g[0][j]=='T'))  
        &&  ((g[1][j]=='O') || (g[1][j]=='T'))
        &&  ((g[2][j]=='O') || (g[2][j]=='T'))
        &&  ((g[3][j]=='O') || (g[3][j]=='T'))
        ) { OWon = true; break; }

    }

    // if nobody has won check diagonals
    if ((!OWon) && (!XWon)) {
      // check diagonal for O
      if (
            ((g[0][0]=='O') || (g[0][0]=='T'))  
        &&  ((g[1][1]=='O') || (g[1][1]=='T'))
        &&  ((g[2][2]=='O') || (g[2][2]=='T'))
        &&  ((g[3][3]=='O') || (g[3][3]=='T'))
        ) { OWon = true; }
            
      if (
            ((g[0][3]=='O') || (g[0][3]=='T'))  
        &&  ((g[1][2]=='O') || (g[1][2]=='T'))
        &&  ((g[2][1]=='O') || (g[2][1]=='T'))
        &&  ((g[3][0]=='O') || (g[3][0]=='T'))
        ) { OWon = true; }

    }

    if ((!OWon) && (!XWon)) {
      // check diagonal for X
      if (
            ((g[0][0]=='X') || (g[0][0]=='T'))  
        &&  ((g[1][1]=='X') || (g[1][1]=='T'))
        &&  ((g[2][2]=='X') || (g[2][2]=='T'))
        &&  ((g[3][3]=='X') || (g[3][3]=='T'))
        ) { XWon = true; }
            
      if (
            ((g[0][3]=='X') || (g[0][3]=='T'))  
        &&  ((g[1][2]=='X') || (g[1][2]=='T'))
        &&  ((g[2][1]=='X') || (g[2][1]=='T'))
        &&  ((g[3][0]=='X') || (g[3][0]=='T'))
        ) { XWon = true; }
    }

    // output
    if (XWon) printf("Case #%d: X won\n", i + 1);
    else if (OWon) printf("Case #%d: O won\n", i + 1);
    else if (gameEnded) printf("Case #%d: Draw\n", i + 1);
    else printf("Case #%d: Game has not completed\n", i + 1);

	}

	return 0;
}
