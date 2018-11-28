#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
typedef long long ll;
const int INF = 999999999;
 
int NA, NB, T;
pair<int, int> A[110];
pair<int, int> B[110];

bool Adone[110], Bdone[110];
int Arest, Brest;

int readtime() {
  int h, m;
  scanf("%d:%d", &h, &m);
  return h * 60 + m;
}

void goA(int);

void goB(int t) {
  if (Brest <= 0) return;
  rep (i, NB) {
    if (!Bdone[i] && t <= B[i].first) {
      //printf("goingB: %d\n", i);
      Bdone[i] = true;
      Brest--;

      goA(B[i].second + T);
      return;
    }
  }
}

void goA(int t) {
  if (Arest <= 0) return;
  rep (i, NA) {
    if (!Adone[i] && t <= A[i].first) {
      //printf("goingA: %d\n", i);
      Adone[i] = true;
      Arest--;

      goB(A[i].second + T);
      return;
    }
  }
}

vector<pair<int, int> > pa;

int main() {
  int N;
  scanf("%d", &N);

  rep (i, N) {
    scanf("%d", &T);
    scanf("%d%d", &NA, &NB);
    
    rep (j, NA) {
      A[j].first = readtime();
      A[j].second = readtime();
    }
    rep (j, NB) {
      B[j].first = readtime();
      B[j].second = readtime();
    }
    sort(A, A + NA);
    sort(B, B + NB);

    pa.clear();
    rep (j, NA) pa.pb(mp(A[j].first, j));
    rep (j, NB) pa.pb(mp(B[j].first, NA + j));

    memset(Adone, 0, sizeof(Adone));
    memset(Bdone, 0, sizeof(Bdone));
    
    Arest = NA;
    Brest = NB;
    
    sort(all(pa));

    int ansa = 0, ansb = 0;
    rep (j, pa.size()) {
      //printf("paowef %d\n", pa[j].second);
      if (pa[j].second >= NA) {
        int b = pa[j].second - NA;
        //printf("B? %d (%d)\n", b, Bdone[b]);
        if (!Bdone[b]) {
          //printf("b %d\n", b);
          goB(0);
          ansb++;
        }
      }
      else {
        int a = pa[j].second;
        if (!Adone[a]) {
          //printf("a %d\n", a);
          goA(0);
          ansa++;
        }
      }
    }
    //printf("%d\n", Bdone[1]);
    printf("Case #%d: %d %d\n", i + 1, ansa, ansb);
  }
}
