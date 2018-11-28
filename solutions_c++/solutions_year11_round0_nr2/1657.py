#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

deque<char> S;
int N,D,C,TT;
set<pair<char,char> > wrong;
map<pair<char,char>,char > combine;

void out(int cs){
  cout << "Case #" << cs << ": [";
  int n = 0;
  while(!S.empty()){
    if (n == 0){ cout << S.back(); }
    else{ cout << ", " << S.back(); }
    n++;
    S.pop_back();
  }
  cout << "]" << endl;
}

int main(){
  cin >> TT;
  FOR(tt,TT){
    wrong.clear();
    while(!S.empty()) S.pop_front();
    combine.clear();
    cin >> C;
    FOR(c,C){
      string s1;
      cin >> s1;
      combine.insert( MP( MP(s1[0],s1[1]),s1[2]) );
      combine.insert( MP( MP(s1[1],s1[0]),s1[2]) );
    }
    cin >> D;
    FOR(d,D){
      string s1;
      cin >> s1;
      wrong.insert(MP(s1[0],s1[1]));
      wrong.insert(MP(s1[1],s1[0]));
    }
    cin >> N;
    string vstup;
    cin >> vstup;
    FOR(i,N){
      char vkladam = vstup[i];
      //nemoze byt reduced?
      while(!S.empty()){
        if ( combine.find(MP(vkladam,S.front())) != combine.end()){
          vkladam = combine[MP(vkladam,S.front())];
          S.pop_front();
        }else{
          break;
        }
      }
      int cistim = 0;
      for(char a='A';a<='Z';a++)if (wrong.find(MP(vkladam,a))!=wrong.end()){
        for(int i=0;i<S.size();i++){
          if (S[i] == a) cistim = 1;
        }
      }
      if (cistim == 0){ S.push_front(vkladam); }
      else{ while(!S.empty()) S.pop_front(); }
    }
    out(tt+1);
  }
}
