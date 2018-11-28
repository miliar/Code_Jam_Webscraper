#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <string>

#define FOREACH( i, C ) for( __typeof(C.begin())i = C.begin(); i != C.end(); ++i )
#define CLEAR( V )      memset( V, 0, sizeof(V) )

#define MAX 10009

using namespace std;

int H, W;
char A;
int T;

struct S {
       char a;
       int val;
       bool was;       
};

struct S M[101][101];

void prnt() {
     for (int i = 0; i < H; ++i) {
            printf("%c", M[i][0].a);
            for (int j = 1; j < W; ++j) {
              printf(" %c", M[i][j].a);           
            }
            printf("\n");
        }
}


char  solve(int r, int c) {
      
     if ( M[r][c].was ) return M[r][c].a;
     
     M[r][c].was = true;
     
     int nextr = r, nextc = c;
     
     int n  = MAX;     
     if ( (r-1 >= 0)) n = M[r-1][c].val;
     
     int s = MAX;
     if (r+1 <= H-1) s = M[r+1][c].val;
     
     int w = MAX;
     if (c-1 >= 0) w = M[r][c-1].val;
     
     int e = MAX;
     if (c+1 <= W-1) e = M[r][c+1].val;
     
     if (M[nextr][nextc].val > n) {nextr = r-1; nextc = c;}
     if (M[nextr][nextc].val > w) {nextr = r; nextc = c-1;}
     if (M[nextr][nextc].val > e) {nextr = r; nextc = c+1;}
     if (M[nextr][nextc].val > s) {nextr = r+1; nextc = c;}
     
     if ((nextr == r) && (nextc == c) ) 
     { M[r][c].a = A; 
       ++A; 
     }
     else 
          M[r][c].a = solve(nextr, nextc);
          
     return M[r][c].a;
}

int d ;
int main() {
    scanf("%d", &T);
    for (int no = 1; no <= T; ++no) {
        A = 'a';
        scanf("%d %d", &H, &W);
        for (int i = 0; i< H; ++i) {
            for (int j = 0; j < W; ++j) {
                         
                scanf("%d", &d);
                M[i][j].a = A;
                M[i][j].val = d;
                M[i][j].was = false; 
            }
        }

        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                solve(i, j);
            }
        }
        
        
        printf("Case #%d:\n", no);
        prnt();
    }
    return 0;
}

