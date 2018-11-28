#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
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
#include <time.h>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
typedef vector<int> vi; typedef long long Int;

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

vector<int> splitInts (string s, string del = " ") { vector<int> res;
  vector<string> t = split(s,del);
  for (int i = 0; i < t.size(); ++i) {
    if (t[i].size() > 10 || (t[i].size()==10 && t[i][0]>='2')) {
      res.push_back(2000000000);
    } else { res.push_back(atoi(t[i].c_str())); }
  } return res;
}

#endif

struct Points {
  int a, b, c;

  Points () {}
  Points (int a, int b, int c) : a(a), b(b), c(c) {}

  bool operator< (const Points &p) const {
    if (a < p.a) return true;
    if (a > p.a) return false;
    if (b < p.b) return true;
    if (b > p.b) return false;
    if (c < p.c) return true;
    if (c > p.c) return false;    
    return false;
  }

  friend ostream& operator<< (ostream& os, const Points &i) {
    return os << i.a << "," << i.b << "," << i.c;
  }

};

int T;
int N,S,P; 
int PTS[111];

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15); 

  scanf("%d",&T);
  REP(testcase,T) {
    scanf("%d %d %d",&N,&S,&P);
    REP(i,N) {
      scanf("%d",&PTS[i]);
    }    
    
    vector<Points> VP;
    REP(i,N) {
      int a = PTS[i]/3;
      int b = (PTS[i] - a)/2;
      int c = (PTS[i] - a - b);
      VP.PB(Points(a,b,c));
    }

    sort(VP.begin(),VP.end());
    
    int ans = 0;
    for(int i = N-1; i >= 0; i--) {
      if (VP[i].a >= P || VP[i].b >= P || VP[i].c >= P) {
        ++ans;
      } else {
        if (S > 0 && VP[i].b > 0 && VP[i].c < 10 && VP[i].b == VP[i].c) {
          if (VP[i].c + 1 >= P) {
            S -= 1;
            ans++;
          }
        }
      }
      //cout << VP[i] << " " << ans << " S = " << S << endl;
    }
    
    solution:
    printf("Case #%d: %d\n",testcase+1,ans);
  }

  return 0;
}