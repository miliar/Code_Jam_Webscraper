#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for (a=(b); a<(c); ++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

typedef map<string,vi> msvi;

pii bestWord(const vs& D, const vi& words, string pat, string alph, int alph_i) {
  int i,j,k;
  //printf("%s\n", pat.c_str());
  //out(all(words));
  if (words.size() == 1) {
    return mp(0, words[0]);
  }
  for (; alph_i < alph.length(); alph_i++) {
    msvi m;
    //cout << "Guess " << alph[alph_i] << "?" << endl;
    bool match = false;
    for (j = 0; j < words.size(); j++) {
      string s(pat);
      for (k = 0; k < D[words[j]].length(); k++) {
        if (D[words[j]][k] == alph[alph_i]) {
          match = true;
          s[k] = alph[alph_i];
        }
      }
      m[s].pb(words[j]);
    }
    if (match) {
      //cout << "Yes." << endl;
      pii ans = mp(-1,-1);
      for (msvi::iterator it = m.begin(); it != m.end(); it++) {
        pii best = bestWord(D, it->second, it->first, alph, alph_i + 1);
        if (it->first == pat)
          best.first++;
        if (best.first > ans.first ||
            (best.first == ans.first && best.second < ans.second))
          ans = best;
      }
      return ans;
    }
  }
  throw -1;
}

int main() {
  int i, j, k, t, tt;
  tt = ni();
  for (t = 1; t <= tt; ++t) {
    printf("Case #%d:", t);
    
    int N = ni();
    int M = ni();
    vs D(N);
    for (i = 0; i < N; i++) {
      D[i] = string(ns());
    }
    for (i = 0; i < M; i++) {
      string alph(ns());
      
      msvi m;
      for (j = 0; j < N; j++) {
        string s(D[j].length(), '_');
        m[s].pb(j);
      }
      
      pii ans = mp(-1,-1);
      for (msvi::iterator it = m.begin(); it != m.end(); it++) {
        pii best = bestWord(D, it->second, it->first, alph, 0);
        if (best.first > ans.first ||
            (best.first == ans.first && best.second < ans.second))
          ans = best;
      }
      printf(" %s", D[ans.second].c_str());
    }
    printf("\n");
  }
  return 0;
}
