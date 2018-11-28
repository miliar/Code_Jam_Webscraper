#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <vector>

using namespace std;

#define MAX 550

int grid[MAX][MAX];
int left[MAX][MAX];
int down[MAX][MAX];

int where[MAX][MAX];

int R, C;

map<int, int> sizes;

struct Cand {
  int d;
  int r, c;
  Cand(int d, int r, int c) : d(d), r(r), c(c) { }
  friend bool operator<(const Cand& A, const Cand& B) {
    if( A.d != B.d ) 
      return A.d > B.d;
    if( A.r != B.r ) 
      return A.r < B.r;
    return A.c < B.c;
  }
  friend bool operator==(const Cand& A, const Cand& B) {
    return A.d == B.d && A.r == B.r && A.c == B.c;
  }
};


set<Cand> s;

set<Cand>::iterator sit[MAX][MAX];

int get(int r, int c) {
  if( sit[r][c] != s.end() ) 
    return sit[r][c]->d;
  return 0;
}

void add(int d, int r, int c) {
  sit[r][c] = s.insert(Cand(d, r, c)).first;
}

void remove(int r, int c) {
  if( sit[r][c] == s.end() ) 
    return ;
  s.erase(sit[r][c]);
  sit[r][c] = s.end();
}

void fix(int d0, int r0, int c0) {
  //printf("Fixing: %d %d %d\n", r0, c0, d0);
  for( int r = max(0, r0-d0+1); r < r0+d0; ++r ) {
    for( int c = max(0, c0-d0+1); c < c0+d0; ++c ) {
      //inside
      if( r >= r0 && c >= c0 ) {
        remove(r, c);
      }
      //down left
      else if( r >= r0 && c < c0 ) {
        int d = min(get(r, c), c0-c);
        remove(r, c);
        if( d > 0 ) 
          add(d, r, c);
      }
      //top right
      else if( r < r0 && c >= c0 ) {
        int d = min(get(r, c), r0-r);
        remove(r, c);
        if( d > 0 ) 
          add(d, r, c);
      }
      //top left
      else {
        int d = min(get(r, c), max(r0-r, c0-c));
        remove(r, c);
        if( d > 0 ) 
          add(d, r, c);
      }
    }
  }
}

void precompute() {
  s.clear();
  for( int r = 0; r <= R; ++r ) 
    for( int c = 0; c <= C; ++c ) 
      sit[r][c] = s.end();

  for( int r = 0; r < R; ++r ) {
    left[r][C] = down[r][C] = 0;
    grid[r][C] = grid[r][C-1];
  }
  for( int c = 0; c < C; ++c ) {
    left[R][c] = down[R][c] = 0;
    grid[R][c] = grid[R-1][c];
  }
  left[R][C] = down[R][C] = 0;
  grid[R][C] = !grid[R-1][C-1];

  for( int r = R-1; r >= 0; --r ) 
    for( int c = C-1; c >= 0; --c ) {
      if( grid[r][c] ^ grid[r][c+1] ) 
        left[r][c] = left[r][c+1] + 1;
      else
        left[r][c] = 1;
      if( grid[r][c] ^ grid[r+1][c] ) 
        down[r][c] = down[r+1][c] + 1;
      else
        down[r][c] = 1;

      int d = 1;
      if( grid[r][c] == grid[r+1][c+1] ) 
        d = min(min(left[r][c], left[r+1][c+1]+1),
                min(down[r][c], down[r+1][c+1]+1));
      d = min(d, get(r+1, c+1)+1);
      add(d, r, c);
    }
}

void solve() {
  int cnt = 0;
  memset(where, 0, sizeof(where));
  sizes.clear();
  int ret = 0;
  while( !s.empty() ) {
    Cand u = *s.begin();
    ++sizes[u.d];
    remove(u.r, u.c);    
    fix(u.d, u.r, u.c);

    if( cnt < 9 ) { 
      where[u.r][u.c] = ++cnt;
      //printf("(%d: %d %d %d)\n", cnt, u.r, u.c, u.d);
    }
  }
}

void input() {
  scanf("%d%d", &R, &C);
  for( int r = 0; r < R; ++r ) {
    static char buff[MAX];
    scanf("%s", buff);
    for( int i = 0; i < C/4; ++i ) {
      char s[2]; int x;
      strncpy(s, buff+i, 1);
      s[2] = '\0';
      sscanf(s, "%x", &x);
      for( int j = 3; j >= 0; --j ) {
        if( (1<<j)&x ) 
          grid[r][4*i+3-j] = 1;
        else
          grid[r][4*i+3-j] = 0;
      }
      
    }
  }
}

void output(int tc) {
  printf("Case #%d: %d\n", tc+1, sizes.size());
  vector< pair<int, int> > v;
  for( map<int, int>::iterator it = sizes.begin(); it != sizes.end(); ++it  ) 
    v.push_back(make_pair(it->first, it->second));
  for( int i = (int)v.size()-1; i >= 0; --i ) 
    printf("%d %d\n", v[i].first, v[i].second);
}

void debug_steps() {
  printf("\nSteps: \n");
  for( int r = 0; r < R; ++r, printf("\n") ) 
    for( int c = 0; c < C; ++c ) 
      printf("%1d ", where[r][c]); 
}

void print_board() {
  for( int r = 0; r < R; ++r, printf("\n") ) 
    for( int c = 0; c < C; ++c ) 
      printf("%d", grid[r][c]);

  printf("\n");
  for( int r = 0; r < R+1; ++r, printf("\n") ) 
    for( int c = 0; c < C+1; ++c )
      printf("%d ", get(r, c));
}

int main() {
  int tc;
  scanf("%d", &tc);
  for( int i = 0; i < tc; ++i ) {
    input();
    precompute();
    //print_board();
    solve();
    output(i);
    //debug_steps();
  }
  return 0;
}
