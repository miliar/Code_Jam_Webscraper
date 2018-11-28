//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <assert.h>
#include <list>

using namespace std;

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	for (int _case=1; _case<=cases; _case++)
	{
		int count;
		f >> count;
		int _min = INT_MAX;
		int sum = 0;
		int sum_xor = 0;
		for (int i=0; i<count; i++)
		{
			int x;
			f >> x;
			if (x<_min)
				_min = x;
			sum+=x;
			sum_xor^=x;
		}

		cout << "Case #" << _case << ": ";
		if (sum_xor)
			cout << "NO";
		else
			cout << sum-_min;

		cout << endl;
	}
}
