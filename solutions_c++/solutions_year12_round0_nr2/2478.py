#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define fs x
#define sc y
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define all(a) (a).begin(), (a).end()
#define sz(a) ((int)a.size())
#define TASKNAME ""

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long ll;
typedef long double ld;

int T, N, S, p;
#define SZ 200
int t[SZ];
int d[SZ][SZ];

int main() {
  
  scanf("%d", &T);
  cerr << T << endl;
  for (int test = 1; test <= T; test++) {
    scanf("%d %d %d", &N, &S, &p);
    for (int i = 0; i < N; i++) {
      scanf("%d", &t[i]);
    }
    memset(d, -1, sizeof(d));
    d[0][0] = 0;
    for (int done = 0; done < N; done++) {
      for (int k = 0; k <= done; k++) {
        if (d[done][k] == -1) continue;
        d[done + 1][k] = max(d[done + 1][k], d[done][k] + ((t[done] + 2) / 3 >= p));
        if (t[done] >= 2) {
          d[done + 1][k + 1] = max(d[done + 1][k + 1], d[done][k] + ((t[done] - 2) / 3 + 2 >= p));
        }
      }
    }
    int res = d[N][S];
    printf("Case #%d: %d\n", test, res);
  }

 	return 0;
}


