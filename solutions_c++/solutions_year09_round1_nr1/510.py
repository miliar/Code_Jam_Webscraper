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

int n;
vector <int> base;
 
int main ()
{
 freopen ("input.txt","r",stdin);
 freopen ("output.txt","w",stdout);
 
 scanf ("%d\n", &n);  
 forn1 (test, n)
 {
  printf ("Case #%d: ", test);
  string s;
  getline (cin, s);
  base.clear ();
  int pos = s.find (' ',0);
  while (pos != -1)
  {
   string ss = s.substr (0, pos);
   s.erase (0, pos+1);
   base.pb (atoi(ss.c_str()));
   pos = s.find (' ', 0);
  }
  base.pb (atoi(s.c_str()));
  forlr (i, 2, 1000000)
  {
   bool f = true;
   forn0 (j, sz(base))
   {
    int cur = i;
    int osn = base[j];
    forn1 (i, 100)
    {
     int sum = 0;
     while (cur > 0)
     {
      sum += (cur%osn) * (cur%osn);
      cur /= osn;
     }
     cur = sum;
    }
    if (cur != 1)
    {
     f = false;
     break;
    }
   }
   if (f)
   {
    printf ("%d", i); 
    break;
   }
  }

  printf ("\n");            
 }

 return 0;
}
