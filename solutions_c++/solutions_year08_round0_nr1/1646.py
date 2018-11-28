#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>

#include <time.h>

using namespace std;

#include <boost/foreach.hpp>

int Case;

int matrix[1001][100];

class Solution
{
public:
  vector<string> engines;
  vector<string> queries;

  int MinSwitches;


  void Solve()
  {
    const int X = numeric_limits<int>::max();

    for (vector<string>::size_type e = 0; e < engines.size(); ++e)
    {
      matrix[queries.size()][e] = 0;
    }

    for (long long q = static_cast<long long>(queries.size()) - 1; q > -1; --q)
//    for (vector<string>::size_type q = 0; q <queries.size(); ++q)
    {
      for (vector<string>::size_type e = 0; e < engines.size(); ++e)
      {
        if (engines[e] == queries[q])
        {
          matrix[q][e] = X;
        }
        else
        {
          if (X == matrix[q + 1][e])
          {
            matrix[q][e] = 1 + *min_element(matrix[q + 1], matrix[q + 1] + engines.size());
          }
          else
          {
            matrix[q][e] = matrix[q + 1][e];
          }
        }
//        cout<<matrix[q][e]<<" ";
      }
//      cout<<endl;
    }
    MinSwitches = *min_element(matrix[0], matrix[0] + engines.size());
  }
private:
};


int main(int argc, char* argv[])
{
//  fill(reinterpret_cast<int*>(matrix), reinterpret_cast<int*>(matrix) + sizeof(matrix)/sizeof(matrix[0][0]), 0);

  ifstream ifs(argv[1]);
  if(!ifs) return 1;

  ofstream ofs(argv[2]);
  if(!ofs) return 2;

  time_t timeStart;
	time(&timeStart);

  int N;
  ifs>>N;
  for(Case = 1; Case <= N; ++Case)
  {
    cout<<"Case #"<<Case<<": "<<endl;
    Solution s;
    int NEngines;
    ifs>>NEngines;
    {
      string dummy;
      getline(ifs, dummy);
    }
    for (int i = 0; i < NEngines; ++i)
    {
      s.engines.push_back(string());
      getline(ifs, s.engines.back());
    }

    int NQueries;
    ifs>>NQueries;
    {
      string dummy;
      getline(ifs, dummy);
    }
    for (int i = 0; i < NQueries; ++i)
    {
      s.queries.push_back(string());
      getline(ifs, s.queries.back());
    }
    s.Solve();

    ofs<<"Case #"<<Case<<": "<<s.MinSwitches<<endl;
  }
  
	time_t timeEnd;
	time(&timeEnd);

	double the_diffTime = difftime(timeEnd, timeStart);
	long long diffTime = static_cast<long long>(the_diffTime);

	cout<<diffTime / (60 * 60)<<" hours; "<< diffTime % (60 * 60) / 60<<" minutes; "
		<<diffTime % (60 * 60) % 60<<" seconds; "<<endl;
  
	return 0;
}
