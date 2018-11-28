#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <cctype>
#include <set>
#include <fstream>
#include <cmath>
using namespace std;

#define rep(i, n) for(int i = 0; i< n; i++)
#define rep2(i, m, n) for(int i = m; i < n; i++)
typedef long long ll;
typedef pair<int, int> P;
const int INF = 1000000007;
const double EPS = 1e-10;

map<char, char> mp;

char mapping[26] = {
'y',
'h',
'e',
's',
'o',
'c',
'v',
'x',
'd',
'u',
'i',
'g',
'l',
'b',
'k',
'r',
'z',
't',
'n',
'w',
'j',
'p',
'f',
'm',
'a',
'q'
};


int main(){
  string s, ans;
  int T;

  cin >> T;
  getline(cin, s);
  rep(t, T){
    getline(cin, s);
    cout << "Case #" << t + 1 << ": ";
    rep(i, (int)s.size()){
      if(s[i] == ' ') cout << ' ';
      else cout << mapping[s[i] - 'a'];
    }
    cout << endl;
    /*
    rep(i, (int)s.size()){
      mp[s[i]] = ans[i];
    }
    */
  }
  /*
  cout << "char mapping[26] = {" << endl;
  for(map<char, char> ::iterator iter = mp.begin(); iter != mp.end(); iter++){
    cout << "'" << iter->second << "'," << endl;;
  }
  cout << "};" << endl;
  */
  
  return 0;
}
