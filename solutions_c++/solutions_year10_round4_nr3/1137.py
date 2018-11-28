#include <cstdio>
#include <set>

#define FORC(it, c) for( __typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it ) 

using namespace std;

typedef pair<int, int> coord;

set<coord> s[2];

int solve() {
  for( int itr = 0; ; ++itr ) {
    int curr = itr % 2;
    int next = curr ^ 1;
    if( s[curr].empty() )
      return itr;
    s[next] = s[curr];
    FORC(it, s[curr]) {
      coord left(it->first-1, it->second);
      coord up(it->first, it->second-1);
      if( s[curr].find(left) == s[curr].end() 
          && s[curr].find(up) == s[curr].end() ) {
        s[next].erase(*it);
      }
      coord down_left(it->first-1, it->second+1);
      coord down(it->first, it->second+1);
      if( s[curr].find(down_left) != s[curr].end() ) 
        s[next].insert(down);
    }
  }
  return 0;
}

void input() {
  s[0].clear();
  int x1, y1, x2, y2, n;
  scanf("%d", &n);
  for( int i = 0; i < n; ++i ) {
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    for( int x = x1; x <= x2; ++x ) 
      for( int y = y1; y <= y2; ++y ) 
        s[0].insert(coord(x, y));
  }
}

int main() {
  int n_tc;
  scanf("%d", &n_tc);
  for( int i = 1; i <= n_tc; ++i ) {
    input();
    printf("Case #%d: %d\n", i, solve());
  }
  return 0;
}
