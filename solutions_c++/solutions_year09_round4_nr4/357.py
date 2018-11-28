#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;

string filename = "D-small-attempt0";


struct ST
{
   ST(int rr, int xx, int yy)
   {
      r = rr;
      x = xx;
      y = yy;
   }
   int r, x, y;
};

int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	REP(t, T)
	{
      int n;
      cin>>n;
      vector<ST> v;
      REP(i, n)
      {
         int x, y, r;   
         cin>>x>>y>>r;
         v.pb(ST(r, x, y));
      }

      double res;

      if (n == 1)
      {
         res = v[0].r;
      }
      else if (n == 2)
      {
         res = MAX(v[0].r, v[1].r);
      }
      else
      {
         res = 1e10;
         REP(i, n)
         {
            double r1 = v[i].r;
            int i1 = (i + 1)%n;
            int i2 = (i + 2)%n;
            double dx1 = v[i1].x, dy1 = v[i1].y, dx2 = v[i2].x, dy2 = v[i2].y;
            double dist = sqrt((dx1-dx2)*(dx1-dx2) + (dy1-dy2)*(dy1-dy2));
            double r2 = (dist + v[i1].r + v[i2].r)/2.0;
            if (r2 > r1)
               r1 = r2;
            res = MIN(r1, res);
         }
      }

      cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}