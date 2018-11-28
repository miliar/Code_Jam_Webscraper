#include<map>
#include<set>
#include<list>
#include<cmath>
#include<ctime>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

// Template Begin(By yayamao)
#ifndef ONLINE_JUDGE
	#define READ freopen("A-large.in", "r", stdin)
	#define WRITE freopen("A-large.out", "w", stdout)
#else
	#define READ
	#define WRITE
#endif

#ifdef _MSC_VER
	#define int64 __int64
	#define uint64 unsigned __int64
#else
	#define int64 long long
	#define uint64 unsigned long long
#endif

#define S(x) ((int)x.size())
#define L(x) ((int)x.length())

#define X first
#define Y second
#define MII map<int, int>
#define MSI map<string, int>
#define MIS map<int, string>
#define PII pair<int, int>
#define PSI pair<string, int>
#define PIS pair<int, string>
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)

#define TWO(x)			(1 << (x))
#define TWOL(x)			(1LL << (x))
#define LOWER_BIT(x)	((x) & (-(x)))
#define CONTAIN(s,x)	(((s) & TWO(x)) != 0)
#define CONTAINL(s,x)	(((s) & TWOL(x)) != 0)

template<class T>inline void checkMax(T &a,const T &b){if(a < b) a = b;}
template<class T>inline void checkMin(T &a,const T &b){if(b < a) a = b;}
template<class T>inline string toString(const T &n){ostringstream out; out << n; out.flush(); return out.str();}
template<class T>inline T toValue(const string &s){T x; istringstream in(s); in >> x; return x;}
bool hasNext(){char c;if(scanf(" %c",&c)==EOF) return false; ungetc(c, stdin); return true;}

const double EPS  = 1E-8;
const double D_INF = 1E99;
const int I_INF = 0x7FFFFFFF;
const int64 L_INF = 0x7FFFFFFFFFFFFFFFLL;

int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};
string dir[]={"L", "R", "U", "D", "LU", "LD", "RU", "RD"};

int tenPower[10]={0x1,0xA,0x64,0x3E8,0x2710,0x186A0,0xF4240,0x989680,0x5F5E100,0x3B9ACA00};

// [l, r]
#define range(i, l, r) for(int i = (l); i <= (int)(r); ++i)
#define rangeD(i, r, l) for(int i = (r); i >= (int)(l); --i)

// [0, n)
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)
#define repD(i, n) for(int i = (int)(n) - 1; i >= 0; --i)

// [begin, end)
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define setv(a, v) memset(a, v, sizeof(a))
#define all(c) (c).begin(), (c).end()
// Template Ended(By yayamao)

void preProcess() {
}

const int N = 4;
char cell[N][N];

bool isWiner(char player) {
    // Row
    rep (i, N) {
        bool ok = true;
        rep (j, N) {
            if (cell[i][j] != player && cell[i][j] != 'T') {
                ok = false;
                break;
            }
        }
        if (ok) {
            return true;
        }
    }

    // Column
    rep (j, N) {
        bool ok = true;
        rep (i, N) {
            if (cell[i][j] != player && cell[i][j] != 'T') {
                ok = false;
                break;
            }
        }
        if (ok) {
            return true;
        }
    }

    // Diagonal
    for (int step = -1; step <= 1; step += 2) {
        int j = (step == -1 ? N - 1 : 0);
        bool ok = true;
        rep (i, N) {
            if (cell[i][j + step * i] != player && cell[i][j + step * i] != 'T') {
                ok = false;
                break;
            }
        }
        if (ok) {
            return true;
        }
    }

    return false;
}

bool hasCell(char target) {
    rep (i, N) {
        rep (j, N) {
            if (cell[i][j] == target) {
                return true;
            }
        }
    }
    return false;
}

string solve() {
    bool xWin = isWiner('X');
    bool oWin = isWiner('O');
    bool isFinished = !hasCell('.');

    if (xWin && !oWin) {
        return "X won";
    } else if (oWin && !xWin) {
        return "O won";
    } else if (isFinished) {
        return "Draw";
    } else {
        return "Game has not completed";
    }
}

void run(const int &caseID) {
    rep (i, 4) {
        rep (j, 4) {
            cin >> cell[i][j];
        }
    }
    cout << "Case #" << caseID << ": ";
    cout << solve();
    cout << endl;
}

void runWithCaseT() {
    int caseT;
    scanf("%d", &caseT);
    getchar();
    for(int caseID = 1; caseID <= caseT; ++caseID) {
        run(caseID);
    }
}

void runWithoutCaseT() {
    int caseID = 0;
    while(hasNext()) {
        run(++caseID);
    }
}

int main(int argc, char *argv[]) {
    srand(time(NULL));

    READ;
    WRITE;

    preProcess();

    runWithCaseT();
    //runWithoutCaseT();

    return (EXIT_SUCCESS);
}

