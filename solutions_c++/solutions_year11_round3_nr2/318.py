#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cassert>

#define eps 1e-9
#define inf int(1e9)
#define inflong __int64(1e18)
#define abs(a) (((a) < 0) ? -(a) : (a))
#define sqr(a) ((a) * (a))
#define taskname "a"
#define sz(a) (int)a.size()
#define mp make_pair
#define pb push_back
#define forn(i, x, y) for (int i = (x); i <= (y); i++)
#define ford(i, y, x) for (int i = (y); i >= (x); i--)
                       
using namespace std;

const int maxn = int(2e5);
const int maxnn = int(2e3);
const double pi = M_PI;

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vii;
typedef vector <bool> vb;
typedef vector <vb> vbb;
typedef vector <ll> vl;
typedef vector <vl> vll;

int T, n, c, l;
ll a[maxn * 10];
ll t;
ll d[maxn * 10], d1[maxn * 10], d2[maxn * 10];

bool les(ll a, ll b)
{
  return a > b;
}

int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  scanf("%d", &T);
  for (int i = 1; i <= T; i++)
  {
    printf("Case #%d: ", i);
    scanf("%d%I64d%d%d", &l, &t, &n, &c);
    for (int j = 0; j < c; j++)
    {
      scanf("%I64d", &a[j]);
      int k = 0;
      while (c * k + j < n)
      {
        d[c * k + j] = a[j];    
        k++;
      }
    }
    int now = 0;
    ll ttime = t;
    ll ans = 0;
    while (now < n)
    {
      if (d[now] * 2 <= ttime)
      {
        ttime -= d[now] * 2;
        ans += d[now] * 2; 
        now++;
      }
      else
        break;
    }
    if (now >= n)
    {
      cout << ans << '\n';
      continue;
    }
    int used = 0;
    if (ttime)
    {
      ll ans1, ans2;
      int used1, used2;
      int now1, now2;
      ll ttime1, ttime2;

      ttime1 = ttime2 = ttime;
      ans1 = ans2 = ans;
      used1 = used2 = used;
      now1 = now2 = now;
      for (int j = 0; j < n; j++)
        d1[j] = d2[j] = d[j];

      used1++;
      if (used1 <= l)    
        ans1 += d1[now1] + ttime1 / 2;
      else
        ans1 += d1[now1] * 2; 
      ttime1 = 0;
      now1++;
      sort(d1 + now1, d1 + n, les);
      while (now1 < n)
      {
        used1++;
        if (used1 <= l)
          ans1 += d1[now1];
        else
          ans1 += d1[now1] * 2;  
        now1++;
      }
      ttime2 = 0;
      ans2 += d[now2] * 2;
      now2++;
      sort(d2 + now2, d2 + n, les);
      while (now2 < n)
      {
        used2++;
        if (used2 <= l)
          ans2 += d2[now2];
        else
          ans2 += d2[now2] * 2;  
        now2++;
      }
      cout << min(ans1, ans2) << '\n';
      continue;
    }
    else
    {
      sort(d + now, d + n, les);
      while (now < n)
      {
        if (!ttime)
        {
          used++;
          if (used <= l)
            ans += d[now];
          else
            ans += d[now] * 2;
          now++;
        }
      }
      cout << ans << '\n';
      continue;
    }
  }
  return 0;
}


