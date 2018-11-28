#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
#include<assert.h>
using namespace std;
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
int T,H,W;
int m[101][101];
char output[101][101];
char c;
char fill(int h, int w) {
  if(output[h][w]!=' ') return output[h][w];

  int nh,nw,min=99999;

  // nord
  if(h>0 && min>m[h-1][w]) {
    min=m[h-1][w];
    nh=h-1; nw=w;
  }

  // west
  if(w>0 && min>m[h][w-1]) {
    min=m[h][w-1];
    nh=h; nw=w-1;
  }

  // east
  if(w+1<W && min>m[h][w+1]) {
    min=m[h][w+1];
    nh=h; nw=w+1;
  }

  // south
  if(h+1<H && min>m[h+1][w]) {
    min=m[h+1][w];
    nh=h+1; nw=w;
  }

  if(min<m[h][w]) {
    output[h][w]=fill(nh,nw);
    return output[h][w];
  } else {
    output[h][w]=c;
    return c++;
  }
}
int main() {
  cin>>T;
  FOR(i,T) {
    cin>>H>>W;
    FOR(h,H) FOR(w,W) { cin>>m[h][w]; output[h][w] = ' '; }
    c='a';
    FOR(h,H) FOR(w,W) fill(h,w);

    cout<<"Case #"<<i+1<<":\n";
    FOR(h,H) FOR(w,W) {
      cout<<output[h][w];
      if(w==W-1) cout<<"\n"; else cout<<" ";
    }
  }
  return 0;
};
