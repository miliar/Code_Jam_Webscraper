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

int solve(const vector<int> & M)
{
	if (M.size() == 0) return 0;
	int bu = 0;
	vector<int> next(M.size()/2);
	for (int i=0;(i+1) < M.size();i+=2)
	{
		next[i/2] = min(M[i],M[i+1]);
		next[i/2]--;
		if (next[i/2] < 0) {bu++;next[i/2]=0;}
	}
// 	cout << "Alive: " << M.size() << endl;
	return bu+solve(next);
}


int main()
{
	ifstream in ("B-small-attempt0.in"); //"A-large.in"
	ofstream out ("B-small-output0.out");
// 	assert( ! (!in));
// 	istream & in = cin;
// 	ostream & out = cout;

	int TestCases;
	in >> TestCases;

	for (int CASE=0;CASE < TestCases;++CASE)
	{
		int P;
		in >> P;
		vector<int> M ((1 << P));
		REP(k,M.size()) in >> M[k];
		vector<int> C ( (1<<P) -1);
		REP(k,C.size()) in >> C[k];
		
		out << "Case #" << CASE+1 << ": " << solve(M) << endl;
	}

	return 0;
}
