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

typedef long long llong;

llong solve(const vector<int> & peoples,int K,int R)
{
	int ptr = 0;
	llong res = 0;
	vector<llong>  mem(peoples.size(),-1);
	vector<int> index(peoples.size(),-1);
	bool jumped = false;
	for (int i=1;i <= R;++i)
	{
		int store=0;
		int newptr = ptr;
		do
		{
			if (store+peoples[newptr] > K) break;
			store+=peoples[newptr++];
			newptr%=peoples.size();
		}
		while (store <= K && newptr != ptr);
		ptr = newptr;
		res+=store;
		
		if (mem[ptr] != -1 && !jumped)
		{
			jumped = true;
			int l = i-index[ptr];
			res+= (res-mem[ptr])*( (R-i)/l);
			i +=(R-i)/l *l;
			cerr << "Jumping at index: " << i << endl;
		}
		else
		{
			mem[ptr] = res;
			index[ptr] = i;
		}
	}
	return res;
}

int main()
{
	int TestCases=0;
	cin >> TestCases;
	for (int i=0;i < TestCases;++i)
	{
		int R,k,N;
		cin >> R >> k >> N;
		vector<int> input;
		for (int j=0;j < N;++j)
		{
			int F;
			cin >> F;
			input.push_back(F);
		}
		cout << "Case #" << i+1 << ": " << solve(input,k,R) << endl;
	}
	return 0;
}
