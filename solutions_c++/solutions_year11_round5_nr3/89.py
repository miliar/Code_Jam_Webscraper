#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=100;
int _,h,w,A[N*N],B[N*N],ile[N*N];
char b[N][N];

int c(int y, int x) { return (x+w)%w*h + (y+h)%h; }

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d%d",&h,&w);
      REP(i,h) REP(j,w) scanf(" %c",&b[i][j]);
      REP(i,h) REP(j,w)
	 if (b[i][j]=='-') A[c(i,j)] = c(i,j-1), B[c(i,j)] = c(i,j+1);
	 else if (b[i][j]=='|') A[c(i,j)] = c(i-1,j), B[c(i,j)] = c(i+1,j);
	 else if (b[i][j]=='/') A[c(i,j)] = c(i-1,j+1), B[c(i,j)] = c(i+1,j-1);
	 else if (b[i][j]=='\\') A[c(i,j)] = c(i-1,j-1), B[c(i,j)] = c(i+1,j+1);
      int ans = 0;
      REP(mask,1<<(h*w)) {
	 int ok=1;
	 REP(i,h*w) ile[i]=0;
	 REP(i,h*w) if (mask&1<<i) ile[A[i]]++; else ile[B[i]]++;
	 REP(i,h*w) if (ile[i]!=1) ok=0;
	 if (ok) ++ans;
      }

      printf("Case #%d: %d\n",test+1, ans % 1000003);
   }
}
