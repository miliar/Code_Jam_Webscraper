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

  unsigned int T, N, S, P, x, y;

  cin >> T;

  for (unsigned int t = 0; t < T; t++)
  {
    cin >> N >> S >> P;
    y = 0;
    for (unsigned int n = 0; n < N; n++)
    {
      cin >> x;
      if ((x + 2)/3 >= P)
        y++;
      // x = 0 is special because negative score is not possible
      else if ( (x != 0) && ((x + 4)/3 >= P) && (S > 0) )
      {
        y++;
	S--;
      }
    }
    cout << "Case #" << t+1 << ": " << y << endl;
  }
  return 0;
}

