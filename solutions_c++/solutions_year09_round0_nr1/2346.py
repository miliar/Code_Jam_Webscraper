#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#include <queue>

using namespace std;

typedef long long int64;

#define pii pair <int,int>
#define mp make_pair 
#define fs first
#define sc second
#define pb push_back
#define all(a) a.begin(),a.end()
#define rz(a) resize(a)
#define sz(a) (int)a.size()
#define len(a) (int)a.length()
#define forn0(i, n) for (int i=0; i<(int)n; i++)
#define forn1(i, n) for (int i=1; i<=(int)n; i++)
#define ford0(i, n) for (int i=(int)n-1; i>=0; i--)
#define ford1(i, n) for (int i=(int)n; i>=1; i--)
#define forlr(i, l, r) for (int i=(int)l; i<=(int)r; i++)               
#define forrl(i, r, l) for (int i=(int)r; i>=(int)l; i--) 
                                                   
const int INF = (int)1e+8;
const double EPS = 1e-9;
const double PI = 3.1415926535897932384626433832795;
const int NMAX = 101;   

int l,d,n,ans;
vector <string> a;
vector <vector < char> > b;

bool prove ( string s, int pos )
{
 forn0 (i, sz(b[pos]))
  if (b[pos][i] == s[pos])
   return true;
 return false;
}

int main ()
{
 freopen ("input.txt","r",stdin);
 freopen ("output.txt","w",stdout);
 
 scanf ("%d%d%d", &l,&d,&n);  
 forn0 (i, d)
 {
  string s;
  cin >> s;
  a.pb (s);
 }
 forn1 (test, n)
 {
  printf ("Case #%d: ", test);
  b.clear ();
  b.resize (l);
  int cur = 0;
  string s;
  cin >> s;
  forn0 (i, len(s))
  {
   if (s[i] != '(')
    b[cur].pb (s[i]);
   else
   {
    forlr (j, i+1, len(s)-1)
     if (s[j] == ')')
     {
      i = j;
      break;
     }
     else b[cur].pb (s[j]);
   }
   cur++;
  }
  ans = 0;
  forn0 (i, sz(a))
  {
   bool good = true;
   forn0 (j, l)
    if (!prove (a[i],j))
    {
     good = false;
     break;
    }
   if (good)
    ans++;
   } 
  printf ("%d", ans);
  printf ("\n");            
 }

 return 0;
}
