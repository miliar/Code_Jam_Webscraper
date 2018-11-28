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

int T;
string line;

char COM[26][26];
bool OPP[26][26];

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);
  
  scanf("%d\n",&T);
  FORU(testcase,0,T) {   
    REP(i,26) REP(j,26) {
      COM[i][j] = '-';
      OPP[i][j] = false;
    }
    
    getline(cin, line);    
    vs data = split(line," ");
    int C = s2t<int>(data[0]);
    FORU(i,1,1+C) {
      string com = data[i]; 
      COM[com[0]-'A'][com[1]-'A'] = com[2];      
      COM[com[1]-'A'][com[0]-'A'] = com[2];
    }
    int D = s2t<int>(data[1+C]);
    FORU(i,1+C+1,1+C+1+D) {
      string com = data[i];
      OPP[com[0]-'A'][com[1]-'A'] = true;
      OPP[com[1]-'A'][com[0]-'A'] = true;
    }    
    int N = s2t<int>(data[1+C+1+D]);
    string spell =  data[1+C+1+D+1];
    
    vector<char> S;
    REPS(i,spell) {
      S.PB(spell[i]);
      int ss = S.size();
      if (ss > 1) {
        char c = COM[S[ss-2]-'A'][S[ss-1]-'A'];
        if (c != '-') {
          S.pop_back();
          S.pop_back();
          S.PB(c);
        } else {
          FORU(i,0,ss-1) {
            if (OPP[S[i]-'A'][S[ss-1]-'A']) {
              S.clear();
            }
          }        
        }
      }
    }
     
    printf("Case #%d: ",testcase+1);
    
    cout << "["; REPS(i,S) {
      if (i) cout << ", ";
      cout << S[i];
    } cout << "]" << endl;
  }

  return 0;
}