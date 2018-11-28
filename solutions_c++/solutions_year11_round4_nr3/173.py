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

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FOREACH(i,c) for(typeof(c.begin()) i=(c).begin();i!=(c).end();++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

void dump(map<int,int> m) {
  //for(map<int,int>::iterator it=m.begin();it!=m.end();it++) {
  FOREACH(it, m) {
    cout << "m[" << it->first << "]=" << it->second << endl;
  }
  cout << endl;
}

void dump(vector<int> v) {
  cout << "v{";
  REP(i, v.size()){
    cout << v[i] << " ";
  }
  cout << "}" << endl;
}

vector<int> primes;
int primes_max = 3; // primes <= primes_max are all found

void gen_primes() {
  primes.push_back(2);
  primes.push_back(3);
}

void gen_primes(unsigned max) {
  for(int i=MAX(primes_max, primes[primes.size()-1])+2;i<=max;i+=2) {
    bool OK=true;
    REP(j, primes.size()) {
      int p = primes[j];
      if( p*p>i ) break;
      if( i % p == 0 ) {
        OK=false;
        break;
      }
    }
    if(OK) {
      primes.push_back(i);
      //cout << i << " is prime" << endl;
    }
  }
  primes_max = max;
  if(primes_max % 2 ==0) primes_max--;
  //cout << "gen_prime " << max << " done" << endl;
}

bool is_prime(long long a) {
  if( a < primes_max ) {
    return find(primes.begin(), primes.end(), a) != primes.end();
  }
  int i = 0;
  while(1) {
    int p = primes[i];
    //cout << "trying " << p << endl;
    if( a % p == 0) {
      return false;
    } else {
      if(i==primes.size()-1) {
        if( p*p < a ) {
          gen_primes(((int)sqrt(a))*2);
        } else {
          return true;
        }
      }
      i++;
    }
  }
}

map<int,int> factorize(long long a) {
  map<int,int> ans;
  long long tmp=a;
  int i = 0;
  while(tmp!=1) {
    int p = primes[i];
    //cout << "trying " << p << endl;
    if( tmp % p == 0) {
      tmp /= p;
      //cout << "factor out " << p << endl;
      ans[p]++;
    } else {
      if(i==primes.size()-1) {
        if( p*p < tmp ) {
          gen_primes(((int)sqrt(tmp))*2);
        } else {
          break;
        }
      }
      i++;
    }
  }
  if(tmp!=1) {
    ans[tmp]++;
  }
  //dump(ans);
  return ans;
}

long long unfactorize(map<int,int> a) {
  long long ans = 1;
  FOREACH(it, a) {
    REP(j, it->second) {
      ans *= it->first;
    }
  }
  return ans;
}
  
int solve()
{
  int N;
  cin >> N;
  if(N==1) return 0;
  map<int,int> all;
  for(int i=2;i<=N;i++) {
    map<int,int> fac = factorize(i);
    //dump(fac);
    FOREACH(it, fac) {
      all[it->first] = MAX(it->second, all[it->first]);
    }
  }
  //dump(all);

  int callmax = 1;
  int callmin = 0;
  FOREACH(it, all) {
    callmax += it->second;
    if(it->second>0)
      callmin++;
  }

  return callmax-callmin;
}

int solvefast()
{
  long long N;
  cin >> N;
  if(N==1) return 0;

  gen_primes(((int)sqrt(N))*1.1+100);

  map<int,int> all;
  REP(i, primes.size()) {
    if(primes[i]*primes[i] > N) {
      break;
    } else {
      long long p = 1;
      int count = 0;
      while(p <= N) {
        p *= primes[i];
        count ++;
        //cout << "p=" << p << " count= " << count << endl;
      }
      count--;
      //cout << "count for " << primes[i] << " is " << count << endl;
      all[primes[i]] = count;
    }
  }
  //dump(all);

  int callmax = 1;
  int callmin = 0;
  FOREACH(it, all) {
    callmax += it->second;
    if(it->second>0)
      callmin++;
  }

  return callmax-callmin;
}

int main()
{
  int T;
  cin >> T;
  gen_primes();
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ": ";
    cout << solvefast();
    cout << endl;
  }
}
