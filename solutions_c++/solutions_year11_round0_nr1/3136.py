#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define p(a) cout << a << endl;
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define zero(a) memset(a, 0, sizeof(a))
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64

typedef vector<int> vint;

int main()
{
  int n;
  cin >> n;

  int cur[2];

  int t[2];
  int veces;
  char tipo;
  int boton;
  int R;

  cin.ignore();

  forn(_i,n)
  {
   cur[0] = cur[1] = 1;
   t[0]=t[1]=0;
   int secs = 0;

   cin >> veces;
   forn(i,veces)
   {
      cin >>  tipo >> boton;
      if(tipo == 'O') R=0; else R=1;

      int tiempo = abs(cur[R]-boton);
      if(secs < t[R]+tiempo) secs =t[R]+tiempo;
      cur[R] = boton;
      t[R] = secs+1;
      secs++;
   }
   cin.ignore();
   p("Case #"<<_i+1<<": "<<secs); 

    
  }
}
