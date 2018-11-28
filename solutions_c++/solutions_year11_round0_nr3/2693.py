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
#define MAPI(m,e) if(m.find(e)!=m.end()){m[e]+=1;}else{m.insert(make_pair(e,1));}
#define SORT(c) sort(c.begin(), c.end())

const int INF = 1000000000;

typedef vector<int> vi; typedef long long Int;
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

int T, N, c;
int C[1001];

int add(int a, int b) {
  int r = 0;
  
  int p = 0;
  while (a > 0 || b > 0) {
    r += (((a&1) + (b&1)) % 2) << p;
    a >>= 1;
    b >>= 1;
    p++;
  }
  
  return r;
}

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);
  
  scanf("%d\n",&T);
  FORU(testcase,0,T) {   
    cin >> N; REP(i,N) { cin >> c; C[i] = c; }
    
    int best = -1;
    bool exist = false;
    sort(C,C+N);
    
    FORU(s,1,N) {
      int sum = 0, rsum = 0;
      int zum = 0, rzum = 0;
      FORU(i,0,s) {
        sum = add(sum, C[i]);
        rsum += C[i];
      }
      FORU(i,s,N) {
        zum = add(zum, C[i]);
        rzum += C[i];
      }

      if (sum == zum) {
        exist = true;
        if (rzum > best) {
          best = rzum; break;
        }
      }
    }
          
    printf("Case #%d: ",testcase+1);
    if (!exist) {      
      cout << "NO";   
    } else {
      cout << best;
    } cout << '\n';
  }

  return 0;
}