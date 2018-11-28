#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <fstream>
#include <cassert>
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

#define FOREACH(container,iter) for(typeof( (container).begin()) iter = (container).begin();iter != (container).end();++iter)
#define REP(i,l) for (int i=0;i < ((int)l);++i)
#define ALL(c) c.begin(),c.end()

typedef vector<string> diamond;

bool go(const vector<vector<bool> > &src,
		vector<vector<bool> > &dest)
{
	dest = src;
	bool res= false;
	for(int i=1;i < 150;++i) for (int j=1;j < 150;++j)
	{
		if (src[i][j])
		{
			res=true;
			if (!src[i-1][j] && !src[i][j-1]) dest[i][j] = false;
		}
		else
		{
			if (src[i-1][j] && src[i][j-1]) dest[i][j] = true;
		}
	}
	return res;
}


int main()
{
	ifstream in ("C-small-attempt0.in"); //"A-large.in"
// 	ifstream in ("test");
	ofstream out ("C-small-output0.out");
	assert( ! (!in));
// 	istream & in = cin;
// 	ostream & out = cout;

	int TestCases;
	in >> TestCases;

	for (int CASE=0;CASE < TestCases;++CASE)
	{
		int R;
		in >> R;
		vector<vector<bool> > g1(150,vector<bool>(150));
		REP(k,R)
		{
			int a,b,c,d;
			in >> a >> b >> c >>  d;
			for (int i=a;i <= c;++i) for (int j=b;j <= d;++j)
				g1[i][j] = true;
		}
		vector<vector<bool> > g2 = g1;
// 		REP(i,6)
// 		{
// 			REP(j,6)
// 				cout << g1[i][j];
// 			cout << endl;
// 		}
		int ans=0;
		while( go(g1,g2))
		{
			ans++;g1.swap(g2);
		}
		
		out << "Case #" << CASE+1 << ": " << ans << endl;
	}

	return 0;
}
