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

/***h ttp://mattmccutchen.net/bigint/  ***/
#include "bigint-2010.04.30/BigInteger.hh"
#include "bigint-2010.04.30/BigIntegerUtils.hh"

using namespace std;
using namespace boost;
using namespace boost::lambda;

#define FOREACH(container,iter) for(typeof(container.begin()) iter = container.begin();iter != container.end();++iter)
#define REP(i,l) for (int i=0;i < l;++i)
#define ALL(c) c.begin(),c.end()

typedef BigInteger BigInt;
typedef vector<BigInt>::iterator BigIntIter;

BigInt MCD(BigInt a,BigInt b)
{
	while (b != 0)
	{
		BigInt r = a%b;
		if (r == 0) return b;
		a = b;
		b = r;
	}
	return a;
}

BigInt Solve (const vector<BigInt> & input)
{
	vector<BigInt> v;
	vector<BigInt>::const_iterator miniter = min_element(input.begin(),input.end());
	for (vector<BigInt>::const_iterator iter = input.begin();iter != input.end();++iter)
	{
		if (iter == miniter) continue;
		v.push_back(*iter - *miniter);
	}
	
	BigIntIter endIterator = remove_if(v.begin(),v.end(),bind1st(equal_to<BigInt>(),0) );
	sort(v.begin(),endIterator);
	endIterator = unique(v.begin(),endIterator);
	
	while (v.begin()+1 != endIterator)
	{
// 		cout << "MCD: " << v[0] << " _ " << *(endIterator-1) << " is: ";
		v[0] = MCD(v[0],*(--endIterator));
// 		cout << v[0] << endl;
	}
	assert(v[0] != 0);
	BigInt p = input[0]%v[0];
	if (p == 0) return 0;
	return v[0]-p;
}

int main()
{
	int TestCases;
	cin >> TestCases;
	
	for (int i=0;i < TestCases;++i)
	{
		int N;
		cin >> N;
		vector<BigInt> bb;
		for (int j=0;j < N;++j)
		{
			string z;
			cin >> z;
			bb.push_back(stringToBigInteger(z));
		}
		
		cout << "Case #" << i+1 << ": " << Solve(bb) << endl;
	}
	
	return 0;
}
