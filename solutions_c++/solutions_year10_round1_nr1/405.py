#include <vector>
#include <list>
#include <map>
#include <set>
#include <fstream>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
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
#include <climits>
#include <cstring>
#include <cfloat>
#include <boost/multi_array.hpp>
#include <boost/lambda/lambda.hpp>
#include <boost/lambda/bind.hpp>
#include <boost/lambda/if.hpp>
#include <boost/lambda/loops.hpp>
#include <boost/lambda/switch.hpp>
#include <boost/lambda/construct.hpp>
#include <boost/lambda/casts.hpp>
#include <boost/lambda/algorithm.hpp>
#include <boost/lambda/numeric.hpp>

using namespace std;
using namespace boost;
using namespace boost::lambda;

#define FOREACH(container,iter) for(typeof(container.begin()) iter = container.begin();iter != container.end();++iter)
#define REP(i,l) for (int i=0;i < l;++i)
#define ALL(c) c.begin(),c.end()

typedef vector<string> vs;

struct eq_dot
{
	bool operator()(const char & c) {return c == '.';}
};

vs rotate(const vs & s)
{
	vs res(s[0].size(),string(s.size(),'.'));

	REP(i,s.size()) REP(j,s[0].size())
		res[j][i] = s[s.size()-i-1][j];

	REP(j,s[0].size())
	{
		string m;
		REP(i,s.size()) m+=res[i][j];

		string::iterator end = remove_if(m.begin(),m.end(),eq_dot());
		int c = m.end()-end;
		m.erase(end,m.end());
		m.insert(0,c,'.');
		REP(i,s.size()) res[i][j] = m[i];
	}
	return res;
}

bool can_win(const char c,int K,const vs & s)
{
	int best=0;

	REP(i,s.size())
	{
		int a=0;
		REP(j,s[0].size())
		{
			if (s[i][j] != c) {best = max(best,a);a=0;}
			else a++;
		}
		best = max(best,a);
	}
	REP(i,s.size())
	{
		int a=0;
		REP(j,s[0].size())
		{
			if (s[j][i] != c) {best = max(best,a);a=0;}
			else a++;
		}
		best = max(best,a);
	}

	REP(i,s.size()) REP(j,s[0].size())
	{
		int a = 0;
		int f = 0;
		while (i+f < s.size() && j+f < s[0].size())
		{
			if (s[i+f][j+f] != c) {best=max(best,a);a=0;}
			else a++;
			f++;
		}
		best = max(best,a);
	}
	REP(i,s.size()) REP(j,s[0].size())
	{
		int a = 0;
		int f = 0;
		while (i+f < s.size() && j-f >= 0)
		{
			if (s[i+f][j-f] != c) {best=max(best,a);a=0;}
			else a++;
			f++;
		}
		best = max(best,a);
	}

	REP(i,s.size()) REP(j,s[0].size())
	{
		int a = 0;
		int f = 0;
		while (i-f >= 0 && j+f < s[0].size())
		{
			if (s[i-f][j+f] != c) {best=max(best,a);a=0;}
			else a++;
			f++;
		}
		best = max(best,a);
	}
	REP(i,s.size()) REP(j,s[0].size())
	{
		int a = 0;
		int f = 0;
		while (i-f >= 0 && j-f >= 0)
		{
			if (s[i-f][j-f] != c) {best=max(best,a);a=0;}
			else a++;
			f++;
		}
		best = max(best,a);
	}
// 	cout << "C: " << c << " best: " << best << endl;
	if (best >= K) return true;
	return false;
}

int main()
{
// 	ifstream input("test");
// 	assert( ! (!input));
	istream & in = cin;
	ostream & out = cout;

	int TestCases;
	in >> TestCases;

	for (int i=0;i < TestCases;++i)
	{
		int I,K;
		in >> I >> K;
		vs table (I,string(I,'.'));
		
		REP(ii,I) REP(j,I) in >> table[ii][j];

		vs ans = rotate(table);

// 		REP(ii,I)
// 		{
// 			REP(j,I)
// 				out << ans[ii][j] << " ";
// 			out << endl;
// 		}

		bool red = can_win('R',K,ans);
		bool blu = can_win('B',K,ans);

		out << "Case #" << i+1 << ": ";
		if (red && blu) out << "Both";
		else if (red) out << "Red";
		else if (blu) out << "Blue";
		else out << "Neither";
		out << endl;
	}

	return 0;
}
