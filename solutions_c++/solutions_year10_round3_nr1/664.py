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



int main(long argc, char* argv[])
{
	ifstream in(argv[1]);

	string line;
	
	getline(in, line);
	
	int counter = atoi(line.c_str());

	for(int iTest = 0; iTest < counter; ++iTest)
	{
		int N = 0;
		getline(in, line);
		sscanf(line.c_str(), "%d", &N);

		vector<int> left, right;
		for(size_t i = 0; i < N; ++i)
		{
			int l,r;
			getline(in, line);
			sscanf(line.c_str(), "%d %d", &l, &r);
			left.push_back(l);
			right.push_back(r);
		}

		int c = 0;
		for(int i = 0; i < left.size(); ++i)
		{
			for(int j = i; j < left.size(); ++j)
			{
				if((left[i] - left[j])*(right[i] - right[j]) < 0)
				{
					++c;
				}
			}
		}




		printf("Case #%d: %d\n", iTest+1, c);
	


	}
	return 0;
}


