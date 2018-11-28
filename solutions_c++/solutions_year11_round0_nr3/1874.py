#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <limits>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; ++c)
	{
    int xorAll = 0, sum = 0, min = numeric_limits<int>::max();
    
		size_t nitems;
		
		cin >> nitems;
		
		for (size_t i = 0; i < nitems; ++i)
		{
      int item;
			cin >> item;
      
      xorAll ^= item;
      sum += item;
      
      if (item < min)
        min = item;
		}
    
    cout << "Case #" << c << ": ";
    if (xorAll)
      cout << "NO";
    else
      cout << (sum - min);
    
		cout << endl;
	}
}
