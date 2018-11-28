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
		uint c;
		f >> c;
		map<char, char> opp;
		map<char, uint> oppc;
		map<string, char> nb;
		string a;
		// Non-base element map
		for (uint j = 0; j < c; ++j)
		{
			f >> a;
			char cc = a[2];
			a.resize(2);
			nb[a] = cc;
			reverse(a.begin(), a.end());
			nb[a] = cc;
		}

		f >> c;
		// opposite elements
		for (uint j = 0; j < c; ++j)
		{
			f >> a;
			opp[a[0]] = a[1];
			opp[a[1]] = a[0];
			oppc[a[0]] = 0;
			oppc[a[1]] = 0;
		}
		
		f >> c >> a;
		char prev = 0;
		list<char> l;
		for (uint j = 0; j < c; ++j)
		{
			char ins = a[j];
			if (prev)
			{
				string test;
				test.resize(2);
				test[0] = prev;
				test[1] = ins;

				map<string, char>::iterator inb = nb.find(test);
				if (inb != nb.end())
				{
					ins = nb[test];
					list<char>::iterator il = l.end();
					--il;
					*il = ins;
					if (oppc.find(prev) != oppc.end())
						oppc[prev] --;
					prev = ins;
					continue;
				}
				else
				{
					if (opp.find(ins) != opp.end() && oppc[opp[ins]])
					{
						l.clear();
						for (map<char, uint>::iterator ioppc = oppc.begin(); ioppc != oppc.end(); ++ioppc)
							ioppc->second = 0;
						prev = 0;
						continue;
					}
				}
			}

			l.push_back(ins);
			if (oppc.find(ins) != oppc.end())
				oppc[ins] ++;
			prev = ins;
		}

		cout << "Case #" << i + 1 << ": [";
		if (l.size())
		{
			list<char>::iterator it = l.begin();
			cout << *it;
			for (++it; it != l.end(); ++it)
				cout << ", " << *it;
		}
		cout << "]" << endl;
	}

	return 0;
}

