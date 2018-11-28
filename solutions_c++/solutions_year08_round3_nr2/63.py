#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

ll cnt;

bool ugly(ll n){
  return (n%2 == 0 || n%3 == 0 || n%5 == 0 || n%7 == 0);
}

void dfs(int depth, string &s, ll sum){
  if(depth == s.length()){
    if(ugly(sum))
      ++cnt;
  }
  else{
    ll num = 0;
    for(int i = depth; i < s.length(); ++i){
      num *= 10;
      num += s[i] - '0';

      dfs(i+1, s, sum + num);
      if(depth > 0)
        dfs(i+1, s, sum - num);
    }
  }
}

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    string line;
    cin >> line;

    cnt = 0;
    dfs(0, line, 0);

    cout << "Case #" << k+1 << ": " << cnt << endl;
  }

  return 0;
}
