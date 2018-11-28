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

template <class T> T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
template <class T> string t2s(T x) {ostringstream o; o << x; return o.str();}

#endif

  vector<string> split (string s, string del = " ") { vector<string> res;
    int ss = s.size(), sdel = del.size();
    for (int p = 0, q; p < ss; p = q+sdel) {
      if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
      if (q-p>0) res.push_back(s.substr(p,q-p));
    } return res;
  }

int T, N;
string line;

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);
  
  scanf("%d\n",&T);
  FORU(testcase,0,T) {   
    scanf("%d ",&N); getline(cin, line);    
    vs data = split(line," ");
    int time = 0, bp = 1, bf = 0, op = 1, of = 0;
    REPS(i,data) {
      char r = s2t<char>(data[i++]);
      int mv = s2t<int>(data[i]);
      
      //cout << r << " " << mv << endl;
      
      switch (r) {
         case 'O': {
           int mt = abs(mv - op);
           if (mt <= of) {
             time += 1;
             //cout << "OO+" << 1 << endl;
             of = 0;
             bf = 1;
           } else {             
             time += (mt - of) + 1;
             //cout << "O+" << mt-of+1 << endl;
             bf += (mt - of) + 1;
             of = 0;
           }
           op = mv;
           break;
         }
         case 'B': {
           int mt = abs(mv - bp);
           if (mt <= bf) {
             time += 1; 
             //cout << "BB+" << 1 << endl;
             bf = 0;
             of = 1;
           } else {             
             time += (mt - bf) + 1;
             //cout << "B+" << mt-bf+1 << endl;
             of += (mt - bf) + 1;
             bf = 0;
           }
           bp = mv;                 
           break;
         }
      }
    }
    printf("Case #%d: %d\n",testcase+1,time);
  }

  return 0;
}