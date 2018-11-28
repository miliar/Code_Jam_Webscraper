#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <cmath>
#include <set>

using namespace std;

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

int h,w;
Mi m;
Mc l;
char nextLabel;

int dc[4] = {0,-1,1,0};
int dr[4] = {-1,0,0,1};

bool ok(int r, int c) {
  return 0<=r && 0<=c && r<h && c<w;
}

char label(int r, int c) {
  char &v=l[r][c];
  if (v=='.') {
    int mn=m[r][c];
    int best=-1;
    forUp(d,4) {
      int r2=r+dr[d];
      int c2=c+dc[d];
      if (!ok(r2,c2)) continue;
      if (m[r2][c2]<mn) {
        mn=m[r2][c2];
        best=d;
      }
    }
    if (best!=-1)
      v=label(r+dr[best],c+dc[best]);
    else
      v=nextLabel++;
  }
  return v;
}

int main() {
  int T;
  cin >> T;
  forUp(t,T) {
    cin >> h >> w;
    m=Mi(h,Vi(w)); 
    forUp(r,h) forUp(c,w) cin >> m[r][c];
    l=Mc(h,Vc(w,'.'));
    nextLabel='a';
    forUp(r,h) forUp(c,w) label(r,c);
    
    cout << "Case #" << t+1 << ":\n";
    forUp(r,h) {
      forUp(c,w) {
        cout << l[r][c];
        if (c<w-1) cout << " ";
      }
      cout << endl;
    }
  }
  return 0;
}






