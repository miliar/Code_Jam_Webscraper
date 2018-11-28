#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1E-9
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLR(c) memset(c, 0, sizeof(c))
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SSORT(c) stable_sort(ALL(c))
#define ZERO(i,v) (((i)<0)?(0):(v))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";
#define TCT template <class T>

typedef long long LL; typedef unsigned long long ULL; typedef long double LD;
typedef vector<int> vi; typedef vector<vi> vvi;
typedef vector<string> vs; typedef pair<int,int> pii;

const int INF = 2000000000; const LL INFLL = LL(INF) * LL(INF);

TCT bool OrdAsc (const T &a, const T &b) {return a < b;}
TCT bool OrdDes (const T &a, const T &b) {return a > b;}
TCT bool OrdXY (const T &a, const T &b) {if (a->x==b->x) RET a->y<b->y; RET a->x<b->x;}
TCT bool OrdYX (const T &a, const T &b) {if (a->y==b->y) RET a->x<b->x; RET a->y<b->y;}
TCT string t2s(T x) {ostringstream o; o << x; return o.str();}
TCT T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
TCT inline int size (const T&c) {return c.size();}

vs split (string s, string del = " ") { vs res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

int X[55];
int V[55];
int S[55];

void swapval (int i, int j) {
  int tmp;
  tmp = X[i]; X[i] = X[j]; X[j] = tmp;
  tmp = V[i]; V[i] = V[j]; V[j] = tmp;
  tmp = S[i]; S[i] = S[j]; S[j] = tmp;
}

int main() {

  int C;
  int N, K, B, T;
  string line;

  scanf("%d",&C); getline(cin, line);
  FORU(testcase,1,C) {
    scanf("%d %d %d %d\n",&N,&K,&B,&T);
    CLR(X); CLR(V); CLR(S);

    REP(i,N) { scanf("%d",&X[i]); }
    REP(i,N) { scanf("%d",&V[i]); }

    FORU(i,1,T) {
      //cout << "Time: " <<  i << endl;
      FORD(j,N-1,0) {
        //cout << j << endl;
        int c = j, v = V[j];
        while (c < N-1 && v) {
          if (X[c+1]-X[c] < v) {
            int tleft = T-i;

            if (X[c+1] + min(V[c+1],v) * tleft < B) {
              v -= X[c+1]-X[c];
              swapval(c,c+1); ++c;               
              X[c] = X[c-1];
              S[c] += 1;
            } else {
              v = 0;
              X[c] = X[c+1];
            }

          } else { X[c] += v; v -= v; }
        }

        if (c == N-1) { X[c] += v; }
      }
    }

    int cnt = 0;
    REP(i,N) {
      if (X[i] >= B) ++cnt;
    }

    printf("Case #%d: ",testcase);
    if (cnt < K) printf("IMPOSSIBLE\n");
    else {
      int used[55], res = 0; CLR(used);
      REP(i,K) {
        int sw = INF, swi = -1;
        REP(j,N) if (X[j] >= B && !used[j]) {
          if (S[j] < sw) {
            sw = S[j]; swi = j;
          }
        }
        used[swi] = 1;
        res += sw;
      }
      printf("%d\n",res);
    }
  }

  return 0;
}
