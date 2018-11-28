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

int n,d[600][30];
 
int main ()
{
 freopen ("input.txt","r",stdin);
 freopen ("output.txt","w",stdout);
 
 scanf ("%d\n", &n);
 string pat = " welcome to code jam";   
 forn1 (test, n)
 {
  printf ("Case #%d: ", test);
  string s;
  getline (cin,s);
  s = " " + s;
  forn0 (i, 600)
   forn0 (j, 30)
    d[i][j] = 0;
  d[0][0] = 1;
  forn0 (i, len(s)-1)
   forn0 (j, len(pat)-1) 
    if (d[i][j] >= 1)
	{
	 forlr (x, i+1, len(s)-1)
      if ((s[i] == pat[j]) && (s[x] == pat[j+1]))
      {
       d[x][j+1] += d[i][j];
       d[x][j+1] %= 10000;
      }
	}
 
  int ans = 0;
  forn0 (i, len(s))
  {
   ans += d[i][len(pat)-1];	
   ans %= 10000;
  }
  printf ("%04d", ans);
  printf ("\n");            
 }

 return 0;
}
