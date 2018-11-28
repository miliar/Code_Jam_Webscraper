#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
#include<list>
#include<deque>
#include<iterator>
#include<sstream>

using namespace std;

#define FOR(i, a, b) for (int i(a) ; i <= b; ++i)
#define FORD(i, a, b) for (int i(a) ; i >= b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)

#define M(a) memset(&a,0,sizeof(a));
#define RES(i) cout<<"Case #"<<i<<": "<<
#define I cin>>
#define O cout<<
#define NL <<endl

#define ALL(c) (c).begin(), (c).end()

//typedef long long int64;
//typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

char buf[200];
void main()
{
	int cases;
	cin>>cases;
	FOR(t,1,cases)
	{
		int n,m;
		cin>>n>>m;
		map<string,int> mp;
		map<string,int>::iterator it;
		FOR(i,1,n)
		{
			string s;
			cin>>s;
			mp[s]=0;
			int ff=s.rfind("/");
			while(ff != string::npos && ff!=0)
			{
				string t=s.substr(0,ff);
				mp[t]=0;
				ff=s.rfind("/",ff-1);
			}

		}
		unsigned int tot=0;
		FOR(k,1,m)
		{
			string s;
			cin>>s;
			bool b=true;
			while(b)
			{
				int ff=s.size();
				if (mp.find(s) == mp.end() && s.size())
				{
					mp[s]=0;
					tot++;
					ff=s.rfind("/",ff-1);
					s=s.substr(0,ff);

				}
				else
				{
					break;
				}
			}
		}
/*		for(it=mp.begin();it!=mp.end();it++)
		{
			cout<<it->first<<endl;
		}
*/		
		cout<<"Case #"<<t<<": "<<tot<<endl;
		
	}
}