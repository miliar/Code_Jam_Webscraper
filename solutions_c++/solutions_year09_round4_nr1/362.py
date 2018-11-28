#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_N = 50;
int n;
char data[MAX_N][MAX_N];
int d[MAX_N];

void fun(int cs) {
    scanf("%d", &n);
    REP(i, n) REP(j, n) scanf(" %c", &data[i][j]);
    REP(i, n) {
        int w = 0;
        for ( int j = n-1; j >= 0; j--)  {
            if ( data[i][j] == '0' )
                w++;
            else
                break;
        }
        d[i] = w;
    }

//    REP(i, n) printf("%d ", d[i]); printf("\n");

    int res = 0;
    REP(i, n) {
        int mam = -1;
        FOR(j, i, n) {
            if ( d[j] >= n-1-i ) {
                mam = j;
                break;
            }
        }

        assert(mam != -1);

        while ( mam != i ) {
            swap(d[mam], d[mam-1]);
            mam--;
            res++;
        }    
    }

    printf("Case #%d: %d\n", cs, res);
}

int main() {
    int T;
    scanf("%d", &T);

    REP(i, T) fun(i+1);

    return 0;
}
