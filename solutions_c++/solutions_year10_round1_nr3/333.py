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
typedef long long llong;

llong GCD(llong a,llong b)
{
	llong T;
	while (b != 0)
	{
		T = b;
		b = a % b;
		a = T;
	}
	return a;
}

bool solve_easy(int A,int B)
{
	if (A == B) return false;
	if (A > B) return solve_easy(B,A);

	if (2*A < B)
		return true;

	return !solve_easy(B-A,A);

// 	cout << "winning with: " << A << " " << B << endl;
// 	return ans%2;
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
		int A1,A2,B1,B2;
		in >> A1 >> A2 >> B1 >> B2;
		int ans = 0;
		for (int k=A1;k <= A2;++k)
			for (int j=B1;j <= B2;++j)
				ans+=solve_easy(k,j);

		cout << "Case #" << i+1 << ": " << ans << endl;

	}

	return 0;
}
