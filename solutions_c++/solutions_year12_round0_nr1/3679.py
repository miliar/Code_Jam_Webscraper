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

const int MaxN = 200;

char s[MaxN];
string str = "yhesocvxduiglbkrztnwjpfmaq";
                                        
int main()
{
  #ifdef LocalHost
    freopen(TASKNAME".in", "r", stdin);
    freopen(TASKNAME".out", "w", stdout);
  #endif  
  int test;
  scanf("%d\n", &test);
  for (int t = 1; t <= test; t++)
  {
    gets(s);
    //cout << s << '\n';
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    {
      if (s[i] == 32)
        continue;
      //s[i] = (s[i] == 'q' ? 0 : str[s[i] - 'a']);
      s[i] = str[s[i] - 'a'];
    }            
    printf("Case #%d: %s\n", t, s);
  }
  return 0;
}
