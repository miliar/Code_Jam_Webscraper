#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


int main() {
  int l, d, n;
  l = GETINT;
  d = GETINT;
  n = GETINT;

  vs dict;
  while(d--) {
    char s[1000];
    scanf("%s", s);
    string str(s);
    dict.pb(str);    
  }

  FOT(test, 1, n+1) {
    vs cur;
    char s[10000];
    scanf("%s", s);
    string str(s);
    int m = s(str);
    bool pick = false;
    string toadd = "";
    FOR(i, m) {
      if(str[i] == '(') {
        toadd = "";
        pick = true;
      }
      else if(str[i] == ')') {
        pick = false;
        if(s(toadd) > 0) cur.pb(toadd);
        toadd = "";
      }
      else if(pick) {
        toadd += str[i];
      }
      else {
        toadd = "";
        toadd += str[i];
        cur.pb(toadd);
      }
    }
    int count = 0;
    
    FOR(i, s(dict)) {
      bool good = true;
      FOR(j, l) {
        bool curgood = false;
        FOR(k, s(cur[j])) {     
          if(cur[j][k] == dict[i][j]) { 
            curgood = true;
            break;
          }
        }
        good = good && curgood;
      }
      if(good) count++;
    }
    printf("Case #%d: %d\n", test, count);
  }
  
  return 0;
}
