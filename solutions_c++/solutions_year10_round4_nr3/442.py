
//Written by Alex Hamed Ahmadi (alex@hamedahmadi.com)

#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl
#define pb push_back

#define zer(x) memset(x,0,sizeof(x));
#define isin(x,s) (s.find(x)!=s.end())

typedef long long ll;
typedef vector <int> vi;
typedef set <int> si;
typedef pair <int, int> pii;

const int maxn=2200;
const int inf=200000000;

int a[maxn][maxn];
int dt[maxn][maxn][4];
int st[maxn][maxn][4];

int xs[maxn];
int ys[maxn];
int nx, ny;

int findx(int x) {
  return lower_bound(xs, xs+nx, x)-xs;
}

int findy(int y) {
  return lower_bound(ys, ys+ny, y)-ys;
}

struct Rect {
  int xlo, xhi, ylo, yhi;
  void clean() {
	if (xlo>xhi) swap(xlo, xhi);
	if (ylo>yhi) swap(ylo, yhi);
	xhi++; yhi++;
  }
} rect[maxn];

void clear() {

  nx=ny=0;


  zer(a);
  zer(dt);
  zer(st);
}


void solve(int cnum) {
  int r;
  cin>>r;
  FOR (i,r) {
	cin>>rect[i].xlo>>rect[i].ylo>>rect[i].xhi>>rect[i].yhi;
	rect[i].clean();
	xs[nx++]=rect[i].xlo;
	xs[nx++]=rect[i].xhi;
	ys[ny++]=rect[i].ylo;
	ys[ny++]=rect[i].yhi;
  }

  xs[nx++]=-10;
  xs[nx++]=10000000;
  ys[ny++]=-10;
  ys[ny++]=10000000;

  sort(xs, xs+nx);
  nx=unique(xs, xs+nx)-xs;

  sort(ys, ys+ny);
  ny=unique(ys, ys+ny)-ys;

  FOR(i,r) {
	int xlo=findx(rect[i].xlo);
	int ylo=findy(rect[i].ylo);
	int xhi=findx(rect[i].xhi);
	int yhi=findx(rect[i].yhi);
	for (int x=xlo;x<xhi;x++)
	  for (int y=ylo;y<yhi;y++)
		a[x][y]=1;
  }

  int maxdt=0;
  for (int x=1;x<nx;x++)
	for (int y=1;y<ny;y++) {
	  int here=0;

	  int w=ys[y+1]-ys[y];
	  int h=xs[x+1]-xs[x];
	  if (a[x][y]) {
		for (int k=0;k<4;k++) st[x][y][k]=0;
		if () 
		  dt[x][y][0]=max(dt[x-1][y][2], dt[x][y-1][1])+1; //TODO: shift???
		else d[x][y][0]=1;
		dt[x][y][1]=dt[x][y][0]+w-1;
		dt[x][y][2]=dt[x][y][0]+h-1;
		dt[x][y][3]=min(dt[x][y][1]+h-1, dt[x][y][2]+w-1);
				
		here=dt[x][y][3];
	  } else {
		
	  }

	  maxdt=max(maxdt, here);
	}

  cout<<"Case #"<<cnum<<": "<<maxdt<<endl;

}

int main() {
  int nt;
  cin>>nt;
  for (int cnum=1; cnum<=nt; cnum++) {
	clear();
	solve(cnum);
  }
  return 0;
}
