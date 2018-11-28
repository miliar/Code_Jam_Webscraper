#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

typedef long long LL;

typedef vector<LL> VLL;


#define For(i,n) for(int i=0;i<(n);++i)
#define Forfrom(i,fr,n) for(int i=(fr);i<(n);++i)

int rec(vector<int> &v, int i) {
  //  cerr << i << "--" << endl;
  if (i == v[i]) return i;
  else {
    int k = rec(v, v[i]);
    v[i] = k;
    return k;
  }
}

int join(vector<int> &v, int i, int j) {
  if (j>=v.size() or i>=v.size()) {
    cerr << i << " " << j << endl;
  }
  if (v[i]==i and v[j]==j) {
    if (i<j) {v[j]=v[i]; return i;}
    else {v[i]=v[j]; return j;}
  }
  else {
    int k;
    if (v[j]!=j) k = join(v, i, v[j]);
    else k = join(v, j, v[i]);
    
    v[i] = v[j] = k;
    return k;
  }
}

int main() {
  int n;
  cin >> n;

  VLL primes;
  LL upto = LL(sqrt(2e12));

  primes.push_back(2);
  primes.push_back(3);
  Forfrom(i, 5, upto) {
    int j = 0;
    while (j<primes.size() and i%primes[j]) ++j;
    if (j==primes.size()) primes.push_back(i);
    //cerr << i << endl;
  }

  For(c, n) {
    cout << "Case #" << (c+1) << ": ";
    LL A, B, P;

    cin >> A >> B >> P;
    LL dist = B-A;
    vector<int> v(dist+1);
    For(i, dist+1) v[i] = i;

    For(j, primes.size()) {
      if (primes[j]<P) continue;
      if (primes[j]>B) break;

      int p = primes[j];
      LL x = (A/p)*p;
      if (x<A) x+=p;

      x+=p;
      while (x<=B) {
	join(v, x-p-A, x-A);
	x+=p;
      }
    }

    int num = 0;
    vector<bool> count(dist+1, false);
    For(i, dist+1) {
      int res = rec(v, i);
      //cerr << "return " << res << endl;
      if (!count[res]) {
	count[res] = true;
	++num;
	//	cerr << res << endl;
      }
    }

    cout << num << endl;
  }
}
