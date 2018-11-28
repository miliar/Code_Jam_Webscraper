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

string filename = "A-large";

bool test(int x, int r)
{
   return x <= r;
}

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
      vector<int> v;
      string str;
      REP(i, n)
      {
         cin>>str;
         int x = 0;
         for (int i = 0; i < str.sz; i++)
            if (str[i] == '1')
               x = i;
         v.pb(x);
      }
      int res = 0;

      for (int r = 0; r < n; r++)
      {
         if (v[r] <= r)continue;
         for (int j = r+1; j < n; j++)
            if (v[j] <= r)
            {
               res++;
               int tmp = v[r];
               v[r] = v[j];
               v.erase(v.begin() + j);
               v.insert(v.begin() + r + 1, tmp);
               break;
            }
            else
               res++;
      }

      cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}