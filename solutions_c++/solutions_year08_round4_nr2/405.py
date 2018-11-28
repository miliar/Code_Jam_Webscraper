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
#include <list>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}

void e_euclid(int a, int b, int &x, int &y, int &d)
{
  int q, r, x1, x2, y1, y2;

  if (b == 0)
  {
    d = a, x = 1, y = 0;
    return;
  }
  x2 = 1, x1 = 0, y2 = 0, y1 = 1;
  while (b > 0) 
  {
    q = a / b, r = a - q * b;
    x = x2 - q * x1, y = y2 - q * y1;
    a = b, b = r;
    x2 = x1, x1 = x, y2 = y1, y1 = y;
  }
  d = a, x = x2, y = y2;
}


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	REP(test, T)
	{
		long long n, m, A;
		cin>>n>>m>>A;

		int rx1 = -1, ry1 = -1, rx2 = -1, ry2 = -1, rx3 = -1, ry3 = -1;

		bool fl = false;
		
		REP(x2, n+1)
			REP(y2, m+1)
				REP(x3, n + 1)
					REP(y3, m + 1)
		{
			if (abs(x2*y3 - y2*x3) == A)
			{
				fl = true;
				rx1 = 0; ry1 = 0; rx2 = x2; rx3 = x3; ry2 = y2; ry3 = y3;
			}
		}

		int res = 0;

		cout<<"Case #"<<test+1<<": ";
		if (fl)
			cout<<rx1<<" "<<ry1<<" "<<rx2<<" "<<ry2<<" "<<rx3<<" "<<ry3<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}
