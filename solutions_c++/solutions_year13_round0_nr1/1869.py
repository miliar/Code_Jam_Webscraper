#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit atof atoi 
#include <cstdio>		// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>		// require fabs
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>		// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>		// require srand
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()
#define XWIN 1
#define OWIN 2
#define DRAW 3
#define GAME_NOT_COMPLETED 4

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int dr[] = { 1, 0, -1, 0 };
const int dc[] = { 0, 1,  0, -1 };

void output (int t, int res )
{
	printf ("Case #%d: ", t );
	switch (res ){
		case 1:
			printf ("O won\n" );
			break;
		case 2:
			printf ("X won\n" );
			break;
		case 3:
			printf ("Draw\n" );
			break;
		case 4:
			printf ("Game has not completed\n" );
			break;
	} // end switch
}

char board[4][4];
int b[4][4];
// 1: O win 2: X win 3: Draw 4: Game has not completed
int calc (void )
{
	memset (b, 0, sizeof (b ) );
	int cnt = 0;

	rep (i, 4 ) rep (j, 4 ){
		char c = board[i][j];
		switch (c ){
			case 'O': cnt++; b[i][j] = 1; break;
			case 'X': cnt++; b[i][j] = 2; break;
			case 'T': cnt++; b[i][j] = 3; break;
		} // end switch
	} // end rep

	int res = 0;

	rep (i, 4 ){
		res = DRAW;
		rep (j, 4 ){
			res &= b[i][j];
		} // end rep
		if (res == 1 || res == 2 ) return res;
	} // end rep

	
	rep (j, 4 ){
		res = DRAW;
		rep (i, 4 ){
			res &= b[i][j];
		} // end rep
		if (res == 1 || res == 2 ) return res;
	} // end rep

	res = DRAW;
	rep (t, 4 ){
		res &= b[t][t];
	} // end rep
	if (res == 1 || res == 2 ) return res;

	res = DRAW;
	rep (t, 4 ){
		res &= b[t][3-t];
	} // end rep
	if (res == 1 || res == 2 ) return res;

	if (cnt == 16 ) return DRAW;

	return GAME_NOT_COMPLETED;
}

int main()
{
	freopen ("A-large.in", "r", stdin );
//	freopen ("output.txt", "w", stdout );
	int n;
	scanf ("%d", &n );
	rep (t, n ){
		memset (board, 0, sizeof (board ) );
		rep (i, 4 ) rep (j, 4 ){
			scanf (" %c", &board[i][j] );
		} // end rep
		int res = calc ();
		output (t+1, res );
	} // end loop
		
	return 0;
}
