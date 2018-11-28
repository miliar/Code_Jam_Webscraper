#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)

template<class T> T getAs(){ T v; std::cin >> v; return v; }
inline int getInt(){ return getAs<int>(); }

int main(){
  int C = getInt();

  REP(cc,C){
    int n = getInt();

    vector<int> t(n);
    vector<int> p(n);
    vector<int> z;

    REP(i,n){
      t[i] = getInt();
    }

    REP(i,n){
      p[i] = getInt();
      if(p[i] == 0) z.push_back(i);
    }

    vector<pair<int, pair<int, int> > > v;

    REP(i,n){
      if(p[i] != 0){
	v.push_back(make_pair(- t[i] * p[i], make_pair(t[i], i)));
      }
    }

    sort(v.begin(), v.end());

    printf("Case #%d:", cc + 1);
    REP(i,v.size()) printf(" %d", v[i].second.second);
    REP(i,z.size()) printf(" %d", z[i]);
    puts("");
  }
  
  return 0;
}
