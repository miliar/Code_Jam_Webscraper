#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <boost/foreach.hpp>

#define foreach BOOST_FOREACH
using namespace std;

typedef vector<string> VString;
typedef vector<unsigned long> VInt;


int main()
{
  int ncases;
  cin >> ncases;
  for (int i=0; i<ncases; ++i)
  {
    unsigned R, k, N;
    cin >> R >> k >> N;
    VInt groupSize;
    for(int j=0; j<N; ++j)
    {
      unsigned s;
      cin >> s;
      groupSize.push_back(s);
    }
    unsigned long groupOffset = 0;
    unsigned long count = 0;
    for (unsigned int r=0; r<R; ++r)
    {
      unsigned long tcont = 0;
      unsigned long firstOffset = groupOffset;
      bool first = true;
      while (tcont + groupSize[groupOffset] <= k
	&& ((first || firstOffset != groupOffset)))
      {
	first = false;
	tcont += groupSize[groupOffset];
	groupOffset++;
	groupOffset %= N;
      }
      count += tcont;
    }
    cout << "Case #" << i+1
    << ": " << count << std::endl;
  }
}


