#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(long long i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

void dumpV(vector<long long> v) {
  cout << "v{";
  REP(i, v.size()){
    cout << v[i] << " ";
  }
  cout << "}" << endl;
}

void dumpM(map<long long,long long> m) {
  for(map<long long,long long>::iterator it=m.begin();it!=m.end();it++) {
    cout << "m[" << it->first << "]=" << it->second << endl;
  }
  cout << endl;
}

long long solve()
{
  long long L, N, C;
  long long t;
  cin >> L >> t >> N >> C;
  vector<long long> a(C);
  long long asum = 0;
  REP(i, C) {
    cin >> a[i];
    asum += a[i];
  }
  long long worst=((long long)(N/C))*asum;
  REP(i, N%C) {
    worst += a[i];
  }
  worst *= 2;
  //cout << "worst=" << worst << endl;
  if(t>=worst) return worst;
  if(L==0) return worst;
  map<long long, long long> cand;
  REP(i, C) {
    cand[a[i]] += N/C;
  }
  REP(i, N%C) {
    cand[a[i]]++;
  }
  //dumpM(cand);
  
  REP(i, C) {
    cand[a[i]] -= t/(2*asum);
    if(cand[a[i]]<0) cout << "ERR1" << endl;
  }
  long long res = t - (t/(2*asum)*(2*asum));
  long long cut = -1;
  REP(i, C) {
    if(res >= 2*a[i]) {
      res -= 2*a[i];
      cand[a[i]] -= 1;
      //cout << "remove " << a[i] << endl;
      if(cand[a[i]]<0) cout << "ERR2" << endl;
    } else {
      cut = i;
      break;
    }
  }
  if(cut <0)cout << "ERR3" << endl;
  if((res%2)!=0) cout << "ERR4";
  if(res > 0) {
    cand[a[cut]] -= 1;
    cand[a[cut]-res/2] += 1;
  }
  //dumpM(cand);
  long long save = 0;
  while(1) {
    if(cand.begin()==cand.end()) break;
    map<long long,long long>::iterator it=cand.end();
    it--;
    if(it->second==0) {
      cand.erase(it);
      continue;
    }
    long long max = it->first;
    long long count = MIN(L, it->second);
    //cout << "remove " << count << " from " << max << endl;
    L-=count;
    it->second -= count;
    save += count * max;
    
    if(L==0) break;
  }
  return worst - save;
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ": ";
    cout << solve();
    cout << endl;
  }
}
