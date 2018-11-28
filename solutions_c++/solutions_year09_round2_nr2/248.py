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

string filename = "B-large";
//string filename = "input";

int d[10];

int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	REP(t, T)
	{
		string str, res;
		cin>>str;

		vector<int> v;

		memset(d, 0, sizeof(d));
		REP(i, str.sz)
			d[str[i] - '0']++;

		v.clear();
		REP(i, str.sz)
			v.pb(str[i] - '0');

		if (next_permutation(v.begin(), v.end()))
		{
			res = "";
			REP(i, v.sz)
				res += (char)('0' + v[i]);
		}
		else
		{
			res = "";
			//all 0 at the end
			v.clear();
			FOR(i, 1, 10)
				REP(j, d[i])
					v.pb(i);
			REP(i, v.sz)
			{
				res += (char)('0' + v[i]);
				if (i == 0)
				{
					REP(j, d[0] + 1)
						res += (char)('0');
				}
			}
		}

		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}