#include <iostream>
#include <cstdio>
using namespace std;

#define REP(x, n) for(int (x)=0; (x)<(n); ++(x))

#define INF 1000000000

char T[500][500];


int lewy, prawy, gora , dol;

int dist(int a, int b){
    if ( a < b ) swap(a, b);
    return a - b + 1;
}

inline int center(int R, int C, int k){
    int koszt = 0;
    for(int r = 110; r < 120 + 2 * k + 10; ++r)
    for(int c = 110; c < 120 + 2 * k + 10; ++c) if ( T[r][c] != '.' ) {
        int dr = r - R;
        int dc = c - C;
        int sr = R - dr;
        int sc = C - dc;
        if ( T[sr][sc] != '.' ) // { T[sr][sc] = T[r][c]; }
       // else
        if ( T[sr][sc] != T[r][c] ) return INF;
        
        sr = R + dr;
        sc = C - dc;
        
        if ( T[sr][sc] != '.' )// { T[sr][sc] = T[r][c]; }
       // else
        if ( T[sr][sc] != T[r][c] ) return INF;
        
        sr = R - dr;
        sc = C + dc;
        
        if ( T[sr][sc] != '.' ) //{ T[sr][sc] = T[r][c]; }
        //else
        if ( T[sr][sc] != T[r][c] ) return INF;
        
        koszt = max( koszt,  dist(r, R) + dist(c, C) - 1 );
    }

    //cout  << "OK ROZMIAR " << n << " R " << R << " C " << C << endl;
    
    return  koszt;
}


int testcase(){
    int voff = 120;
    int k; scanf("%d", &k);
    
    dol = 0;
    gora = INF;
    prawy = 0;
    lewy = INF;
    
    gora = voff + 1;
    
    REP(i, 500) REP(j, 500) T[i][j] = '.';
    for(int i=1; i<=k; ++i){
        int off = k - i + 120;
        REP(j, i) {
            int a; scanf("%d", &a);
            T[i + voff][2*j + off] = '0'+a;
            dol = i + voff;
            prawy = max( prawy, off + 2 * j );
        }
        lewy = min(lewy, off);
        
    }
    
    //lewy = 
    
    for(int i=k+1; i<2*k; ++i){
        int off = i - k + 120;
        REP(j, 2*k-i) {
            int a; scanf("%d", &a);
            T[i + voff][2*j + off] = '0'+a;
            dol = i + voff;
        }
    }
    
    //cout << "lpgd" << lewy << ' ' << prawy << " gora " << gora << " dol " << dol << endl;
    
    /*
    REP(i, 20) {
        REP(j, 20) cout << T[i][j]; cout << endl;
    }
    */
    
    int sol = INF;
    
    for(int r = 110; r < 120 + 2 * k + 10; ++r)
    for(int c = 110; c < 120 + 2 * k + 10; ++c){
        sol = min(sol, center(r, c, k));
        if ( sol == k ) break;
    }
    
    //cout << "intest " << center( 120, 122, k );
    
    //cout << "solution size " << sol << endl;
    
    return sol * sol - k * k;
}

int main(){
    int z; scanf("%d", &z);
    REP(i, z){
        cerr << "case " << i+1 << "/" << z << endl;
        printf("Case #%d: %d\n", i+1, testcase());
    }
}
