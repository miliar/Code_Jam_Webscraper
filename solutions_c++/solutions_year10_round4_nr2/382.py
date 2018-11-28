#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

const int DBG = 0, INF = int(7e8);

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

const int MAXN = 1500;

int P, c;

int V[MAXN], L[MAXN], R[MAXN];

void readPrices() {

    c = 0;

    FORD(j,P - 1, 0) {

      int k = (1 << j);

      int b = c - (1 << (j + 1));

      //cout << "YO " << k << endl;

      REP(i,k) {
  
        int a;

        scanf("%d", &a);

        V[c] = a;
        if (j == P - 1) 
          L[c] = R[c] = -1;
        else {
          L[c] = b;
          R[c] = L[c] + 1;
          b += 2;
          //cout << c << " " << L[c] << " " << R[c] << endl;
        }
        ++c;

      }

    }
    --c;
}

int walk(int cur, int left, int right, int bal, VI &M) {
  //cout << left << " " << right << " " << bal << " " << cur <<  endl;
  //assert(left < right);

  if (left + 1 == right) { // first round

    if (M[left] + bal < 0 || M[right] + bal < 0) 
      return INF;
    if (M[left] + bal == 0 || M[right] + bal == 0) {
      //cout << "KROWA " << left << " " << right << " " << cur << endl;
      return V[cur];
    }
    return 0;

  }

  else {//cout << "HOP " << left << " " << right << endl;

    int res = V[cur] + walk(L[cur], left,left +  (right - left) / 2, bal, M) + walk(R[cur], left + (right - left) / 2 + 1, right, bal, M);
    int res2;
    FOR(i,left,right)
      if (M[i] + bal <= 0) 
        return res;
    res2 = walk(L[cur], left, left + (right - left) / 2, bal - 1,M) + walk(R[cur], left + (right - left) / 2 + 1,right,  bal - 1, M);
    if (res > INF)
      res = INF;
    if (res2 > INF)
      res2 = INF;
    //cout << left << " " << right << " " << res << " " << res2 << endl;
    return min(res, res2);    

  }
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;

  scanf("%d", &T);

  REP(q,T) {



    scanf("%d", &P);

    VI M((1 << P));

    REP(i,(1 << P))
      scanf("%d", &M[i]);

    readPrices();

    int res = walk(c, 0, (1 << P) - 1, 0, M);    

    printf("Case #%d: %d\n", q + 1, res);

    //return 0;

  }

  return 0;
}
