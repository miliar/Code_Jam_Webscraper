#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <iostream>
#include <utility>
#include <sstream>
#include <cstring>
#include <boost/dynamic_bitset.hpp>

using namespace std;
using namespace boost;
template<typename T> void P(T& t)
{
	cerr << t << endl;
}


int calcSwitchCount()
{
	int engineCount;
	string s;
	s.reserve(200);

	map<string, int> engines;

	cin >> engineCount;
	getline(cin, s);
	
	

	P(engineCount);
	if(engineCount > 200)
	{
		cerr << "queryCount error" << endl;
		exit(1);
	}
	for(int i=0;i<engineCount;i++)
	{
		getline(cin, s);
		engines[s] = i;
		cerr << s << endl;
	}

	vector<int> queries;
	queries.reserve(1000);

	int queryCount;
	cin >> queryCount;
	getline(cin, s);
	P(queryCount);
	if(queryCount > 12000)
	{
		cerr << "queryCount error" << endl;
		exit(1);
	}
	
	for(int i=0;i<queryCount;i++)
	{
		getline(cin, s);
		queries.push_back(engines[s]);
	}


	/*
	for(map<string, int>::iterator it = engines.begin();
		it != engines.end(); ++it)
	{
		cerr << it->second << ":" << it->first << endl;
	}

	for(vector<int>::iterator it = queries.begin();
		it != queries.end(); ++it)
	{
		cerr << *it << ", ";
	}
	cerr << endl;
	*/
	dynamic_bitset<> can(engines.size());
	can.flip();

	int ret = 0;
	for(size_t i=0;i<queries.size();i++)
	{
		can[queries[i]] = false;
		if(can.none())
		{
			//cerr << i << endl;
			can.flip();
			can[queries[i]] = false;
			ret++;
		}
	}
	return ret;

}


int main()
{
	
	int testcaseCount;
	cin >> testcaseCount;

	for(int i=0;i<testcaseCount;i++)
	{
		//cerr << "start" << endl;
		printf("Case #%d: %d\n", i+1, calcSwitchCount());  
	}

	cerr << "OK" << endl;
}

