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
typedef vector<int> VInt;

int main()
{
  int ncases;
  cin >> ncases;
  for (int i=0; i<ncases; ++i)
  {
    unsigned N, K;
    cin >> N  >> K;
    bool res = (K & ( (1 << N)-1)) == ( (1 << N)-1);
    cout << "Case #" << i+1
    << ": "
    << (res?"ON":"OFF")
    << std::endl;
  }
}
