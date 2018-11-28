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
const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())



const char *in_file = "input.txt";
const char *out_file = "output_b.txt";

int n,m;

int main()
{
	freopen(in_file, "r", stdin);
	freopen(out_file, "w", stdout);

	int T;
	cin>>T;
	REP(t,T)
	{
		cout<<"Case #"<<t+1<<":";
		int n,m;
		cin>>n>>m;
		vector<string> w(n), l(m);
		REP(i,n)
			cin>>w[i];
		REP(i,m)
			cin>>l[i];
		vector<string> v(m);
		vector<int> b(m,-1);

		REP(i,m)
		{
			int best =0;
			REP(j,n)
			{
				int c_best = 0;		
				int len = w[j].size();
				vector<int> c;
				map<char, int> s;
				// for len
				REP(ii,n)
				{
					if (w[ii].size() == len)
					{
						c.push_back(ii);
						REP(jj, w[ii].size())
						{
							s[w[ii][jj]]++;
						}
					}
				}
				// for letter
				int k = 0;
				while(true)
				{
					if (c.size()==1) break;
					while (s[l[i][k]]<1) 
						++k;
					if (k>=l[i].size()) break;
					vector<int> c2;
					bool ok2 = false;
					REP(ii,c.size())
					{
						bool ok = true;
						REP(jj,w[j].size())
						{
							if (w[j][jj] == l[i][k])
							{
								ok2 = true;
								if (w[c[ii]][jj]==w[j][jj])
									continue;
								else
								{
									ok = false;
									break;
								}
							}
							else if(w[c[ii]][jj]== l[i][k])
							{
								ok = false;
								break;
							}
						}
						if (ok)
							c2.push_back(c[ii]);
					}
					c = c2;
					s.clear();
					REP(jj,c.size())
					{
						REP(i2, w[c[jj]].size())
						{
							s[w[c[jj]][i2]]++;
						}
					}
					if (!ok2) ++c_best;
					if (c.size() == 1 ) break;
					++k;
					if (k>=l[i].size()) break;
				}
				if (c_best>b[i])
				{
					b[i] = c_best;
					v[i] = w[j];
				}
			}

		}


		REP(i,m)
			cout<<" "<<v[i];
		cout<<endl;
	}
}
