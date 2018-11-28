//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <fstream>
#include <utility>
#include <cmath>
#include <map>
#include <set>
using namespace std;

typedef multimap<char,char>::iterator ITER;

int main() {
  int T;
  ifstream ifs("B-small-attempt1.in");
  ofstream ofs("result.dat");
  ifs >> T;
  for (int i = 0; i < T; ++i)
  {
	char temp[2];
	char tc;
	int N, D, C;
	map<pair<char, char>, char> compl_elem;
	multimap<char, char> oppos;
	vector<char> res;
	int cands[1024];
	for(int k = 0; k < 1024; ++k) cands[k] = 0;
	ifs >> N;
	for (int j = 0; j < N; ++j)
	{
		ifs >> temp[0] >> temp[1] >> tc;
		sort(temp, temp + 2);
		compl_elem[make_pair(temp[0],temp[1])] = tc;
	}
	ifs >> D;
	for (int j = 0; j < D; ++j)
	{
		ifs >> temp[0] >> temp[1];
		oppos.insert(make_pair(temp[0], temp[1]));
		oppos.insert(make_pair(temp[1], temp[0]));
	}
	ifs >> C;
	for (int j = 0; j < C; ++j)
	{
		ifs >> tc;
		if(res.empty())
		{
			res.push_back(tc);
			if (oppos.find(tc) != oppos.end())
			{
				cands[tc] = 1;
			}
			continue;
		}
		pair<char, char> last;
		last.first = res.back();
		last.second = tc;
		if (last.first > last.second) swap(last.first, last.second);
		if (compl_elem.find(last) != compl_elem.end())
		{
			if (cands[res.back()] > 0) cands[res.back()]--;
			res.pop_back();
			res.push_back(compl_elem[last]);
		}
		else
		{
			pair<ITER, ITER> r = oppos.equal_range(tc);
			while (r.first != r.second)
			{
				if (cands[(r.first)->second] > 0)
				{
					break;
				}
				r.first++;
			}
			if(r.first == r.second)
			{
				res.push_back(tc);
              if (oppos.find(tc) != oppos.end())
                {
            	  cands[tc]++;
                }
			}
			else
			{
				for(int k = 0; k < 1024; k++) cands[k] = 0;
				res.clear();
			}
		}
	}
	ofs << "Case #" << (i+1) << ": [";
	if (!res.empty()) ofs << res[0];
	for(int j = 1; j < res.size(); ++j)
	{
		ofs << ", "<< res[j];
	}
	ofs << "]\n";
  }
  ofs.close();
  ifs.close();
  return 0;
}
