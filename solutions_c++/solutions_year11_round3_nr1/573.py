#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()

int t, w, h;
char m[52][52];

int main() {
  int count = 0;
  scanf("%d", &t);
  
  while(t--) {
    scanf("%d%d", &h, &w);
    rep(i, h)
      scanf("%s", m[i]);
    
    bool f = false;
    rep(y, h-1) {
      if(f) break;
      rep(x, w-1) {
        if(f) break;
        if(m[y][x] == '#') {
          if(m[y][x+1] == '#' && m[y+1][x] == '#' && m[y+1][x+1] == '#') {
            m[y][x] = m[y+1][x+1] = '/';
            m[y][x+1] = m[y+1][x] = '\\';
          }
          else { f=true; break; }
        }
      }
    }
    rep(y, h) if(m[y][w-1] == '#') f = true;
    rep(x, w) if(m[h-1][x] == '#') f = true;
    
    printf("Case #%d:\n", ++count);
    if(f) printf("Impossible\n");
    else {
      rep(y, h) {
        printf("%s\n", m[y]);
      }
    }
  }
  
  return 0;
}

