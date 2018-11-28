#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)
#define NSUMS 10

using namespace std;

char board[10][10];
int sums[20];
char outcomes[4][100] = {"X won","O won","Draw","Game has not completed"};

int hasVal(int r, int c, const char *s) {
    char t = board[r][c];
    for (const char *c=s; *c != '\0'; c++) if (*c == t) return 1;
    return 0;
}

int srow(int r, const char *s) {
    int sum=0;
    rep(c,4) sum += hasVal(r,c,s);
    return sum;
}

int scol(int c, const char *s) {
    int sum = 0;
    rep(r,4) sum += hasVal(r,c,s);
    return sum;
}

void csums(const char *s) {
    sums[8]=sums[9]=0;
    rep(i,4) {
        sums[i] = srow(i,s);
        sums[4+i] = scol(i,s);
        sums[8] += hasVal(i,i,s);
        sums[9] += hasVal(i,3-i,s);
    }
}

int cmpOutcome() {
    csums("XT");
    rep(i,NSUMS) if(sums[i]==4) return 0;
    csums("OT");
    rep(i,NSUMS) if(sums[i]==4) return 1;
    csums(".");
    rep(i,NSUMS) if(sums[i]>0) return 3;
    return 2;
}

int main() {
    int tc;
    cin >> tc;
    rep(i,tc) {
        rep(j,4) cin >> board[j];
        char *s = outcomes[cmpOutcome()];
        printf("Case #%d: %s\n",i+1,s);
    }
}
