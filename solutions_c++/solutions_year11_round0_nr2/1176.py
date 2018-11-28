#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>

using namespace std;

const double EPS = 1e-9;
const long LONGMAX = numeric_limits<long>::max();
const long INTMAX = numeric_limits<int>::max();

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())



const char *in_file = "input.txt";
const char *out_file = "output.txt";

void main()
{
	freopen(in_file, "r", stdin);
	freopen(out_file, "w", stdout);
	int T;
	cin>>T;
	REP(t,T)
	{
		map<string, char> comb;
		map<char , set<char> > op;
		string line, temp;
		int c,d,n;
		cin>>c;
		REP(i,c)
		{
			cin>>temp;
			string in;
			in.push_back(temp[0]);
			in.push_back(temp[1]);
			comb[in] = temp[2];
			in = "";
			in.push_back(temp[1]);
			in.push_back(temp[0]);
			comb[in] = temp[2];
		}
		cin>>d;
		REP(i,d)
		{
			string temp;
			cin>>temp;
			op[temp[0]].insert(temp[1]);
			op[temp[1]].insert(temp[0]);
		}
		cin>>n;
		cin>>line;
		string res;
		map<char , int> in;
		REP(i,n)
		{
			if (res.size()==0)
			{
				res.push_back(line[i]);
				in[line[i]]++;
				continue;
			}

			string last;
			last.push_back(res[res.size()-1]);
			last.push_back(line[i]);

			if (comb.count(last)>0)
			{
				in[res[res.size()-1]]--;
				res[res.size()-1] = comb[last];
				in[comb[last]]++;
			}
			else
			{
				vector<char> inter(100);
				if (op.count(line[i])>0)
				{
					vector<char> a;
					map<char, int>::iterator it = in.begin();
					for(it; it!=in.end();++it)
						if (it->second>0) a.push_back(it->first);
					set_intersection(a.begin(), a.end(), op[line[i]].begin(), op[line[i]].end(), inter.begin());
				}

				if (inter[0]!=0)
				{
					in.clear();
					res = "";
				}
				else
				{
					in[line[i]]++;
					res.push_back(line[i]);
				}
			}
		}

		printf("Case #%d: [", t+1);
		REP(i,res.size())
		{
			if(i) printf(", ");
			printf("%c" , res[i]);
		}

		if (t!=T-1) printf("]\n");
	}
}