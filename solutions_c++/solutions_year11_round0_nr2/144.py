#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;
typedef vector<int> VI;
typedef vector<string> VS;
#define REP(i,n) for(int _n=n, i=0;i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define PB push_back

string C[100], D[100], S;
int start, cL, dL, sL;

char getC(char c1, char c2) {
  REP(i,cL) {
    string& s=C[i];
    if(s[0]==c1 && s[1]==c2) return s[2];
    if(s[0]==c2 && s[1]==c1) return s[2];
  }
  return ' ';
}

bool getD(char c1, char c2) {
  REP(i,dL) {
    string& s=D[i];
    if(s[0]==c1 && s[1]==c2) return true;
    if(s[0]==c2 && s[1]==c1) return true;
  }
  return false;
}

int main() {
  int Ts;
  cin>>Ts;
  FOR(cs, 1, Ts) {
    cin>>cL; REP(i,cL) cin>>C[i];
    cin>>dL; REP(i,dL) cin>>D[i];
    cin>>sL; cin>>S;
    start = 0;
    REP(i, sL) {
      if (i == start) continue;
      char T = getC(S[i], S[i-1]);
      if (T != ' ') {
        S[i-1]=' '; S[i]=T;
      } else {
        FOR(j, start, i-1) {
          if (getD(S[j],S[i])) {
            start=i+1;break;
          }
        }
      }
    }
    cout << "Case #" << cs << ": [";
    int f=0;
    FOR(i, start, sL-1) if (S[i]!=' ') {
      if(f) cout<<", "; f=1;
      cout<<S[i];
    }
    cout<<"]"<<endl;
  }
  return 0;
}
