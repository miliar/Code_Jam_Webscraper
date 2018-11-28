#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

inline int hash (char c1, char c2) {
  char mi = c1>c2?c1:c2;
  char ma = c1>c2?c2:c1;
  return mi*256+ma;
}

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    int i,j,c,d,n;
    map<int, char> com;
    map<int, int> op;
    cin >> c;
    REP(i,c){
      string s;
      cin >> s;
      com[hash(s[0],s[1])] = s[2];
    }
    cin >> d;
    REP(i,d){
      string s;
      cin >> s;
      op[hash(s[0],s[1])] = 1;
    }
    cin >> n;
    string s;
    cin >> s;
    string t;
    REP(i,n){
      t += s[i];
      int size=t.size();
      if(t.size()<2) continue;
      // check combine
      int h = hash(t[size-2],t[size-1]);
      if(com[h]){
        t = t.substr(0, size-2) + com[h];
        continue;
      }
      // check oppose
      bool oppose = false;
      REP(j,size-1){
        if(op[hash(t[j],t[size-1])]){
          oppose = true;
          break;
        }
      }
      if(oppose){
        t = "";
      }
    }
    string ans = "[";
    bool first = true;
    REP(i,t.size()){
      if(first){
        ans += t[i];
        first=false;
      }else{
        ans += ", ";
        ans += t[i];
      }
    }
    ans += "]";
    gp(ans);
  }
  return 0;
}

