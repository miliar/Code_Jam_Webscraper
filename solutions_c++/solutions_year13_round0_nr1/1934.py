#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;


int test_cases;
char *result, t[4][4];
bool is_board_full;


bool is_X(char h) { return (h=='X' || h=='T'); }
bool is_O(char h) { return (h=='O' || h=='T'); }

int check_4(char A, char B, char C, char D) {

	if(is_X(A) && is_X(B) && is_X(C) && is_X(D)) return 1;
	if(is_O(A) && is_O(B) && is_O(C) && is_O(D)) return 2;

	return 0;
}

void check() {

	int won = 0;

	// check rows
	won = max(won, check_4(t[0][0], t[0][1], t[0][2], t[0][3]));
	won = max(won, check_4(t[1][0], t[1][1], t[1][2], t[1][3]));
	won = max(won, check_4(t[2][0], t[2][1], t[2][2], t[2][3]));
	won = max(won, check_4(t[3][0], t[3][1], t[3][2], t[3][3]));

	// check cols
	won = max(won, check_4(t[0][0], t[1][0], t[2][0], t[3][0]));
	won = max(won, check_4(t[0][1], t[1][1], t[2][1], t[3][1]));
	won = max(won, check_4(t[0][2], t[1][2], t[2][2], t[3][2]));
	won = max(won, check_4(t[0][3], t[1][3], t[2][3], t[3][3]));

	// diag
	won = max(won, check_4(t[0][0], t[1][1], t[2][2], t[3][3]));
	won = max(won, check_4(t[0][3], t[1][2], t[2][1], t[3][0]));

	if(won == 1) {
		result = "X won";
	} else
	if(won == 2) {
		result = "O won";
	} else
	if(is_board_full) {
		result = "Draw";
	} else {
		result = "Game has not completed";
	}

	return;
}


int main() {

  scanf("%d", &test_cases);
  FOR(test_case, 1, test_cases) {

  	is_board_full = true;

    REP(i,4) REP(j,4) {
    	scanf(" %c", &t[i][j]);
    	if(t[i][j]=='.') {
			is_board_full = false;    		
    	}
    }

    check();

    printf("Case #%d: %s\n", test_case, result);
  }

  return 0;
}
