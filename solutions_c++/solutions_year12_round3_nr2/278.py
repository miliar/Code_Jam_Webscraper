#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

ld dist;
int points;
int numacc;

vector < ld > t;
vector < ld > pos;

ld distTraveled(ld time, ld acc, ld initial) {
  return time * (initial + 0.5 * acc * time);
}

ld timeTaken(ld dd, ld acc, ld initial) {
  ld mn = 0.0;
  ld mx = 999999999.0;
  while(mx > mn + 0.000000000001) {
    ld md = (mn + mx) / 2;
    if(distTraveled(md, acc, initial) >= dd) {
      mx = md;
    } else {
      mn = md;
    }
  }
  return mx;
}

ld catchup(ld speed, ld p, ld acc) {
  ld mn = 0.0;
  ld mx = 99999999.0;
  while(mx > mn + 0.0000000000001) {
    ld md = (mn + mx) / 2;
    if(p + speed * md <= distTraveled(md, acc, 0.0)) {
      mx = md;
    } else {
      mn = md;
    }
  }
  return mx;
}

ld find(ld acc) {
  assert(t.size() <= 2);
  if(pos[0] >= dist) return timeTaken(dist, acc, 0.0);
  assert(t.size() == 2);
  ld speed = (pos[1] - pos[0]) / (t[1] - t[0]);
  ld when = catchup(speed, pos[0], acc);
  ld dd = distTraveled(when, acc, 0.0);
  if(dd >= dist) return timeTaken(dist, acc, 0.0);
  return when + (dist - dd) / speed;
}

int main()
{
  int tests;
  cin >> tests;
  for(int tt = 1; tt <= tests; tt++) {
    t.clear(); pos.clear();
    cin >> dist >> points >> numacc;
    FOR(i, points) {
      ld ti, po;
      cin >> ti >> po;
      t.pb(ti); pos.pb(po);
    }
    cout << "Case #" << tt << ":" << endl;
    cout.precision(10);
    FOR(i, numacc) {
      ld a;
      cin >> a;
      cout << find(a) << endl;
    }
  }
  return 0;
}
