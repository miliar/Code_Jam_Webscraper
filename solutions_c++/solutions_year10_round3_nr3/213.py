#include <iostream>
#include <map>

using namespace std;

int hex(char c) {
  c = ::tolower(c);
  if (c>='0' && c<='9') return c-'0';
  return c-'a'+10;
}

int solve(int tc) {
  bool board[513][513];
  bool used[513][513];
  int dp[513][513];
  
  int m, n; cin >> m >> n;
  
  for(int i=0; i<m; i++) {
    string s; cin >> s;
    for(int j=0; j<(int)s.size(); j++) {
      int x = hex(s[j]);
      for(int k=0;k<4;k++) {
        board[4*j+k][i] = (x>>(3-k))&1;
      }
    }
  }
  
  int left = n*m;
  
  for(int i=0;i<n;i++) dp[i][0] = 1;
  for(int i=0;i<m;i++) dp[0][i] = 1;
  
  int bx,by;
  
  memset(used, 0, sizeof used);
  
  map<int, int> res;
  
  while(left) {
    bx = by = 0;
    for(int j=1; j<m; j++) {
      for(int i=1; i<n; i++) {
        bool p = board[i][j];

        if((board[i-1][j-1] == p) && (board[i-1][j] != p) && (board[i][j-1] != p)) {
          dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
        } else {
          dp[i][j] = 1;
        }

        if(used[i][j])
          dp[i][j] = 0;

        if (dp[i][j] > dp[bx][by]) {
          bx = i;
          by = j;
        }
      }
    }
    
    int sz = dp[bx][by];

    res[sz]++;
    
    left -= sz*sz;
    
    if(sz==1) {
      res[1] += left;
      break;
    }
    cerr<<sz<<endl;
    
    for(int j=by; j>by-sz; j--) {
      for(int i=bx; i>bx-sz; i--) {
        used[i][j] = true;
      }
    }
    
  }
  
  printf("Case #%d: %d\n", tc, (int)res.size());
  
  for(typeof(res.rbegin()) it = res.rbegin(); it != res.rend(); ++it) {
    cout << it->first << " " << it->second << endl;
  }
  
  return 1;
}

int main() {
  int n; cin >> n;
  for(int i=1; solve(i)&&i<n;i++);
}