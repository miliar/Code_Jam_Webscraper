#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <queue>

using namespace std;

typedef long long huge;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef pair<int, int> pi;
typedef vector<pair<int, int> > vpi;

#define oo 0x3f3f3f3f
#define eps 1e-9
#define fn(_i, _n) for(int (_i) = 0; (_i) < (_n); (_i)++)
#define fi(_n) fn(i, (_n))
#define fj(_n) fn(j, (_n))
#define fk(_n) fn(k, (_n))
#define foreach(_x) for(typeof((_x).begin()) it = (_x).begin(); it != (_x).end(); it++)
#define pb(_x) push_back((_x))
#define sz(_x) ((int)(_x).size())
#define all(_x) (_x).begin(), (_x).end()
#define rall(_x) (_x).rbegin(), (_x).rend()
#define mp(_x, _y) make_pair((_x), (_y))
#define fill(_x, _y) memset((_x), (_y), sizeof(_x))
#define zero(_x) fill(_x, 0)
#define shl(_n) (1<<(_n))
#define lshl(_n) (1LL<<(_n))

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    int X,S,R,t,N;

    scanf("%d %d %d %d %d", &X,&S,&R,&t,&N);
    vpi c;

    fi(N)
    {
      int B, E, W;
      scanf("%d %d %d", &B, &E, &W);
      c.pb(mp(W, E-B));
      X -= (E-B);
    }
    c.pb(mp(0, X));
    sort(all(c));

    double r = 0.0;
    double t0 = (double)t;
    fi(N+1)
    {
      double s = (double)(c[i].second);
      double v = (double)(S+c[i].first);
      double vr = (double)(R+c[i].first);
      if (t0 > eps)
      {
        double s0 = min(s, t0*vr);
        double s1 = s-s0;
        double temp = s0/vr + s1/v;
        //printf("[%lf %lf %lf %lf %lf]", t0, s, s0, s1, temp);
        t0 -= temp;
        r += temp;
      }
      else r += s/v;
    }
    printf("Case #%d: %.10lf\n", caso, r);
  }

  return(0);
}

