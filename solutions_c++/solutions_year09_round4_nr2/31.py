#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
typedef long double ld;

int cas=0;
int R,C,F;
char grid[64][64];
bool mark[64][64][64];
vector<pair<int, pair<int,int> > > qs[51];
bool issupp(int r, int c) {
  return r==R-1 || grid[r+1][c]=='#';
}
int getheight(int r, int c) {
  int h = 1;
  while (!issupp(r+h-1,c)) ++h;
  return h;
}
void doit() {
  scanf("%d%d%d",&R,&C,&F);
  FOR(r,R) scanf("%s",grid[r]);

  FOR(i,51) qs[i].clear();

  CLR(mark,0);
  int ans = -1;
  qs[0].PB(MP(0,MP(0,1)));
  int t = 0, lastt = 0;
  while (t <= lastt+50) {
    while (qs[t%51].size()) {
      lastt = t;

      int r = qs[t%51].back().A;
      int cl = qs[t%51].back().B.A;
      int cr = qs[t%51].back().B.B;
      qs[t%51].pop_back();
      assert(r<R);

      if (mark[r][cl][cr]) continue;
      mark[r][cl][cr] = 1;

      if (r==R-1) {
	ans = t;
	goto xx;
      }

      while (cl>0 && grid[r][cl-1]=='.' && issupp(r,cl)) --cl;
      while (cr<C && grid[r][cr]=='.' && issupp(r,cr-1)) ++cr;

      //printf("~~ %d [%d,%d)\n",r,cl,cr);

      if (cl+1==cr) continue;

      // dig from r2l
      FR(cl2,cl+1,cr) if (grid[r+1][cl2-1]=='#') {
	FR(cr2,cl2+1,cr+1) {
	  if (grid[r+1][cr2-1]=='.') break;
	  int tpm = (t+(cr2-cl2))%51;

	  if (issupp(r+1,cl2)) {
	    qs[tpm].PB(MP(r+1,MP(cl2,cr2)));
	  } else {
	    int h = getheight(r+1,cl2);
	    if (h <= F) {
	      qs[tpm].PB(MP(r+h,MP(cl2,cl2+1)));
	    }
	  }
	}
      }

      // dig from l2r
      FR(cr2,cl+1,cr) if (grid[r+1][cr2]=='#') {
	RF(cl2,cr2,cl) {
	  //printf(" !! [%d,%d)\n",cl2,cr2);
	  if (grid[r+1][cl2]=='.') break;
	  int tpm = (t+(cr2-cl2))%51;

	  if (issupp(r+1,cr2-1)) {
	    qs[tpm].PB(MP(r+1,MP(cl2,cr2)));
	  } else {
	    int h = getheight(r+1,cr2-1);
	    if (h <= F) {
	      qs[tpm].PB(MP(r+h,MP(cr2-1,cr2)));
	    }
	  }
	}
      }

      // walk off left
      if (!issupp(r,cl)) {
	//printf(" ?? can walk off left\n");
	int h = getheight(r+1,cl);
	assert(r+h<R);

	if (h <= F) {
	  int tpm = t%51;
	  qs[tpm].PB(MP(r+h,MP(cl,cl+1)));
	}
      }

      // walk off right
      if (!issupp(r,cr-1)) {
	//printf(" ?? can walk off right\n");
	int h = getheight(r+1,cr-1);

	if (h <= F) {
	  int tpm = t%51;
	  qs[tpm].PB(MP(r+h,MP(cr-1,cr)));
	}
      }
    }
    ++t;
  }
  xx:;

  printf("Case #%d: ",++cas);
  if (ans == -1) printf("No");
  else printf("Yes %d",ans);
  printf("\n");
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}
