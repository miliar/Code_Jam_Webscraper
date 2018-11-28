// CodeJam.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>

using namespace std;

struct entry{
	
	entry(int time, bool arr, bool sta)
		:time(time), arr(arr), sta(sta)
	{
	}

	int time, arr, sta;

	bool operator< (const entry& entry )
	{
		if ( time < entry.time )
			return true;
		if ( time > entry.time )
			return false;
		if ( arr )
			return true;
		if ( entry.arr )
			return false;

		return sta < entry.sta;
	}
};

int htom(const string& h)
{
	vector<int> n(4);
	n[0] = int(h[0] - '0');
	n[1] = int(h[1] - '0');
	n[2] = int(h[3] - '0');
	n[3] = int(h[4] - '0');
	for ( int j = 0; j < 4; j++ )
		cout << n[j];
	cout << " ";
	return (n[0]*10+n[1])*60+(n[2]*10+n[3]); 
}

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int cases;
	in >> cases;

	for ( int i = 0; i < cases; i++ )
	{

		int turn;
		int na, nb;
		in >> turn >> na >> nb;
		vector<entry> table;


		for ( int j = 0; j < na; j++ )
		{
			string dep; string arr;
			in >> dep >> arr;

			int tdep = htom(dep);
			int tarr = htom(arr) + turn;
			entry edep(tdep, false, true);
			entry earr(tarr, true, false);

			table.push_back(edep);
			table.push_back(earr);
		}
		
		for ( int j = 0; j < nb; j++ )
		{
			string dep; string arr;
			in >> dep >> arr;

			int tdep = htom(dep);
			int tarr = htom(arr) + turn;
			entry edep(tdep, false, false);
			entry earr(tarr, true, true);

			cout << "\n" << tdep << " " << tarr;
			table.push_back(edep);
			table.push_back(earr);
		}

		sort(table.begin(), table.end());

		int trainsa = 0, trainsb = 0;
		int neededa = 0, neededb = 0;


		for ( int j = 0; j < table.size(); j++ )
		{
			if ( table[j].arr )
			{
				if ( table[j].sta )
				{
					trainsa++;
				} else 
				{
					trainsb++;
				}
			} else {
				if ( table[j].sta )
				{
					if ( trainsa )
						trainsa--;
					else
						neededa++;
				} else 
				{
					if ( trainsb )
						trainsb--;
					else
						neededb++;
				}
			}
		}

		out << "Case #" << (i+1) << ": " << neededa << " " << neededb <<  "\n";

	}
	return 0;
}

