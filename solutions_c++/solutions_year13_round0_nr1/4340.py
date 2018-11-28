/* Michał Adamczyk, majkello */
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<set>
#include<map>
#include<utility>
#include<ext/numeric>
#include<tr1/unordered_map>
#include<string>

using namespace std;
using namespace std::tr1;
using namespace __gnu_cxx;

#define REP(i,n) for(int i=0;i<(n);++i)
#define PER(i,n) for(int i=(n)-1;i>=0;--i)
#define FORU(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define ALL(X) (X).begin(),(X).end()
#define SIZE(X) (int)(X).size()
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

LL nwd(LL a,LL b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }

const int INF = 1000000007;
const int MX = 1000*1000+7;

char M[4][5];

bool checkRow(int k, char P) {
    REP(i,4) if(M[k][i] != P && M[k][i] != 'T') return false;
    return true;
}
bool checkCol(int k, char P) {
    REP(i,4) if(M[i][k] != P && M[i][k] != 'T') return false;
    return true;
}

bool checkX1(char P) {
    REP(i,4) if(M[i][i] != P && M[i][i] != 'T') return false;
    return true;
}

bool checkX2(char P) {
    REP(i,4) if(M[3-i][i] != P && M[3-i][i] != 'T') return false;
    return true;
}


bool hasWon(char P) {
    bool won = false;
    REP(i,4) won |= checkRow(i, P) || checkCol(i, P);
    won |= checkX1(P) || checkX2(P);
    return won;
}

bool isFF() {
    REP(i,4)REP(j,4) if(M[i][j] == '.') return false;
    return true;
}

void solve(int testCase) {
    REP(i,4) scanf("%s",M[i]);
    string res;

    if(hasWon('X')) res = "X won";
    else if(hasWon('O')) res = "O won";
    else if (isFF()) res = "Draw";
    else res = "Game has not completed";

    printf("Case #%d: %s\n", testCase, res.c_str());
}

int main() {
    int _T;
    scanf("%d",&_T);
    REP(i,_T) solve(i+1);
    return 0;
}

