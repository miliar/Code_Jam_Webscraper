#include <iostream>
#include <fstream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <complex>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define EACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define FOR(i,k,n) for (int i=(k);i<(int)(n);i++)
#define FEQ(i,k,n) for(int i=(k);i<=(int)(n);i++)
typedef long long ll;
typedef complex<double> P;

int main()
{
  bool base[26];memset(base,0,sizeof(base));
  base['Q'] = base['W'] = base['E'] = base['R'] = base['A'] = base['S'] = base['D'] = base['F'] = true;
  int tc;cin>>tc;
  for(int t=1;t<=tc;t++){
    int c,d,n;
    string elem;
    char compose[150][150];
    bool oppose[150][150];
    memset(compose,0,sizeof(compose));
    memset(oppose,0,sizeof(oppose));
    cin>>c;
    REP(i,c){
      string s;cin>>s;
      compose[s[0]][s[1]] = compose[s[1]][s[0]] = s[2];
    }
    cin>>d;
    REP(i,d){
      string s;cin>>s;
      oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = true;
    }
    cin>>n>>elem;
    vector<char> ret;
    REP(i,n){
      if (ret.empty()) ret.push_back(elem[i]);
      else {
        if (compose[elem[i]][ret[ret.size()-1]] != 0){
          ret[ret.size()-1] = compose[elem[i]][ret[ret.size()-1]];
          goto NEXT;
        }
        REP(j,ret.size()){
          if (oppose[elem[i]][ret[j]]){
            ret.clear();
            goto NEXT;
          }
        }
        ret.push_back(elem[i]);
      NEXT:;
      }
    }
    printf("Case #%d: [",t);
    REP(i,ret.size()){
      putchar(ret[i]);
      if (i != ret.size() - 1) printf(", ");
    }
    puts("]");
  }
  return 0;
}

