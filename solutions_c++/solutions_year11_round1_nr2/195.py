#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
#define ALL(a) (a).begin(),(a).end()
typedef long long LL;
#define CR clear
#define PB push_back
#define VR vector
#define forE(elem,v)  for(__typeof__(v.begin()) _it = v.begin(); _it != v.end();++_it) for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) :_it ) for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1)
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
typedef vector<string> VRS;
// end insert defines

struct Ht
{
  string key;
  int next;
  Ht() {}
  Ht(string _key, int _next) {key = _key, next = _next;}
  friend bool operator < (const Ht &l, const Ht &r)
  {
    return l.key < r.key;
  }
};

int n, gq;
VRS words;
string l;
VR<Ht> ht[26];
//VR<bool> ext[26];
VR<int> loc[26];

void pre_set()
{
  Rep(i, 26) ht[i].CR();
  forE(w, words) {
    string ts = w;
    //    ext.assign(26, false);
    Rep(i, 26) loc[i].CR();
    Rep(i, w.size()) {
      loc[w[i] - 'a'].PB(i);
    }
    int next = 26;
    for (int i = 25; i >= 0; i--) {
      if (loc[l[i] - 'a'].size()) {
        forE(loci, loc[l[i] - 'a']) ts[loci] = '_';
        next = i;
      }
      ht[i].PB(Ht(ts, next));
    }
  }
}

bool ht_cmp(const Ht &l, const Ht &r)
{
  if (l.key != r.key) return l.key < r.key;
  return l.next < r.next;
}

VRS anss;

void work2()
{
  pre_set();
  Rep(i, 26) sort(ALL(ht[i]), ht_cmp);
  int maxi = -1;
  string ans;
  forE(w, words) {
    //  cout << w << endl;
    int nsum = 0;
    string ts = w;
    forE(tsi, ts) tsi = '_';
    Rep(i, 26) loc[i].CR();
    Rep(i, w.size()) {
      loc[w[i] - 'a'].PB(i);
    }
    int cc = 0;
    Rep(i, 26) {
      int j = lower_bound(ALL(ht[i]), Ht(ts, 0)) - ht[i].begin();
      if (!(j < ht[i].size() && ht[i][j].key == ts)) continue;
      if (ht[i][j].next != i) continue;
      else {
        if (loc[l[i] - 'a'].size())
          forE(loci, loc[l[i] - 'a']) ts[loci] = l[i], cc++;
        else nsum++;
      }
      if (cc == w.size()) break;
    }
    if (nsum > maxi) {
      maxi = nsum;
      ans = w;
    }
  }
  anss.PB(ans);
}
  
void work()
{
  anss.CR();
  Rep(qid, gq) {
    cin >> l;
    work2();
  }
  Rep(i, anss.size()) {
    if (i) cout << " ";
    cout << anss[i];
  }
  cout << endl;
}

void myin()
{
  cin >> n >> gq;
  words.resize(n);
  forE(w, words) cin >> w;
}

int main()
{
  int tests;
  cin >> tests;
  for (int Ca = 0; Ca < tests; Ca++) {
    cout << "Case #" << Ca + 1 << ": ";
    myin();
    work();
  }
  return 0;
}


