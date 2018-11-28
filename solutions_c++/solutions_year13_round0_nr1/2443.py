#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) (x).size()
#define MMS(x,n) memset(x,n,sizeof(x))
#define pb push_back
#define mp make_pair
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

char board[4][5];

bool check(char p)
{
    int i, j;
    bool t;
    REP(i,4)
    {
        t=1;
        REP(j,4)
        {
            if(board[i][j]=='T' && t) { t=0; continue; }
            if(board[i][j]!=p) break;
        }
        if(j==4) return 1;
    }
    REP(i,4)
    {
        t=1;
        REP(j,4)
        {
            if(board[j][i]=='T' && t) { t=0; continue; }
            if(board[j][i]!=p) break;
        }
        if(j==4) return 1;
    }
    t=1;
    REP(i,4)
    {
        if(board[i][i]=='T' && t) { t=0; continue; }
        if(board[i][i]!=p) break;
    }
    if(i==4) return 1;
    j=3, t=1;
    REP(i,4)
    {
        if(board[i][j]=='T' && t) { t=0; continue; }
        if(board[i][j]!=p) break;
        j--;
    }
    return i==4;
}

bool isempty()
{
    int i, j;
    REP(i,4) REP(j,4) if(board[i][j]=='.') return 1;
    return 0;
}

int main()
{
    READ("A-small-attempt0.in");
    WRITE("A-small-attempt0.out");
    int i, t, k;
    char won;
    scanf("%d",&t);
    rep(k,1,t+1)
    {
        won = '!';
        REP(i,4) scanf("%s",board[i]);
        if(check('X'))
            won = 'X';
        else if(check('O'))
            won = 'O';
        if(won!='!')
        {
            printf("Case #%d: %c won\n",k,won);
            continue;
        }
        if(isempty())
            printf("Case #%d: Game has not completed\n",k);
        else
            printf("Case #%d: Draw\n",k);
    }
    return 0;
}

