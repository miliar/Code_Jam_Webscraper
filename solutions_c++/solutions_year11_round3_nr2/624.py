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

template <class K,class V> bool PAIR_BY_FIRST (
  const pair<K,V>& p1, const pair<K,V>& p2) { if (p1.first == p2.first) 
    return p1.second > p2.second; else return p1.first > p2.first; }  
  
template <class K,class V> bool PAIR_BY_SECOND (
  const pair<K,V>& p1, const pair<K,V>& p2) { if (p1.second == p2.second) 
    return p1.first > p2.first; else return p1.second > p2.second; }

#endif

Int t;
int T, L, N, C, A[1001];
int D[1111111];
int B[1111111];
vector< pair<int,int> > P;

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  FORU(testcase,0,T) {
    P.clear();
  
    cin >> L >> t >> N >> C;
    REP(i,C) { cin >> A[i]; }
    
    D[0] = 0;
    B[0] = 0;
    int idx = 1;
    while (idx < N) {
      REP(j,C) {
        D[idx] = A[j];
        B[idx] = 0;
        ++idx;
      }
    }

    // REP(i,N+1) cout << D[i] << " "; cout << endl;
    
    Int time = 0;
    int star = 0;    
    
    while (star < N && time < t) {
      if (time + D[star+1] * 2 <= t) {
        time += D[star+1] * 2;
        star++;
      } else { 
        // cout << "@" << star << ": ";
        // cout << D[star+1] << " " <<  t << " " << time << endl;
        D[star+1] = D[star+1] - (t - time)/2;
        P.PB(MP(star, D[star+1]));
        time = t;
        break;
      }
    }    
    
    if (star < N) {
    
      if (time == 0) {
        FORU(s,star,N) {
          P.PB(MP(s,D[s+1]));
        }  
      } else {    
        FORU(s,star+1,N) {
          P.PB(MP(s,D[s+1]));
        }           
      }
    
      sort(P.begin(), P.end(), PAIR_BY_SECOND<int,int>);
    
      REP(i,L) {
        B[P[i].ST] = 1;
      }
    
      /*
      cout << "TIME = " << time << endl;
      REPS(i,P) {
        cout << "(" << P[i].ST << "," << P[i].ND << ") ";
      } cout << endl;
      */

      while (star < N) {
        if (B[star] == 1) {
          time += D[star+1];
          star++;
        } else { 
          time += D[star+1] * 2;
          star++;
        }
      }    
      
    }
    
    solution:
    printf("Case #%d: ",testcase+1);
    cout << time << endl;
  }

  return 0;
}