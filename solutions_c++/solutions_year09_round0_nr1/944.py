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


int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int l, d, n;
	cin>>l>>d>>n;
	vector<string> words;

	REP(i, d)
	{
		string str;
		cin>>str;
		words.pb(str);
	}

	REP(i, n)
	{
		string str;
		cin>>str;
		int res = 0;

		vector<set<char> > v;
		
		while(str.sz)
		{
			set<char> ss;
			if (str[0] == '(')
			{
				int last = str.find(')');
				for (int j = 1; j < last; j++)
					ss.insert(str[j]);
				str = str.substr(last+1, str.sz - last - 1);
			}
			else
			{
				ss.insert(str[0]);
				str = str.substr(1, str.sz - 1);
			}
			v.pb(ss);
		}
		
		REP(j, words.sz)
		{
			bool fl = true;
			REP(k, words[j].sz)
			{
				if (v[k].find(words[j][k]) == v[k].end())
				{
					fl = false;
					break;
				}
			}
			if (fl)
				res++;
		}

		cout<<"Case #"<<(i + 1)<<": "<<res<<endl;
	}

	return 0;
}