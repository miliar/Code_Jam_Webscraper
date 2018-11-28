#include <set>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

long toTen(long v, const int b)
{
	/*if (b == 10)*/ return v;
}
long sumSquare(long val, const int b)
{
	long sum = 0;
	while (val > 0) 
	{
		long valb = toTen( (val%b), b);
		sum += valb*valb; 
		val /= b; 
	}
	return sum;
}

bool happyNum(long val, int b)
{
	std::set<long> prevs;
	prevs.insert(val);
	while (val > 1)
	{
		val = sumSquare(val, b);
		if (prevs.find(val) != prevs.end()) return false;
		prevs.insert( val );
	}
	return val == 1;
}

int smallestHappyNum(std::vector<int> &bs)
{
	for (int i=2; i < INT_MAX; ++i)
	{
		int j=0;
		for (; j < bs.size(); ++j)
			if (bs[j] != 2 && !happyNum(i, bs[j])) break;
		if (j == bs.size()) return i;
	}
	return INT_MAX;
}

int runTest()
{
	std::string str;
	getline( cin, str );

	vector<int> bs;
	istringstream is(str);
	while ( !is.eof() )
	{
		int b;
		is >> b;
		bs.push_back(b);
	}
	return smallestHappyNum(bs);
}

int main()
{
	int T;
	cin >> T;
	std::string str;
	getline( cin, str );
	for(int i=0; i < T; ++i)
		printf("Case #%d: %d\n", i+1, runTest());
}
