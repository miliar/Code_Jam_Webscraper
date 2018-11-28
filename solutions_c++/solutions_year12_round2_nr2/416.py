#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

const int infty = 10000000;

int H; // initial water level 
int N; // height (y)
int M; // witdh  (x)

int a[100][100]; // floor 
int b[100][100]; // ceil
int t[100][100]; // time_to_reach (Decimi di sec.)

int x,y;

int time_move(int x,int y, int xx, int yy, int t) {
  int h = H - t;
  int qa = a[x][y];
  int qb = b[x][y];
  int qaa = a[xx][yy];
  int qbb = b[xx][yy];
  if (qbb - qa < 50) return infty;
  if (qbb - qaa < 50) return infty;
  if (qb -  qaa < 50) return infty;

  int td = (h+50 - qbb);
  if (td<0) td=0; // decimi di secondo per passare
  float hh = h-td;
  //  if (-qbb + h + 50 > 0) return infty;
  if (t==0 && td ==0) return 0;
  if (hh - qa >= 20) return 10+td;
  return 100+td;
}

void reset() {
  for (int x=0;x<M;++x)
    for (int y=0;y<N;++y)
      t[x][y]=infty;
  t[0][0]=0;
}

void print(int t[100][100]) {
  cerr<<endl;
  for (int y=0;y<N;++y) {
    for (int x=0;x<M;++x)
      cerr<< t[x][y]<<" ";
    cerr<<"."<<endl;
  }
}

bool compute(int x, int y) {
  bool changed = false;
  int qt = t[x][y];
  if (qt == infty) return false;
  int tt;
  if (x>0) {
    tt = time_move(x,y,x-1,y,qt);
    tt += qt;
    if (tt < t[x-1][y]) {
      t[x-1][y]=tt;
      changed=true;
    }
  }
  if (x<M-1) {
    tt = time_move(x,y,x+1,y,qt);
    tt += qt;
    if (tt < t[x+1][y]) {
      t[x+1][y]=tt;
      changed=true;
    }
  }
  if (y>0) {
    tt = time_move(x,y,x,y-1,qt);
    tt += qt;
    if (tt < t[x][y-1]) {
      t[x][y-1]=tt;
      changed=true;
    }
  }
  if (y<N-1) {
    tt = time_move(x,y,x,y+1,qt);
    tt += qt;
    if (tt < t[x][y+1]) {
      t[x][y+1]=tt;
      changed=true;
    }
  }
  return changed;
}

void pass() {
  bool changed = true;
  while (changed) {
    changed = false;
    //    print(t);
    for (int x=0;x<M;++x)
      for (int y=0;y<N;++y) {
	if (compute(x,y))
	  changed = true;
      }
  }
}


int run() {
  reset();
  pass();
  return t[M-1][N-1];
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin>>H>>N>>M;
    for (int i=0;i<N;++i)
      for (int j=0;j<M;++j)
	cin >> b[j][i];
    for (int i=0;i<N;++i)
      for (int j=0;j<M;++j) {
	cin >> a[j][i];
	assert(a[j][i] <= b[j][i]);
      }
    assert(b[0][0] - H >= 50);
    assert(b[0][0] - a[0][0] >= 50);
    assert(b[M-1][N-1] - a[M-1][N-1] >= 50);
    x=0; y=0;
    //    print(b);
    //    print(a);
    cout<<"Case #"<<Ti<<": "<<run()*0.1<<endl;
  }
}
