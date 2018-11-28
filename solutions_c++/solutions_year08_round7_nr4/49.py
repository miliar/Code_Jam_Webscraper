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

using namespace std;

#define FOR(i,a,b)  for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cout << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

/*
struct state    {
    vector<int> st;
    int pi, pj; //pos of king
};
*/

int R, C;

int memo[1<<16][4][4];
bool burn[16][16];

int ADDR(int i, int j)   {
    return i * C + j;
}

/*
int STATE(int board, int i, int j)  {
    int st = 0;
    st |= board;
    st |= j<<(R*C);
    st |= i<<(R*C + 2);
    return st;
}
*/

//board, king at i, j
int go(int board, int i, int j)    {
    if (board == (1<<(R*C))-1)  return memo[board][i][j] = 0;
    //int check = STATE(board, i, j);
    if (memo[board][i][j] != -1)  return memo[board][i][j];

    int win = 0;

    FOR (di, -1, 2) {
        FOR (dj, -1, 2) if (!(di == 0 && dj == 0))   {
            int ni = i + di, nj = j + dj;
            if (!(ni >= 0 && ni < R && nj >= 0 && nj < C)) continue;
            if (burn[ni][nj])   continue;
            //been there before
            if ((board & (1<<ADDR(ni,nj))) != 0)    continue;
            //move from i, j to ni, nj
            int nboard = board;//board ^ (1<<ADDR(i,j));
            nboard |= (1<<ADDR(ni,nj));
            /*
            dbg(board);
            dbg(i);
            dbg(j);

            dbg(nboard);
            dbg(ni);
            dbg(nj);
            */
            int ret = go(nboard, ni, nj);
            if (ret == 0)   {
                win = 1;
            }
        }
    }
    
    return memo[board][i][j] = win;
}

int main(void)  {
    int numTests;
    cin >> numTests;
    FOR (nc, 1, numTests+1) {
        cin >> R >> C;

        memset(memo, 255, sizeof memo);

        memset(burn, 0, sizeof burn);

        int si = -1, sj = -1, board = 0;
        FOR (i, 0, R)   {
            string s;
            cin >> s;
            assert(s.size() == C);
            FOR (j, 0, C)   {
                if (s[j] == 'K')    {
                    si = i;
                    sj = j;
                }
                else if (s[j] == '#')   {
                    burn[i][j] = true;
                    board |= (1<<ADDR(i,j));
                }
            }
        }
        board |= (1<<ADDR(si, sj));
        
        //cout << si << " " << sj << endl;

        int win = go(board, si, sj);
        
        //dbg(win);

        cout << "Case #" << nc << ": " << ((win == 1) ? "A" : "B") << endl;
    }
    
    
}
