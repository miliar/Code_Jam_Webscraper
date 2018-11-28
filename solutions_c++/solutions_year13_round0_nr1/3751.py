#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;
const int inf = int(1e9)+7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

char mp[4][4];

bool check(char ch) {
    FOR(i,4) {
        bool flag = true;
        FOR(j,4) if (mp[i][j] != ch && mp[i][j] != 'T') flag = false;
        if (flag) return true;
    }
    FOR(j,4) {
        bool flag = true;
        FOR(i,4) if (mp[i][j] != ch && mp[i][j] != 'T') flag = false;
        if (flag) return true;
    }
    
    {
        bool flag = true;
        FOR(i,4) {
            int j = i;
            if (mp[i][j] != ch && mp[i][j] != 'T') flag = false;
        }
        if (flag) return true;
    }
    
    
    {
        bool flag = true;
        FOR(i,4) {
            int j = 4-i-1;
            if (mp[i][j] != ch && mp[i][j] != 'T') flag = false;
        }
        if (flag) return true;
    }
    
    
    return false;
}
bool isFull() {
    FOR(i,4) FOR(j,4) if (mp[i][j] == '.') return false;
    return true;
}

int main() {
    int caseNum;
    scanf("%d", &caseNum);
    FOR(rp,caseNum) {
        FOR(i,4) scanf("%s", mp[i]);
        printf("Case #%d: ", rp+1);
        if (check('X')) printf("X won\n"); else
        if (check('O')) printf("O won\n"); else
        if (isFull()) printf("Draw\n"); else
            printf("Game has not completed\n");
    }
    return 0;
}

