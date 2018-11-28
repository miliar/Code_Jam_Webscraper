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

string filename = "C-large";

string str = "welcome to code jam";

ll mod = 10000;

ll mem[600][20];

int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int n;
	cin>>n;
	string stm;
	getline(cin, stm);
	REP(t, n)
	{
		ll res = 0;
		memset(mem, 0, sizeof(mem));

		string s;
		getline(cin, s);

		if (str[0] == s[0])
			mem[0][0] = 1;

		FOR(i, 1, s.sz)
			REP(k, str.sz)
			if (s[i] == str[k])
			{
				if (k == 0)
				{
					mem[i][k] = 1;
				}
				else
				{
					REP(j, i)
						if (s[j] == str[k-1])
						{
							mem[i][k] += mem[j][k-1];
							mem[i][k] %= mod;
						}
				}
			}

		REP(i, s.sz)
		{
			res += mem[i][str.sz - 1];
			res %= mod;
		}
		
		/*REP(i, s.sz)
		{
			REP(j, str.sz)
				cout<<mem[i][j]<<" ";
			cout<<endl;
		}*/

		ostringstream ssout;
		ssout<<res;
		string sres = ssout.str();
		while (sres.sz != 4)
			sres = "0" + sres;

		cout<<"Case #"<<t+1<<": "<<sres<<endl;
	}

	return 0;
}