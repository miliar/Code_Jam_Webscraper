#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve(void){
  int C,D,N;
  map<pair<char, char>, char> combine;
  map<char, char> opposed;

  cin >> C;
  for(int i=0; i<C; i++){
    string s;
    cin >> s;
    pair<char, char> c1(s[0],s[1]);
    pair<char, char> c2(s[1],s[0]);
    combine[c1] = s[2];
    combine[c2] = s[2];
  }

  cin >> D;
  for(int i=0; i<D; i++){
    string s;
    cin >> s;
    opposed[s[0]] = s[1];
    opposed[s[1]] = s[0];
  }

  cin >> N;
  string s;
  cin >> s;
  vector<char> res;
  for(int i=0; i<N; i++){
    res.push_back(s[i]);
    if(2 <= res.size()){
      pair<char,char> p(res[res.size()-1],res[res.size()-2]);
      if(combine[p]!=char()){
        res[res.size()-2] = combine[p];
        res.pop_back();
      }
    }
    for(int j=0; j<res.size()-1; j++){
      if(res[j]==opposed[res[res.size()-1]]){
        res.clear();
        break;
      }
    }
  }

  cout << '[';
  for(int i=0; i<res.size(); i++){
    cout << res[i];
    if(i < res.size() - 1){
      cout << ", ";
    }
  }
  cout << ']' << endl;
}

int main(void){
  int testCaseCount;
  cin >> testCaseCount;
  for(int i=1; i<=testCaseCount; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
