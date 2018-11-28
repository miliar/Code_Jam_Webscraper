//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl; 
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

template <class T>
inline std::string to_string (const T& t)
{
  std::stringstream ss;
  ss << t;
  return ss.str();
}


string a,b;
int T;
int ss1,ss2;

set<pair<string,string> > myset;

inline bool leading_zero(string s) {
  return (s[0] == '0');
}

string r1,r2,res;

void count_recycle(string s) {
  for(int i = 1; i < SZ(s); i++) {
    r1=s.substr(0,i);
    r2=s.substr(i);
    res = r2+r1;
    //
    if(!leading_zero(res) && res < s && a <= res) { 
      myset.insert(pair<string,string>(res,s));
    }
  }
}
int main() {
  scanf("%d",&T);
  for(int t=1; t <= T; t++) {
    myset.clear();
    scanf("%d %d",&ss1,&ss2);
    a = to_string(ss1); 
    b = to_string(ss2);
    
    for(int i = ss1; i <= ss2; i++) {
      count_recycle(to_string(i));
    }
    printf("Case #%d: %d\n",t,SZ(myset));
  }
  
  return 0;
}
