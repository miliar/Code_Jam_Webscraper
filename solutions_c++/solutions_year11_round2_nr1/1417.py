#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define MOD 1000000009
#define DEC(a,b) (((a + b) >= MOD) ? (a+b-MOD) : (a+b))
#define INC(a,b) (((a + b) < 0) ? (a+b+MOD) : (a+b))

#define FMAX(a,b) if (b > a) { a = b; }
#define FMIN(a,b) if (b < a) { a = b; }

#define MP make_pair
#define ND second
#define PB push_back
#define ST first
#define SZ(c) ((int)(c).size())
#define CLR(c) memset(c, 0, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define MAPI(m,e,v) if(m.find(e)!=m.end()){m[e]+=v;}else{m.insert(make_pair(e,v));}
#define SORT(c) sort(c.begin(), c.end())

const int INF = 1000000000;

typedef long long Int;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;

#endif

#ifndef TOOLS

template <class T> T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
template <class T> string t2s(T x) {ostringstream o; o << x; return o.str();}

vector<string> split (string s, string del = " ") { vector<string> res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

#endif

int T, N;
string line, S[101];

double WP[101];
double OWP[101];
double OOWP[101];

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  FORU(testcase,0,T) {
    cin >> N;
    REP(r,N) {
      cin >> line;
      S[r] = line;
    }

    // WP
    
    REP(r,N) {
      int played = 0, won = 0;
      REP(c,N) {
        if (S[r][c] != '.') {
          ++played;
          if (S[r][c] == '1') {
            ++won;
          }
        }      
      }
      WP[r] = (double)won / (double)played;
    }
    
    // OWP
    
    REP(p,N) {
      int opp = 0; double sumWP = 0.0;
      REP(o,N) {
        if (S[p][o] != '.') {        
          int played = 0, won = 0;
          REP(c,N) if (c != p) {
            if (S[o][c] != '.') {
              ++played;
              if (S[o][c] == '1') {
                ++won;
              }
            }      
          }
          sumWP += (double)won / (double)played;
          opp += 1; 
        }
      }
      OWP[p] = (double)sumWP / (double)opp;    
    }
    
    // OOWP

    REP(r,N) {
      int opp = 0; double sumWP = 0.0;
      REP(c,N) {
        if (S[r][c] != '.') {
          ++opp;
          sumWP += OWP[c];
        }      
      }
      OOWP[r] = (double)sumWP / (double)opp;
    }   
    
    solution:
    printf("Case #%d:\n",testcase+1);
    REP(r,N) {
      double res = 0.25 * WP[r] + 0.50 * OWP[r] + 0.25 * OOWP[r];
      cout << res << endl;
    }
  }

  return 0;
}