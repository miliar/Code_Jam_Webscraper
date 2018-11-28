#include <iostream>
#include <cstdio>

#include <map>
#include <queue>
#include <set>
#include <vector>
#include <string>

#include <cmath>
#include <algorithm>
#include <sstream>
#include <ctype.h>

#define FOR(i,a,b) for (int i=(a); i<(int)(b); i++)
#define FI(b)      FOR(i,0,b)
#define FJ(b)      FOR(j,0,b)
#define FK(b)      FOR(k,0,b)
#define FC(b)      FOR(c,0,b)
#define EACH(x,it) for(__typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

#define ZERO(x) memset((x),0,sizeof(x))
#define NEG(x) memset((x),-1,sizeof(x))

#define ASIZE(x) sizeof(x) / sizeof(x[0])

using namespace std;

int rown, coln;
int a[55][55];
int cnt[55][55];
int tgtr;
bool mines[55][55];

bool putmine(int r, int c) {
    bool succ = true;

    mines[r][c] = 1;
    FI(3) FJ(3) {
        int nr=r+i-1, nc=c+j-1;
        if(nr<0||nc<0||nr>=rown||nc>=coln) continue;
        cnt[nr][nc]++;
        if (cnt[nr][nc] > a[nr][nc]) succ = false;
    }

    return succ;
}

void takemine(int r, int c) {
    mines[r][c] = 0;
    FI(3) FJ(3) {
        int nr=r+i-1, nc=c+j-1;
        if(nr<0||nc<0||nr>=rown||nc>=coln) continue;
        cnt[nr][nc]--;
    }
}

int ans;

void go(int r, int c, int got) {
    if (r==rown) {
        bool good = true;
        FI(rown) FJ(coln) if (cnt[i][j]!=a[i][j]) good = false;
        if (good) ans >?= got;
        //FI(rown) { FJ(coln) cout << mines[i][j]; cout << endl; }
        //cout <<endl;
        return;
    }
    if (c==coln) { go(r+1,0,got); return; }

    if (putmine(r,c)) {
        go(r, c+1, r==tgtr ? got+1 : got);
    }

    takemine(r,c);
    go(r, c+1, got);
}

int main() {
   int cases;
   cin >> cases;

   FC(cases) {
       //cout << "CASE " << c << endl;
      cin >> rown >> coln;
      FI(rown) FJ(coln) cin >> a[i][j];
    
      tgtr = rown / 2;
      ZERO(cnt); ZERO(mines);
      ans=0; go(0,0,0);
      cout << "Case #" << c+1 <<": "<<ans<<endl;
   }
}
