#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int dy[]={-1,0,1,0},dx[]={0,1,0,-1};

int W;

bool isdig(char c) {
  return c>='0' && c<='9';
}

bool ok(int y, int x) {
  return y>=0 && y<W && x>=0 && x<W;
}

int main() {
  int T;
  cin >> T;
  for (int iT=0; iT<T; ++iT) {
    int Q;
    cin >> W >> Q;
    vector<string> v(W);
    for (int i=0; i<W; ++i) {
      cin >> v[i];
    }
    cout << "Case #" << iT+1 << ":" << endl;
    for (; Q--;) {
      vector<vector<map<int,string> > > a(W,W),b(W,W);
      int n;
      cin >> n;
      for (int i=0; i<W; ++i) {
        for (int j=0; j<W; ++j) if (isdig(v[i][j])) {
          a[i][j][int(v[i][j]-'0')]=string(1,v[i][j]);
        }
      }
      string sol="";
      for (int cnt=0; sol==""; ++cnt) {
        //cerr << cnt << endl;
        swap(a,b);
        for (int i=0; i<W; ++i) {
          for (int j=0; j<W; ++j) if (isdig(v[i][j])) {
            a[i][j].clear();
            if (b[i][j].find(n)!=b[i][j].end()) {
              if (sol=="") sol=b[i][j][n];
              else sol=min(sol,b[i][j][n]);
            }
          }
        }
        for (int i=0; i<W; ++i) for (int j=0; j<W; ++j) if (isdig(v[i][j])) {
          for (map<int,string>::iterator it=b[i][j].begin(); it!=b[i][j].end(); ++it) {
            for (int d1=0; d1<4; ++d1) for (int d2=0; d2<4; ++d2) {
              int ni=i+dy[d1],nj=j+dx[d1];
              int nni=ni+dy[d2],nnj=nj+dx[d2];
              if (ok(ni,nj) && ok(nni,nnj)) {
                int val=it->first;
                if (v[ni][nj]=='+') val+=int(v[nni][nnj]-'0');
                else val-=int(v[nni][nnj]-'0');
                string s=it->second;
                s=(s+v[ni][nj])+v[nni][nnj];
                if (a[nni][nnj].find(val)==a[nni][nnj].end()) {
                  a[nni][nnj][val]=s;
                }
                else a[nni][nnj][val]=min(a[nni][nnj][val],s);
              }
            }
          }
        }
      }
      cout << sol << endl;
    }
  }
}
