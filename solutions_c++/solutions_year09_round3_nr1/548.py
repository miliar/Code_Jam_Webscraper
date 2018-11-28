#include <iostream>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>

#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cstring>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)
#define FORC(i,b,e,c) for(int i=(int)(b);i<(int)(e)&&(c);i++)
#define ALL(c) (c).begin(), (c).end()
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef vector<string> vstring;
typedef vector<double> vdouble;

template<class T>void pp(T v,int n){ REP(i,n)cout<<v[i]<< ' ' ; cout << endl;}
template<class T>void pp(T v){ EACH(it,v) cout << *it << ' ' ; cout << endl; }
template<class T>T& ls(T& a,T b){ if(b<a) a=b; return a;}
template<class T>T& gs(T& a,T b){ if(b>a) a=b; return a;}

int base(string s){
  sort(ALL(s));
  return unique(ALL(s))-s.begin();
}

int main(){
  int C; cin >> C;
  string s; getline(cin,s);

  REP(CC,C){
    getline(cin,s);

    int b=max(2,base(s));

    map<char,int> m;
    int cnt=2;
    m[s[0]]=1;
    FOR(i,1,s.length()) if(!m.count(s[i])){
      if(m.size()==1) m[s[i]]=0;
      else m[s[i]]=cnt++;
    }
    
    // EACH(it,m){ cout << it->first << ' ' << it->second << endl;}


    long long result=0;
    long long d=1;
    reverse(ALL(s));
    REP(i,s.length()){
      result+=d*m[s[i]];
      d*=b;
    }

    printf("Case #%d: %lld\n" , CC+1, result);
  }
}
