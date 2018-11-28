#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <complex>
using namespace std;

#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define REPD(i,n) for (int i = n-1; i >= 0; --i)
#define FOR(i,p,k) for (int i = p; i <= (int)(k); ++i)
#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) x.begin(), x.end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) std::cout<<*it<<' '; std::cout<<std::endl; }

bool check(int n, int base) {
  set<int> memo;
  while (true) {
    int sum = 0;
    while (n) {
      int r = n % base;
      sum += r*r;
      n /= base;
    }
    if (sum == 1) return true;
    else n = sum;
    if (memo.count(n)) return false;
    else memo.insert(n);
  }
}


int main() {
  int T; cin>>T;
  string str;
  getline(cin,str);
  for (int tc = 1; tc <= T; tc++) {
    getline(cin,str);
    istringstream is(str);
    vector<int> data;
    int tmp;
    while (is>>tmp) {
      data.push_back(tmp);
    }
    //cerr<<"ok"<<data.size()<<endl;
    for (int x = 2;; x++) {
      bool ok = true;
      for (int i = 0; i < data.size(); i++) {
	ok &= check(x,data[i]);
      }
      if (ok) {
	cout<<"Case #"<<tc<<": "<<x<<endl;
	break;
      }
    }
  }
  return 0;
}
