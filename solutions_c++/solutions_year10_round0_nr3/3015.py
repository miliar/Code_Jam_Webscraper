// CodeJam2010-2.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

long GetNext(const vector<long>& vG,
			 long start,
			 long long& money, 
			 const unsigned long long& K)
{
	money = 0;

	size_t counter = 0;

	long next = 0;
	while(true)
	{
		money += vG[start];

		next = start + 1;
		if(next == (long)vG.size()) next = 0;
		++counter;

		if(K < money + vG[next] || vG.size() == counter)
		{
			return next;
		}
		start = next;
	}
}

long long
GetMoney(unsigned long R,
		 const unsigned long long& K,
		 const vector<long>& vG)
{
	set<long> index_set;
	vector<pair<long, long long> > order;

	long long money;
	long next;

	next = GetNext(vG, 0, money, K);
	index_set.insert(0);
	order.push_back(make_pair(0, money));

	while(true)
	{
		if(index_set.end() != index_set.find(next))
		{
			break;
		}
		long cur = next;
		next = GetNext(vG, next, money, K);
		index_set.insert(cur);
		order.push_back(make_pair(cur, money));
	}

	long long total_money = 0;
	size_t loop_start;
	for(size_t i = 0; i < order.size(); ++i)
	{
		if(order[i].first == next)
		{
			loop_start = i;
			break;
		}
		total_money += order[i].second;
	}

	long loop_size = order.size() - loop_start;
	long long loop_money = 0;
	for(size_t i = loop_start; i < order.size(); ++i)
	{
		loop_money += order[i].second;
	}

	long loops = (R - loop_start) / loop_size;
	long remain = (R - loop_start) % loop_size;

	total_money += loops * loop_money;

	for(size_t i = 0; i < remain; ++i)
	{
		total_money += order[i+loop_start].second;
	}

	return total_money;
}

long main(long argc, char* argv[])
{
	ifstream in(argv[1]);

	string line;
	
	getline(in, line);
	
	long counter = atoi(line.c_str());

	for(long i = 0; i < counter; ++i)
	{
		unsigned long R, N;
		unsigned long long K;
		getline(in, line);
		sscanf(line.c_str(), "%u %llu %u", &R, &K, &N);

		getline(in, line);
		vector<long> vG;
		char* tok = (char*)line.c_str();
		vG.push_back(atoi(strtok(tok, " ")));
		for(unsigned long j = 1; j < N; ++j)
		{
			vG.push_back(atoi(strtok(NULL, " ")));
		}

		printf("Case #%d: %lld\n", i+1, GetMoney(R, K, vG));

	}
	return 0;
}

