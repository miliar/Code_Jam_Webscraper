#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORDQ(i,a,b) for (int i=(a);i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)
#define MP make_pair
#define F first
#define S second
#define PB push_back

using namespace std;

typedef long long LL;
const int MN = 53;
char T[MN][MN], TR[MN][MN];
int n,k;

bool check(int i, int j, char co) {
    if (j+k<=n) {
        bool res = true;
        FOR(x,0,k) {
            if (TR[i][j+x] != co) {
                res = false;
                break;
            }
        }
        if (res)
            return true;
    }
    if (i+k<=n) {
        bool res = true;
        FOR(x,0,k) {
            if (TR[i+x][j] != co) {
                res = false;
                break;
            }
        }
        if (res)
            return true;
    }
    if (i+k<=n && j+k<=n) {
        bool res = true;
        FOR(x,0,k) {
            if (TR[i+x][j+x] != co) {
                res = false;
                break;
            }
        }
        if (res)
            return true;
    }
    if (i-k+1>=0 && j+k<=n) {
        bool res = true;
        FOR(x,0,k) {
            if (TR[i-x][j+x] != co) {
                res = false;
                break;
            }
        }
        if (res)
            return true;
    }
    return false;
}

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(l,1,lw) {
        scanf("%d%d",&n,&k);
        FOR(i,0,n)
            scanf("%s",T[i]);
        FOR(i,0,n)
            FOR(j,0,n)
                TR[i][n-1-j] = T[j][i];

        FOR(j,0,n) {
            int le = n-1;
            FORD(i,n,0) {
                if (TR[i][j] != '.') {
                    while (le>i && TR[le][j] != '.')
                        le--;
                    if (TR[le][j] == '.') {
                        TR[le][j] = TR[i][j];
                        TR[i][j] = '.';
                    }
                }
            }
        }

        bool resR = false, resB = false;
        FOR(i,0,n) {
            FOR(j,0,n) {
                resR = resR || check(i,j,'R');
                resB = resB || check(i,j,'B');
            }
        }

        printf("Case #%d: ",l);
        if (resR && resB)
            printf("Both\n");
        if (resR && !resB)
            printf("Red\n");
        if (!resR && resB)
            printf("Blue\n");
        if (!resR && !resB)
            printf("Neither\n");
            
    }
    return 0;
}
