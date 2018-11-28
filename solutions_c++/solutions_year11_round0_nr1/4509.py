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
using namespace std;

int main() {
  int T;
  ifstream ifs("A-large.in");
  ofstream ofs("result.dat");
  ifs >> T;
  for (int i = 0; i < T; ++i)
  {
	int N;
	ifs >> N;
	char R;
	int P, oPl = 1, bPl = 1;
	deque<pair<int, int> > ostep, vstep;
	for (int j = 0; j < N; ++j)
	{
		ifs >> R;
		ifs >> P;
		if(R == 'O')
		{
			ostep.push_back(make_pair(j, fabs(P - oPl)));
			oPl = P;
		}
		else
		{
          vstep.push_back(make_pair(j, fabs(P - bPl)));
          bPl = P;
		}
	}
	int res = 0;
	for (int j = 0; j < N; ++j)
	{
		if(!ostep.empty() && ostep.front().first == j)
		{
			res += ostep.front().second + 1;
			vstep.front().second -= min(ostep.front().second + 1, vstep.front().second);
			ostep.pop_front();
		}
		else
		{
          res += vstep.front().second + 1;
          ostep.front().second -= min(ostep.front().second, vstep.front().second + 1);
          vstep.pop_front();
		}
	}
	ofs << "Case #" << (i+1) << ": " << res << "\n";
  }
  ofs.close();
  ifs.close();
  return 0;
}
