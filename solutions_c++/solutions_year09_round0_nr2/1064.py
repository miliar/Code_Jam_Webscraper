#include <iostream>
#include <vector>

using namespace std;

const int dy[]={-1,0,0,1},dx[]={0,-1,1,0};
const int INF=1000000000;

int h,w;

bool ok(int y, int x) {
  return y>=0 && y<h && x>=0 && x<w;
}

int repr(vector<vector<int> > &fath, int nd) {
  int y=nd/w,x=nd%w;
  if (fath[y][x]==nd) return nd;
  return fath[y][x]=repr(fath,fath[y][x]);
}

int main() {
  int T;
  cin >> T;
  for (int iT=0; iT<T; ++iT) {
    cin >> h >> w;
    vector<vector<int> > v(h,w),fath(h,w);
    for (int i=0; i<h; ++i) {
      for (int j=0; j<w; ++j) {
        cin >> v[i][j];
        fath[i][j]=i*w+j;
      }
    }
    for (int i=0; i<h; ++i) {
      for (int j=0; j<w; ++j) {
        int bd=-1,bval=INF;
        for (int d=0; d<4; ++d) if (ok(i+dy[d],j+dx[d])) {
          int val=v[i+dy[d]][j+dx[d]];
          if (val<bval) {
            bd=d;
            bval=val;
          }
        }
        if (bval<v[i][j]) {
          int ra=repr(fath,i*w+j),rb=repr(fath,(i+dy[bd])*w+(j+dx[bd]));
          if (ra!=rb) fath[ra/w][ra%w]=rb;
        }
      }
    }
    vector<vector<char> > bas(h,vector<char>(w,'.'));
    char cur='a';
    cout << "Case #" << iT+1 << ":" << endl;
    for (int i=0; i<h; ++i) {
      for (int j=0; j<w; ++j) {
        int y=repr(fath,i*w+j)/w,x=repr(fath,i*w+j)%w;
        if (bas[y][x]!='.') bas[i][j]=bas[y][x];
        else bas[i][j]=bas[y][x]=cur++;
        if (j>0) cout << " ";
        cout << bas[i][j];
      }
      cout << endl;
    }
  }
}
