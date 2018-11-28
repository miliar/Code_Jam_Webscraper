#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 101
#define INF 100000

int A[MAXN][MAXN];
int M[MAXN][MAXN];

int da[] = {-1, 0, 0, 1};
int db[] = {0, -1, 1, 0};

int freeid = 0;
int h, w;

char rm[MAXN*MAXN];

inline bool isLegal(int a, int b){
    if (a < 0 || b < 0) return false;
    if (a >= h || b >= w) return false;
    return true;
}

inline void isSink(int a, int b){
    for(int i=0; i<4; ++i) if ( isLegal(a+da[i], b+db[i]) )
        if (A[a][b] > A[a+da[i]][b+db[i]]) return;
    M[a][b] = freeid++;
}

inline bool proc(int a, int b){
    int lowest = INF;
    if ( M[a][b] >= 0 ) return false;
    for(int i=0; i<4; ++i) if ( isLegal(a+da[i], b+db[i]) )
        lowest = min(lowest, A[a+da[i]][b+db[i]]);
    
    for(int i=0; i<4; ++i) if ( isLegal(a+da[i], b+db[i]) ) {
        if( lowest == A[a+da[i]][b+db[i]] ) {
            if (M[a+da[i]][b+db[i]] < 0) return false;
            M[a][b] = M[a+da[i]][b+db[i]];
            return true;
        }
    }
}

void remap(){
    for(int i=0; i<freeid; ++i) rm[i] = ' ';
    char lit = 'a';
    for(int i=0; i<h; ++i) {
        for(int j=0; j<w; ++j) {
            if (rm[M[i][j]] == ' ') rm[M[i][j]] = lit++;
            printf("%c ", rm[M[i][j]]);
        }
        printf("\n");
    }
}

void testcase(){
    scanf("%d%d", &h, &w);

    for(int i=0; i<h; ++i){
        for (int j=0; j<w; ++j) {
            scanf("%d", &A[i][j]);
            M[i][j] = -1;
        }
    }
    
    // cout << "read" << endl;
    
    freeid = 0;
    for(int i=0; i<h; ++i) for(int j=0; j<w; ++j) isSink(i, j);
    
    while(true){
        bool done = true;
        for(int i=0; i<h; ++i) for(int j=0; j<w; ++j) {
            if ( proc(i, j) ) done = false;
        }
        if (done) break;
    }
    
    remap();
}

int main(){
int t; scanf("%d", &t);
for (int i=1; i<=t; ++i) {
    printf("Case #%d:\n", i);
    testcase();
}
return 0;
}

