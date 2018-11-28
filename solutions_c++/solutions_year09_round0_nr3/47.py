#include<iostream>
#include<cstring>
using namespace std;

string welcome = "welcome to code jam";
int memo[512][32];

int rec(int n, int m,const string &str){
  if( m == 0 ) return 1;
  
  int &res = memo[n][m];
  if( res != -1 ) return res;
  res = 0;

  for(int i = 0; i < n; i++){
    if( str[i] == welcome[m-1] ) {
      res += rec(i, m-1, str);
      if( res >= 10000 ) res %= 10000;
    }
  }

  return res;
}

int main(){
  int T;
  cin >> T >> ws;
  for(int tno = 0; tno < T; tno++){
    string str;
    getline(cin, str);

    int N = str.size();
    int M = welcome.size();
    
    memset( memo, -1, sizeof(memo));

    int ans = 0;
    for(int i = 0; i < N; i++){
      if( str[i] == welcome[M-1] ){
        ans += rec(i, M-1, str);
        if( ans >= 10000 ) ans %= 10000;
      }
    }
    
    printf("Case #%d: %04d\n", tno + 1, ans);
  }
}
