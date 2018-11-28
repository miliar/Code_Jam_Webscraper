#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <cassert>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

typedef pair<int,int> PII;
typedef vector<int> VI;


#define NUM 102

inline int get(int n, int j) {
  return (n & (1 << j)) >> j;
}

inline void set(int &n, int j) {
  n |= (1 << j);
}

inline int num(int n) {
  int res = 0;
  For(i,10) if (get(n, i)) ++res;
  return res;
}

inline bool good(int a) {
  return (a & (a << 1)) == 0;
}

inline bool comp(int a, int b) {
  return (a & b) == 0;
}

void debug(int i) {
  For(j,10) cout << get(i,j);
  cout << endl;
}

inline bool compinf(int a, int b) {
  if ( ((a & (b << 1)) == 0) and (((a << 1) & b) == 0)) {
    //    cerr << "!!!!!!!"; debug(a);
    //   debug(b);
    return 1;
  }
  else {
    return 0;
  }
}



void solveit() {
  int M, N;
  cin >> M >> N;
  vector<vector<int> > v(M, vector<int>(1024, -1));
  
  vector<int> oc(M);
  For(i,M) For(j,N) {
    char c;
    cin >> c;
    if (c=='x') set(oc[i],j);
  }

  For(i,M) Forf(j,N,10) set(oc[i],j);

  //  For(i,M) debug(oc[i]);
  
  For(i, 1024) if (good(i) and comp(i, oc[0])) {
    v[0][i] = num(i);
    //    cerr << "vist " << num(i) << " ";
    //    debug(i);
  }

  for(int i=1; i<M; ++i) {
    For(conf, 1024) {
      if (not good(conf) or not comp(conf, oc[i])) continue;
      int count = num(conf);

      int best = count;
      for(int j = 0;j<1024;++j) {
	if (v[i-1][j]>0 and compinf(conf, j)) {
	  //cerr << v[i-1][j] << "---" << endl;
	  best = max(best, count + v[i-1][j]);
	}
      }
      //      cerr << i << " " << best << " ";
      //debug(conf);
      v[i][conf] = best;
    }
  }
 
  int verybest = 0;
  For(j, 1024) verybest = max(verybest, v[M-1][j]);

  cout << verybest << endl;
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
