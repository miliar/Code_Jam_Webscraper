#define TASKNAME "text"

#include <cstdio>
#include <iostream>

#include <cmath>
#include <algorithm>
#include <functional>

#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>

#include <ctime>
#include <cassert>

#include <map>
#include <set>
#include <vector>
 
#define EPS 1e-9
#define INF int(1e9)
#define INFLONG (long long)(1e18)
#define sqr(a) ((a) * (a))
#define abs(a) (((a) < 0) ? -(a) : (a))
#define sz(a) (int)a.size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define fst first
#define snd second
#define y1 osrughosduvgarligybakrybrogvba
#define y0 aosfigdalrowgyalsouvgrlvygalri
#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#ifdef WIN32
  #define I64d "%I64d"
#else
  #define I64d "%lld"
#endif
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <ll> vl;
typedef vector <vl> vvl; 
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef vector <pii> vpii;

const int MaxN = 30;

int ten[MaxN];
map <pii, int> was; 
         
inline int calc_digits(int n)
{
  int res = 0;
  while (n)
    ++res, n /= 10;
  return res;
}

int main()
{
  #ifdef LocalHost
    freopen(TASKNAME".in", "r", stdin);
    freopen(TASKNAME".out", "w", stdout);
  #endif  
  int test;
  ten[0] = 1;
  for (int i = 1; i <= 9; i++)
    ten[i] = ten[i - 1] * 10;
  scanf("%d", &test);
  for (int t = 1; t <= test; t++)
  {
    was.clear();
    int l, r;
    scanf("%d%d", &l, &r);
    int digits = calc_digits(l);

    int answer = 0;
    for (int i = l; i < r; i++)
    {
      int num = i;
      int now = 0;
      int st = 1;
      for (int j = 1; j < digits; j++)
      {
        now += st * (num % 10);
        num /= 10;  	
        st *= 10;
        int number = now * ten[digits - j] + num;
        if (number > i && number <= r && !was[mp(i, number)])
          ++answer;
        was[mp(i, number)] = 1;
      }
    }
    printf("Case #%d: %d\n", t, answer);
  }            
  return 0;
}
