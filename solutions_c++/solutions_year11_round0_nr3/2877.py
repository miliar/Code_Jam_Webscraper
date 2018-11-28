// gj.cpp
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

int main(int argc, char* argv[])
{
	ifstream f;
	f.open(argv[1]);

	uint64 cases;
	f >> cases;

	for (uint64 i = 0; i < cases; ++i)
	{
		uint64 n;
		f >> n;
		vector<uint64> c;

		for (uint64 j = 0; j < n; ++j)
		{
			uint64 aux;
			f >> aux;
			c.push_back(aux);
		}
		sort(c.begin(), c.end());

		uint64 res = 0,
			   xor = 0,
			   min = 0;
		for (vector<uint64>::iterator it = c.begin(); it != c.end(); ++it)
		{
			res += *it;
			xor ^= *it;
		}
		if (c.size())
			min = *(c.begin());

		if (xor)
			cout << "Case #" << i + 1 << ": NO" << endl;
		else
			cout << "Case #" << i + 1 << ": " << res - min << endl;
	}

	return 0;
}

