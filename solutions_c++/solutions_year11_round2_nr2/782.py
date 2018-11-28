
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 

int C, D;
vector<pair<int,int> > m;

bool can(double time)
{
	double last_pos = m[0].first-time;

	for(int i=0; i < m.size();++i)
	{
		for(int p = 0; p < m[i].second; ++p)
		{
			if (i==0 && p==0)
				continue;

			double this_pos = m[i].first;
			
			if (this_pos + time < last_pos + D)
				return false;

			double new_pos = max(this_pos-time, last_pos+D);


			last_pos = new_pos;

		}
	}

	return true;
}




int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin>>T;

	REP(t, T)
	{

		m.clear();

		cin >> C >> D;
		REP(i, C)
		{
			int P, V;
			cin >> P >> V;
			m.push_back(MP(P,V));
		}

		double l=0,h=10e12;

		while(abs(h-l) > 10e-9)
		{
			double m = (h+l)/2;

			if(can(m))
				h=m;
			else
				l=m;
		}

		cout << "Case #" << (t+1) << ": ";

		char buf[0xff]={0};
		sprintf(buf, "%.8f", h);
		string s(buf);
		cout << s << "\n";



	}


	int Int;
	std::cin >> Int;
}