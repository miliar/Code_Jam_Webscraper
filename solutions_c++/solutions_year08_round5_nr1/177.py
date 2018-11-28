#include<cstdio>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
#include<sstream>

using namespace std;

#define pf printf
#define sf scanf
#define co continue
#define re return
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

struct point
{
  int x, y;
};

vector<point> v;
string S;
char str[100000];

int move[][2] = 
{
  1, 0, 0, 1, -1, 0, 0, -1
};

bool inside(double x, double y) {
  double x1 = 1000;
  double y1 = y;
  
  int cnt = 0;
  int i;
  for(i=0;i+1<v.size();i++) {
    if( v[i].y == v[i+1].y ) co;
    if( v[i].x > x && v[i].x < x1  && max(v[i].y, v[i+1].y) > y && min(v[i].y, v[i+1].y) < y )
      cnt++;
  }
  return cnt % 2 == 1;
}



bool valid(double x, double y) {
  if( inside(x,y) ) return false;
  
  bool up, down, left, right;
  up = down = left = right = false;
  
  // up
  double x1 = x;
  double y1 = 1000;
  int i;
  for(i=0;i+1<v.size() && up == false;i++) {
    if( v[i].x == v[i+1].x ) co;
    if( v[i].y > y && v[i].y < y1 && max(v[i].x, v[i+1].x) > x && min(v[i].x, v[i+1].x) < x )
      up = true;
  }
  
  // down;
  x1 = x;
  y1 = -1000;
  for(i=0;i+1<v.size() && down == false && up == true;i++) {
    if( v[i].x == v[i+1].x ) co;
    if( v[i].y > y1 && v[i].y < y && max(v[i].x, v[i+1].x) > x && min(v[i].x, v[i+1].x) < x )
      down = true;
  }
  if( up == true && down == true ) return true;
  // left
  x1 = -1000;
  y1 = y;
  
  for(i=0;i+1<v.size() && left==false;i++) {
    if( v[i].y == v[i+1].y ) co;
    if( v[i].x > x1 && v[i].x < x  && max(v[i].y, v[i+1].y) > y && min(v[i].y, v[i+1].y) < y )
      left = true;
  }

// right
  x1 = 1000;
  y1 = y;
  
  for(i=0;i+1<v.size() && right==false && left==true;i++) {
    if( v[i].y == v[i+1].y ) co;
    if( v[i].x > x && v[i].x < x1  && max(v[i].y, v[i+1].y) > y && min(v[i].y, v[i+1].y) < y )
      right = true;
  }  
  bool yes = false;
  if( up == true && down == true ) yes = true;
  if( left == true && right == true ) yes = true;
  
  re yes;
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    int cases = 1;
    for( sf("%d", &t); t--;  ) {
      v.clear(); S.clear();
      int L;
      sf("%d", &L);
      while(L--) {
        sf("%s", str);
        int k; sf("%d", &k);
        string s = "";
        while(k--)
          s += str;
        S += s;
      }
      point p;
      p.x = 0;
      p.y = 0;
      int d = 0;
      v.pb(p);
      double maxx, maxy, minx, miny;
      maxx = minx = maxy = miny = 0;
      int i, j;
      for(i=0; i<S.size(); i++) {
        if( S[i] == 'L' ) { d--; d += 4; d %= 4; }
        else if( S[i] == 'R' ) { d++; d %= 4; }
        else {
          for(j=i; j<S.size() && S[j] == 'F'; j++);
          int k = j - i;
          i = j-1;
          
          // k = number of forward moves
          
          point np;
          np.x = p.x + k * move[d][1];
          np.y = p.y + k * move[d][0];
          p = np;
          maxx >?= np.x; minx <?= np.x;
          maxy >?= np.y; miny <?= np.y;
          v.pb(np);
        }
      }
      
      double x, y;
      int res = 0;
      for(x=minx+0.5; x<maxx; x += 1)
        for(y=miny+0.5; y<maxy; y += 1)
          if( valid(x,y) ) res++;
      pf("Case #%d: %d\n", cases++, res);
      
    }
    return 0;
}
