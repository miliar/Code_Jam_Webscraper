#include <cstdio>
#include <string.h>
#include <stack>
#include <vector>
#include <algorithm>

// box factory

#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

int N;
int M;

long long int a[100];
int A[100];
long long int b[100];
int B[100];

void readInput() {
   scanf("%d %d", &N, &M);
   for (int i=0; i<N; ++i) {
      scanf("%lld %d", &(a[i]), &(A[i]));
   }
   for (int i=0; i<M; ++i) {
      scanf("%lld %d", &(b[i]), &(B[i]));
   }
}

void readInputInv() {
   scanf("%d %d", &M, &N);
   for (int i=0; i<M; ++i) {
      scanf("%lld %d", &(b[i]), &(B[i]));
   }
   for (int i=0; i<N; ++i) {
      scanf("%lld %d", &(a[i]), &(A[i]));
   }
}

/*
typedef struct {
   long long int ap, bp, res; // a partially, b partially, current result
} CellLine;

vector<CellLine> D[101][101]; // dp table D[a_completely_comsumed][b..]
                              //              N                    M
*/

// at least one of {ap,bp} is 0
// ac,bc first not completely consumed
long long int solve(int ac, long long int ap, int bc, long long int bp) {
   long long int res = 0;
   long long int bp_saved = bp;
   if (ac==N || bc==M) return 0;
   // look for match to a in b
   for (int b2 = bc; b2<M; ++b2) if (B[b2]==A[ac]) {
      if (b2 > bc) bp = 0;
      long long int added;
      if (b[b2]-bp >= a[ac]-ap) { // a completely consumed
         added = a[ac]-ap;
         res = max(res, added + solve(ac+1, 0, b2, bp+added));
      } else { // b completely consumed
         added = b[b2]-bp;
         res = max(res, added + solve(ac, ap+added, b2+1, 0));
      }      
      break;
   }
   // skip this element in a
   res = max(res, solve(ac+1, 0, bc, bp_saved));
   return res;
}


long long int solve() {
   /*for (int i=0; i<=N; ++i) for (int j=0; j<=M; ++j) D[i][j].clear();
   
   for (int ac=1; ac<=N; ++ac) {
      for (int bc=1; bc<=M; ++bc) { //??
   */         
   return solve(0,0,0,0);
}



int main() {
   //printf("INV\n");
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: %lld\n", i, solve());
   }
   return 0;
}

