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
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int main() {
  int T;
  T = GETINT;
  FOR(test, T) {

    vvi diamond;
    diamond.clear();
    
    int k = GETINT;

    for(int i = 1; i <= 2*k-1; i++) {
      int num = k - abs(k - i);
      vi cur;
      FOR(j, num) cur.pb(GETINT);
      diamond.pb(cur);
    }

    int best = 123456789;

    for(int vert = 0; vert < 2 * k - 1 ; vert++)
      for(int hor = 0; hor < 2 * k - 1; hor++) {

        int nk = k + abs(k-1-vert) + abs(k-1-hor);
        //        cerr << vert << ' ' << hor << ' ' << k + nk << endl;
       
        bool ok = true;

        map< PII, int> m;
        m.clear();

        FOR(i, s(diamond)) {
          FOR(j, s(diamond[i])) {
            int what = diamond[i][j];

            int v = abs(k - 1 - i) + 2 * j;
            int h = i;

            m[PII(v-vert, h-hor)] = what;
            
            PII reflection = PII(v-vert, hor - h);
            if(m.find(reflection) != m.end() && m[reflection] != what) {
              ok = false;
              break;
            }
            reflection = PII(vert-v, h - hor);
            if(m.find(reflection) != m.end() && m[reflection] != what) {
              ok = false;
              break;
            }            
          }
          if(!ok) break;
        }

        if(ok && (nk < best)) {
          best = nk;
        }
      }
    printf("Case #%d: %d\n", 1+test, best*best-k*k);
  }
  return 0;
}
