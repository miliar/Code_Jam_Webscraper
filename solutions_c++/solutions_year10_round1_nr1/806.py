// CodeJam2010-2.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <algorithm>

using namespace std;

void move(vector<vector<int> >& vvMap)
{
	for(size_t i = 0; i < vvMap.size(); ++i)
	{
		vector<int>& a = vvMap[i];
		int empty = -1;
		for(size_t j = 0; j < a.size(); ++j)
		{
			size_t j_ = a.size() - j - 1;
			if(0 == a[j_]) 
			{
				if(empty == -1)
				{
					empty = j_;
				}
				continue;
			}
			else
			{
				if(empty != -1)
				{
					swap(a[j_], a[empty]);
					while(true)
					{
						--empty;
						if(a[empty] == 0)
						{
							break;
						}
					}
				}
			}


		}
	}
}

bool Result(const vector<vector<int> >& vvMap, const int num, int col)
{
	for(size_t i = 0; i < vvMap.size(); ++i)
	{
		int value = 0;
		for(size_t j = 0; j < vvMap[i].size(); ++j)
		{
			if(col == vvMap[i][j])
			{
				++value;
				if(num == value) return true;
			}
			else
			{
				value = 0;
			}
		}
	}

	for(size_t i = 0; i < vvMap.size(); ++i)
	{
		int value = 0;
		for(size_t j = 0; j < vvMap[i].size(); ++j)
		{
			if(col == vvMap[j][i])
			{
				++value;
				if(num == value) return true;
			}
			else
			{
				value = 0;
			}
		}
	}

	vector<vector<int> > vvMapCopy = vvMap;

	for(size_t i = 0; i < vvMapCopy.size(); ++i)
	{
		for(size_t j = 0; j < vvMapCopy.size(); ++j)
		{
			if(col == vvMapCopy[i][j])
			{
				vvMapCopy[i][j] = 0;
				int value = 1;
				int i_ = i;
				int j_ = j;
				while(true)
				{
					++i_;
					++j_;
					if(i_ == vvMapCopy.size() || j_ == vvMapCopy.size()) break;
					if(col != vvMapCopy[i_][j_]) break;
					++value;
					if(value == num) return true;
				}
			}
		}
	}

	vvMapCopy = vvMap;

	for(size_t i = 0; i < vvMapCopy.size(); ++i)
	{
		for(size_t j = 0; j < vvMapCopy.size(); ++j)
		{
			if(col == vvMapCopy[i][j])
			{
				vvMapCopy[i][j] = 0;
				int value = 1;
				int i_ = i;
				int j_ = j;
				while(true)
				{
					++i_;
					--j_;
					if(i_ == vvMapCopy.size() || j_ == -1) break;
					if(col != vvMapCopy[i_][j_]) break;
					++value;
					if(value == num) return true;
				}
			}
		}
	}

	return false;
}

int main(long argc, char* argv[])
{
	ifstream in(argv[1]);

	string line;
	
	getline(in, line);
	
	int counter = atoi(line.c_str());

	for(int i = 0; i < counter; ++i)
	{
		int N = 0;
		int K = 0;
		getline(in, line);
		sscanf(line.c_str(), "%d %d", &N, &K);

		vector<vector<int> > vvMap;
		vvMap.resize(N);
		for(int j = 0; j < N; ++j)
		{
			getline(in, line);
			for(int k = 0; k < N; ++k)
			{
				if(line[k] == '.')
				{
					vvMap[j].push_back(0);
				}
				else if(line[k] == 'R')
				{
					vvMap[j].push_back(1);
				}
				else
				{
					vvMap[j].push_back(2);
				}
			}
		}

		move(vvMap);
		bool red = Result(vvMap, K, 1);
		bool blue = Result(vvMap, K, 2);

		if(red && blue)
		{
			printf("Case #%d: %s\n", i+1, "Both");
		}
		else if(red)
		{
			printf("Case #%d: %s\n", i+1, "Red");
		}
		else if(blue)
		{
			printf("Case #%d: %s\n", i+1, "Blue");
		}
		else
		{
			printf("Case #%d: %s\n", i+1, "Neither");
		}
	

		int i = 0;


	}
	return 0;
}

