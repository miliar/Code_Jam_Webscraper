#include <iostream>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;

#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ALL(s) s.begin(),s.end()
#define SZ(s) signed(s.size())
#define MP make_pair
typedef pair<int,int> PII;
typedef pair<int,char> PIC;
const int INF = 2000000000;

#define D(A)

int main() {
  int ncases; scanf("%d", &ncases);
  FOR(casenum,ncases) {
    int P, Q; scanf("%d %d",&P, &Q);
    int p[Q+2]; p[0]=0; FOR(i,Q) scanf("%d",&p[i+1]); p[Q+1]=P+1;
    int b[Q+2][Q+2];
    FCO(l,1, Q+2) FOR(i,Q+2-l) { //i+l < Q+2 <=> i<Q+2-l
      int j = i+l;
      D(fprintf(stderr, "b[%d][%d]: \n", i,j););
      if(j==i+1) {
        b[i][j] = 0;
        D(fprintf(stderr, "\t b[%d][%d]=%d\n", i,j, b[i][j]););
        continue;
      }
      b[i][j] = max(0, p[j]-p[i]-2);
      int m = INF;
      FCO(k,i+1,j) {
        m = min(m, b[i][k]+b[k][j]);
        D(fprintf(stderr, "\t b[%d][%d]+b[%d][%d]=%d (now %d)\n", i,k, k, j, b[i][k]+b[k][j], m););
      }
      b[i][j] += m;
      D(fprintf(stderr, "b[%d][%d]=%d\n", i,j, b[i][j]););
    }
    printf("Case #%d: %d\n", casenum+1, b[0][Q+1]);
  }
  return 0;
}
