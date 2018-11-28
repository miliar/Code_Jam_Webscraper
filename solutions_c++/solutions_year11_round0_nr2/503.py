#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

char invoke[256][256];
bool forb[256][256];

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");

  int n, c, d, idx;
  string s;
  char ret[300];
  FOR (test, tests){
    SET(invoke, 0);
    SET(forb, 0);
    cin >> c;
    FOR (i, c){
      cin >> s;
      char ch1 = s[0], ch2 = s[1], r = s[2];
      invoke[ch1][ch2] = invoke[ch2][ch1] = r;
    }
    
    cin >> d;
    FOR (i, d){
      cin >> s;
      char ch1 = s[0], ch2 = s[1];
      forb[ch1][ch2] = forb[ch2][ch1] = true;
    }
    cin >> n;
    cin >> s;
    idx = -1;
    char c;
    FOR (i, n){
      ret[++idx] = s[i];
      while (idx > 0 && (c = invoke[ret[idx]][ret[idx - 1]]) != 0)
        ret[--idx] = c;
      c = ret[idx];
      FOR (j, idx)
        if (forb[ret[j]][c]){
          idx = -1;
          break;
        }
    }
    
    cout << "Case #" << (test + 1) << ": ";
    cout << "[";
    FOR (i, idx + 1){
      if (i)
        cout << ", ";
      cout << ret[i];
    }
    cout << "]" << "\n";
  }
  return 0;
}
