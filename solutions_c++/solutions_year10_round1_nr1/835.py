#include<iostream>
#include<string>
#include<vector>
#define MAX 54
using namespace std;

void rotate(int n, vector<string> &map){
  vector<string> ret = map;
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < n; ++j){
      ret[i][j] = '.';
    }
  }
  for(int i = n-1; i >= 0; --i){
    for(int j = 0; j < n; ++j){
      ret[j][n-i-1] = map[i][j];
    }
  }
  map = ret;
}

void gravity(int n, vector<string> &map){
  for(int j = 0; j < n; ++j){
    string s;
    for(int i = 0; i < n; ++i){
      s += map[i][j];
    }
    int erased = 0;
    for(int i = 0; i < n; ++i){
      if( s[i] == '.' ){
	s.erase(s.begin()+i);
	erased++;
	--i;
      }
    }
    for(int i = 0; i < erased; ++i){
      s.insert(s.begin(),'.');
    }
    for(int i = 0; i < n; ++i){
      map[i][j] = s[i];
    }
  }
}

#define RED 0
#define BLUE 1

string solve(int n, int K, vector<string> &map){
  int dp[2][MAX][MAX][4] = {{{{0,},},},};

  const int di[] = {0,1,1,1};
  const int dj[] = {1,1,0,-1};

  for(int i = n; i >= 1; --i){
    for(int j = n; j >= 1; --j){
      if( map[i-1][j-1] == 'R' ){
	for(int k = 0; k < 4; ++k){
	  dp[RED][i][j][k] = max( dp[RED][i][j][k], dp[RED][i+di[k]][j+dj[k]][k] + 1 );
	}
      }else if(map[i-1][j-1] == 'B'){
	for(int k = 0; k < 4; ++k){
	  dp[BLUE][i][j][k] = max( dp[BLUE][i][j][k], dp[BLUE][i+di[k]][j+dj[k]][k] + 1 );
	}
      }
    }
  }

  int maxBlue = 0;
  int maxRed = 0;
  bool winBlue = false;
  bool winRed = false;

  for(int i = 1; i <= n; ++i){
    for(int j = 1; j <= n; ++j){
      for(int k = 0; k < 4; ++k){
	maxRed = max( maxRed, dp[RED][i][j][k] );
	maxBlue = max( maxBlue, dp[BLUE][i][j][k] );
      }
    }
  }

  if( maxRed >= K ){
    winRed = true;
  }
  if( maxBlue >= K ){
    winBlue = true;
  }

  if( winBlue && winRed ){
    return string("Both");
  }else if( winBlue ){
    return string("Blue");
  }else if( winRed ){
    return string("Red");
  }else
    return string("Neither");
}

int main(){
  int T;
  cin >> T;
  for(int tc=1; tc<=T; ++tc){
    string ans;
    vector<string> map;
    int N,K;
    cin >> N >> K;
    for(int i = 0; i < N; ++i){
      string s;
      cin >> s;
      map.push_back(s);
    }
    rotate(N,map);
    gravity(N,map);
    ans = solve(N,K,map);
    printf("Case #%d: %s\n", tc, ans.c_str());
  }
  return 0;
}
