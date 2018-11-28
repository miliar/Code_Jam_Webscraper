#include <fstream>
#include <iostream>
#include <cassert>
#include <cmath>
#include <stdexcept>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <cctype>
#include <algorithm>

using namespace std;

typedef unsigned long long Ullong;


int main()
{
  unsigned int T, N, K;

  cin >> T;
  
  for (unsigned int t = 0; t < T; t++)
  {
    cin >> N >> K;
    cout << "Case #" << t+1 << ": ";
    if ((K+1) & ((1 << N) -1))
      cout << "OFF" << endl;
    else
      cout << "ON" << endl;
  }

  return 0;
}

