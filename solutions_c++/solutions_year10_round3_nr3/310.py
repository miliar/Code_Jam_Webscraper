#include<cstdio>
#include<algorithm>
#include<utility>

using namespace std;

char fld[512][2048];
int dp[512][2048];
int dpx[512][2048], dpy[512][2048];
pair<int, pair<int, int> > sq[512*2048];
int sol[1024];

bool cmp(const pair<int, pair<int, int> >& a, const pair<int, pair<int, int> >& b)
{
  return a.first != b.first ? a.first < b.first : a.second > b.second;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    int M, N;
    scanf("%d%d", &M, &N);
    for(int i=0; i<M; ++i) {
      char s[1024];
      scanf("%s", s);
      for(int j=0; j<N/4; ++j) {
	int k = '0' <= s[j] && s[j] <= '9' ? s[j] - '0' : s[j] - 'A' + 10;
	fld[i][4*j] = !!(k & 8);
	fld[i][4*j+1] = !!(k & 4);
	fld[i][4*j+2] = !!(k & 2);
	fld[i][4*j+3] = !!(k & 1);
      }
    }
    //for(int i=0; i<M; ++i,puts(""))
    //  for(int j=0; j<N; ++j)
    	//putchar(".*"[fld[i][j]]);
    for(int i=0; i<M; ++i) {
      dpx[i][0] = 1;
      for(int j=1; j<N; ++j) {
	dpx[i][j] = 1;
	if(fld[i][j-1] != fld[i][j])
	  dpx[i][j] = dpx[i][j-1]+1;
      }
    }
    for(int j=0; j<N; ++j) {
      dpy[0][j] = 1;
      for(int i=1; i<M; ++i) {
	dpy[i][j] = 1;
	if(fld[i-1][j] != fld[i][j])
	  dpy[i][j] = dpy[i-1][j]+1;
      }
    }
    //for(int i=0; i<M; ++i,puts(""))
    //  for(int j=0; j<N; ++j)
    //	printf("%d",dpx[i][j]);
    //for(int i=0; i<M; ++i,puts(""))
    //  for(int j=0; j<N; ++j)
    //	printf("%d",dpy[i][j]);
    int picked = 0;
    for(int i=0; i<1024; ++i)
      sol[i] = 0;
    while(picked < M*N) {
      int maxk = 1;
      for(int i=0; i<M; ++i) {
	dpx[i][0] = fld[i][0]>1?0:1;
	for(int j=1; j<N; ++j) {
	  if(fld[i][j] > 1) {
	    dpx[i][j] = 0;
	    continue;
	  }
	  dpx[i][j] = 1;
	  if(fld[i][j-1] != fld[i][j])
	    dpx[i][j] = dpx[i][j-1]+1;
	}
      }
      for(int j=0; j<N; ++j) {
	dpy[0][j] = fld[0][j]>1 ? 0 : 1;
	for(int i=1; i<M; ++i) {
	  if(fld[i][j] > 1) {
	    dpy[i][j] = 0;
	    continue;
	  }
	  dpy[i][j] = 1;
	  if(fld[i-1][j] != fld[i][j])
	    dpy[i][j] = dpy[i-1][j]+1;
	}
      }
      for(int i=0; i<M; ++i)
	dp[i][0] = fld[i][0]>1 ? 0 : 1;
      for(int j=0; j<N; ++j)
	dp[0][j] = fld[0][j]>1 ? 0 : 1;
      for(int i=1; i<M; ++i) {
	for(int j=1; j<N; ++j) {
	  if(fld[i][j] > 1) {
	    dp[i][j] = 0;
	    continue;
	  }
	  dp[i][j] = 1;
	  if(fld[i][j] == fld[i-1][j-1]) {
	    dp[i][j] = max(dp[i][j], 1+min(dp[i-1][j-1], min(dpx[i][j]-1, dpy[i][j]-1)));
	  }
	  if(maxk<dp[i][j])maxk=dp[i][j];
	}
      }
      //for(int i=0; i<M; ++i,puts(""))
      //	for(int j=0; j<N; ++j)
      //	  printf("%d",dp[i][j]);
      if(maxk == 1) break;
      for(int i=0; i<M; ++i) {
	for(int j=0; j<N; ++j) {
	  if(dp[i][j] == maxk) {
	    for(int y=i-maxk+1; y<=i; ++y)
	      for(int x=j-maxk+1; x<=j; ++x)
		fld[y][x] = 100;
	    picked += maxk*maxk;
	    sol[maxk]++;
	    goto next;
	  }
	}
      }
    next:;
    }
    sol[1] = M * N - picked;
    int types = 0;
    for(int i=0; i<1024; ++i)
      if(sol[i]) types++;
    printf("Case #%d: %d\n", C, types);
    for(int i=1023; i>=0; --i)
      if(sol[i])
	printf("%d %d\n", i, sol[i]);
    fprintf(stderr, "%d ", C);
  }
  return 0;
}
