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

  unsigned int T, A, B;

  cin >> T;

  for (unsigned int t = 0; t < T; t++)
  {
    cin >> A >> B;

    unsigned int y = 0;
    unsigned int D = 0;
    unsigned int a = A;

    // # of digits
    while (a > 0)
    {
      a /= 10;
      D++;
    }

    unsigned int m[D];

    for (unsigned int n = A; n <= B; n++)
    {
      m[0] = n;

      for (unsigned int d = 1; d < D; d++)
      {
	unsigned int d10 = (unsigned int)pow(10,d);
        unsigned int Dd10 = (unsigned int)pow(10,D-d);
	m[d] = n/(pow(10,d)) + (n - (n/d10)*d10) * Dd10;
      
	// avoid double counting same permutations like 1212
        bool same = false;
	for (unsigned int i = 0; i < d; i++)
	{
	  if (m[d] == m[i])
	    same = true;
	}

        if ((m[d] >= A) && (m[d] <= B) && !same)
          y++;
      }
    }

    y /= 2;

    cout << "Case #" << t+1 << ": " << y << endl;
  }
  return 0;
}

