#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<_ll> _vll;
typedef vector<string> _vs;
typedef istringstream _iss;
#define _a(v) (v).begin(),(v).end()
#define _e(x,y) (fabs((x)-(y))<1e-10)
#define _p push_back
#define _mp make_pair
#define _m(v) memset(v,0,sizeof(v));
#define _f(i,b,e) for(int i=b;i<e;i++)
#define _fl(i,n) for(int i=0;i<(n).length();i++)
#define _fs(i,n) for(int i=0;i<(n).size();i++)
#define _fe(t,i,n) for(t::iterator i=(n).begin();i!=(n).end();i++)
#define _fd(t,e) ((t).find(e)!=(t).end())
#define _s(x,y) {x+=y;y=x-y;x-=y;}
#define _st(x, y, t) {t _t_; _t_=x;x=y;y=_t_;}


#define FILE_INPUT

#ifdef FILE_INPUT
	#define is_ file_in
	#define os_ file_out
#else
	#define is_ cin
	#define os_ cout
#endif



int zcnt;

int main()
{
#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif
	char chline[200];
	int tnum;

	is_>>zcnt;
	for(int zi=1; zi<=zcnt; zi++)
	{
		int scnt, qcnt;
		string rst, rstlast;
		map<string, int> mans, mnew, minit;

		is_>>scnt;
		is_.getline(chline, 200);
		for(int i=0; i<scnt; i++)
		{
			is_.getline(chline, 200);
			rst = chline;
			mans.insert( _mp(rst, 0) );
			minit.insert( _mp(rst, 1000000) );
		}
		is_>>qcnt;
		is_.getline(chline, 200);
		for(int i=0; i<qcnt; i++)
		{
			is_.getline(chline, 200);
			rst = chline;
			mnew = minit;
			mnew[rst] = mans[rst];
			for(map<string, int>::iterator it=mans.begin(); it!=mans.end(); it++)
			{
				if(it->first == rstlast)
					continue;
				for(map<string, int>::iterator jt=mnew.begin(); jt!=mnew.end(); jt++)
				{
					if(jt->first == rst)
						continue;
					if(it->first == jt->first)
						tnum = it->second;
					else
						tnum = it->second + 1;
					if(tnum < jt->second)
						jt->second = tnum;
				}
			}
			mans = mnew;
			rstlast = rst;
		}
		int ans = 10000000;
		for(map<string, int>::iterator it=mans.begin(); it!=mans.end(); it++)
			if(it->second < ans && it->first != rstlast)
				ans = it->second;
		os_<<"Case #"<<zi<<": "<<ans<<endl;
	}


#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif

	return 0;
}