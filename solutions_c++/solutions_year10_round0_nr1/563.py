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

int main()
{
	istream & in = cin;
	ostream & out = cout;

	int TestCases;
	in >> TestCases;
	
	for (int i=0;i < TestCases;++i)
	{
		int N,K;
		in >> N >> K;
		int res = K%(1 << N);
		out << "Case #" << i+1 << ": " << (__builtin_popcount(res)==N ? "ON" : "OFF") << endl;
	}
	
	return 0;
}
