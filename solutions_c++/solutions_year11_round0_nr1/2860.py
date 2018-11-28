// gj.cpp
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
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
		uint n;
		f >> n;
		vector<uint> btns;
		vector<char> clrs;
		char c;
		uint btn;
		for (uint j = 0; j < n; ++j)
		{
			f >> c >> btn;
			clrs.push_back(c);
			btns.push_back(btn);
		}

		__int64 res = 0,
				prevo = 1,
				prevb = 1,
			    cur = 1,
			    time = 0;
		__int64* prev;
		vector<uint>::iterator ib = btns.begin();
		vector<char>::iterator ic = clrs.begin();
		char curcol;
		while (ib != btns.end())
		{
			curcol = *ic;
			prev = ('O' == curcol) ? &prevo : &prevb;
			__int64 ptime = time;
			time = 0;
			while (ib != btns.end() && curcol == *ic)
			{
				cur = *ib;
				__int64 aux = cur - *prev;
				if (aux < 0)
					aux = -aux;

				if (ptime)
				{
					if (aux - ptime > 0)
						aux -= ptime;
					else
						aux = 0;

					ptime = 0;
				}

				time += aux + 1;

				++ib;
				++ic;
				*prev = cur;
			}

			res += time;
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}

