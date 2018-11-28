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
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

char strs[4][5];
int numx, numo, nume, numt;
bool winx, wino, empty;
void check(int i, int j) {
    char tc = strs[i][j];
    if (tc == 'X') {
        numx++;
    } else if (tc == 'O') {
        numo++;
    } else if (tc == '.') {
        nume++;
    } else if (tc == 'T') {
        numt++;
    }
}
void check2() {
    if (numx + numt == 4) {
        winx = true;
    } else if (numo + numt == 4) {
        wino = true;
    }
    if (nume != 0) {
        empty = true;
    }
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        winx = false, wino = false, empty = false;
        for (int i = 0; i < 4; i++) {
            scanf("%s", strs[i]);
        }
        for (int i = 0; i < 4; i++) {
            numx = 0, numo = 0, nume = 0, numt = 0;
            for (int j = 0; j < 4; j++) {
                check(i, j);
            }
            check2();
        }
        for (int j = 0; j < 4; j++) {
            numx = 0, numo = 0, nume = 0, numt = 0;
            for (int i = 0; i < 4; i++) {
                check(i, j);
            }
            check2();
        }
        //diagonal
        numx = 0, numo = 0, nume = 0, numt = 0;
        for (int i = 0; i < 4; i++) {
            check(i, i);
        }
        check2();

        numx = 0, numo = 0, nume = 0, numt = 0;
        for (int i = 0; i < 4; i++) {
            check(i, 3 - i);
        }
        check2();

        printf("Case #%d: ", casenum++);
        if (winx) {
            printf("%s\n", "X won" );
        } else if (wino) {
            printf("%s\n", "O won" );
        } else if (empty) {
            puts("Game has not completed");
        } else  {
            puts("Draw");
        }
    }
	return 0;
}

