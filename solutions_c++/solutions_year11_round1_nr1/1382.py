
#include <algorithm> 
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <queue>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
#include <stdio.h>

using namespace std;

#include <ext/hash_set>
#include <ext/hash_map>

//using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
/*
 #define dot(a,b) ((conj(a)*(b)).X)
 #define X real()
 #define Y imag()
 #define length(V) (hypot((V).X,(V).Y))
 #define vect(a,b) ((b)-(a))
 #define cross(a,b) ((conj(a)*(b)).imag())
 #define normalize(v) ((v)/length(v))
 #define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
 #define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
 */
typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

inline int comp(const long double &a, const long double &b) {
  long double tt = a-b;
  if( tt < 0 )
    tt = -tt;
  if (tt < eps)
    return 0;
  return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int R, C;

inline bool val(const int &i, const int &j) {
  if (i < 0 || j < 0 || i >= R || j >= C)
    return false;
  return true;
}

int N;

#define SMALL
//#define LARGE

int main() {
  freopen("a.txt", "rt", stdin);
#ifdef SMALL
  freopen("A-small-0.in", "rt", stdin);
  freopen("A-small-0.out", "wt", stdout);
#endif
#ifdef LARGE
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
#endif

  cin >> N;
  int i, j, ii;
  long long n;
  int d;
  int g;
  int flag;
  for (int nn = 1; nn <= N; ++nn) {
    cin >> n >> d >> g;
    flag = 1;
    if(n < 100)
    {
      for(i = n; i >=1; i--)
      {
	if((i * d) % 100 == 0)
	{
	  flag = 0;
	  break;
	}
      }
    }
    if(n >= 100)
      flag = 1;


      if(flag == 0)
      {
	if(g == 100)
	{
	  if(d < 100)
	    cout<<"Case #"<< nn <<": Broken"<<endl;
	  else
	    cout<<"Case #"<< nn<<": Possible"<<endl;
	}
	else if(g == 0)
	{
	  if(d > 0)
	    cout<<"Case #"<< nn<<": Broken"<<endl;
	  else
	    cout<<"Case #"<<nn<<": Possible"<<endl;
	}
	else
    	cout<<"Case #"<<nn<<": Possible"<<endl;	  
	
      }
      else
	cout<<"Case #"<<nn<<": Broken"<<endl;
  }
/*
#ifdef SMALL
    cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
    cerr << nn << " of " << N << " is done." << endl;
#endif
*/
 
  return 0;
}
