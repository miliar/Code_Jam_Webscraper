#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;
string doperm(string s, vector<int> v){
  string ret = s;
  for(int i=0;i<(int)v.size();i++){
    ret[i] = s[v[i]];
  }
  return ret;
}
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    int k;
    cin >> k;
    string s;
    cin >> s;
    int l;
    l = s.length();
    vector<int> v(k);
    for(int i=0;i<k;i++){
      v[i] = i;
    }
    int minimum = 10000;
    do {
      string generated;
      for(int i=0;i<l/k;i++){
	generated += doperm(s.substr(i*k,k), v);
      }
      int prev = -1;
      int count = 0;
      for(int i=0;i<l;i++){
	if(prev != generated[i])count++;
	prev = generated[i];
      }
      minimum = min(minimum, count);
    } while(next_permutation(v.begin(), v.end()));
    cout << minimum << endl;
  }
  return 0;
}
