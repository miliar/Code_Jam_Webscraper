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
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

const int Inf=1000000000;
int nRows, nCols, maxFall;
Vs M;
vector<Mi> C;

int fall(int r, int c) {
  int f=0;
  while (r<nRows-1 && M[r+1][c]=='.') {
    f++;
    r++;
  }
  return f;
}

// Is c0 in [c,c+d]?
bool indug(int c, int d, int c0) {
  if (d<0)
    return c0>=c+d && c0<=c;
  else
    return c0<=c+d && c0>=c;
}

int minDig(int r, int c, int d) {
  if (r==nRows-1) return 0;
  int &V=C[r][c][d+nCols];
  if (V!=-1) return V;

  int mn=Inf;

  int c0=c,c1=c; // First/last col we can go to before falling
  while (c0 && (M[r][c0-1]=='.' || indug(c,d,c0-1)) && M[r+1][c0]=='#') c0--;
  while (c1<nCols-1 && (M[r][c1+1]=='.' || indug(c,d,c1+1)) && M[r+1][c1]=='#') c1++;

//   disp2(c0,c1);
//   if (r==2 && c==1 && d==0) {
//     disp("hej");
//     disp2(c0,c1);
//     disp(fall(2,1));
//     disp(fall(2,2));
//   }
//   disp2(r,M[r]);
//   disp2(c0,c1);
  for (int s=c0; s<=c1; s++) {
    int f=fall(r,s);
//     disp2(s,f);
    if (f>0 && f<=maxFall)
      mn=min(mn,minDig(r+f,s,0));
    if (f>0) continue;
    if (s<c1) {
      int f=fall(r+1,s+1)+1;
//       if (r==2 && c==1 && d==0) {
//         disp2(s,f);
//       }
      if (f<=maxFall) {
        for (int d2=0; s+1+d2<=c1; d2++) {
          mn=min(mn,minDig(r+f,s+1,d2)+1+d2);
          if (f>1) break;
        }
      }
    }
    if (s>c0) {
      int f=fall(r+1,s-1)+1;
//       if (r==2 && c==1 && d==0) {
//         disp2(s,f);
//       }
      if (f<=maxFall) {
        for (int d2=0; s-1-d2>=c0; d2++) {
          mn=min(mn,minDig(r+f,s-1,-d2)+1+d2);
          if (f>1) break;
        }
      }
    }
  }

//   disp4(r,c,d,mn);
  V=mn;
  return mn;
}

int main() {
  int nCases;
  cin >> nCases;
  forUp(cnr,nCases) {
    cin >> nRows >> nCols >> maxFall;
    string s;
    getline(cin,s);
    M=Vs(nRows);
    C=vector<Mi>(nRows,Mi(nCols,Vi(2*nCols+2,-1)));
    forUp(r,nRows)
      getline(cin,M[r]);
//     disp2(maxFall,M);
    int d=minDig(0,0,0);
    cout << "Case #" << cnr+1 << ": ";
    if (d==Inf)
      cout << "No";
    else
      cout << "Yes " << d;
    cout << endl;
  }
  
  return 0;
}






