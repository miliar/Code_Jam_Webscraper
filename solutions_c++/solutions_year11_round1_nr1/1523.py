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
  
int T, N, D, PD, G, PG;
string line;

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);
  
  scanf("%d\n",&T);
  FORU(testcase,0,T) {   
    scanf("%d %d %d\n",&N,&PD,&PG);
    D = -1; G = -1;
    set<int> A;
    
    if ((PG == 100 && PD != 100) || (PG == 0 && PD != 0)) {
      // impossible
    } else {    
      FORU(today,1,N+1) {
        if ((PD*today) % 100 == 0) {
          D = today;
          int all = D;
          while (1) {
            if (A.find((PG*all) % 100) != A.end()) {            
              break;
            } else {
              A.insert((PG*all) % 100);
              if ((PG*all) % 100 == 0) {
                G = all;
                break;
              }
            }
            all += 1;
          }        
          break;
        }
      }    
    }
    
    // cout << D << " " << G << endl;
    
    if (D != -1 && G != -1) {
      printf("Case #%d: Possible\n",testcase+1);
    } else {
      printf("Case #%d: Broken\n",testcase+1);
    }    
  }

  return 0;
}