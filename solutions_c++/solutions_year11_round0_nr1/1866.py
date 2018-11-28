#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <limits>

#define ABSD(a,b) ((a) >= (b)? (a) - (b): (b) - (a))

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; ++c)
	{
    int pO = 1, pB = 1, restO = 0, restB = 0, count = 0;
    size_t nitems;
		
		cin >> nitems;
		// play
		for (size_t i = 0; i < nitems; ++i)
		{
      char who;
      cin >> who;
      int where;
      cin >> where;
      if (who == 'O')
      {
        int pathl = ABSD(where, pO) - restO;
        if (pathl < 0)
          pathl = 0;
        ++pathl; // push the button
        restB += pathl;
        restO = 0;
        count += pathl;
        pO = where;
      }
      else
      {
        int pathl = ABSD(where, pB) - restB;
        if (pathl < 0)
          pathl = 0;
        ++pathl; // push the button
        restO += pathl;
        restB = 0;
        count += pathl;
        pB = where;
      }
		}
    
    cout << "Case #" << c << ": ";
    
    cout << count;
		cout << endl;
	}
}
