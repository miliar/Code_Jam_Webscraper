//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

bool is_ok(int x, int note)
{
	return x%note == 0 || note%x == 0;
}

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
		int players_count, _min, _max;
		f >> players_count;
		f >> _min;
		f >> _max;
		vector<int> players(players_count);
		for (int i=0; i<players_count; i++)
			f >> players[i];

		bool found = false;
		int i = _min;
		for (; i<=_max && !found; i++)
		{
			bool ok = true;
			for (int j=0; j<players_count && ok; j++)
				ok = is_ok(i, players[j]);

			found = ok;
		}

		cout << "Case #" << _case << ": ";
		if (found)
			cout << i-1 << endl;
		else
			cout << "NO" << endl;
	}
}
