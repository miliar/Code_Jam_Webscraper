using namespace std;
#include <iostream>
#include <map>
#include <vector>

int process(map<int, int> o, map<int, int> b)
{
	map<int, int>::iterator oiter=o.begin();
	map<int, int>::iterator biter=b.begin();

	int opos=1;
	int bpos=1;

	int time=0;
	
	while (oiter != o.end() || biter != b.end())
	{
		if (biter == b.end() || (oiter != o.end() && oiter->first < biter->first))
		{
			if (biter!=b.end() && bpos < biter->second)
				++bpos;
			else if (biter!=b.end() && bpos > biter->second)
				--bpos;
			
			if (oiter!=o.end() && opos == oiter->second)
				++oiter; //push button
			else if (oiter!=o.end() && opos < oiter->second)
				++opos;
			else if (oiter!=o.end() && opos > oiter->second)
				--opos;
		}
		else
		{
			if (oiter!=o.end() && opos < oiter->second)
				++opos;
			else if (oiter!=o.end() && opos > oiter->second)
				--opos;
			
			if (biter!=b.end() && bpos == biter->second)
				++biter; //push button
			else if (biter!=b.end() && bpos < biter->second)
				++bpos;
			else if (biter!=b.end() && bpos > biter->second)
				--bpos;
		}

		++time;
	}
	
	return time;
}

int main()
{
	map<int, int> o;
	map<int, int> b;
	vector<int> results;

	int cases;
	int cindex=1;
	int moves;

	char who;
	int where;

	int priority=1;

	cin >> cases;
	while (cases>0)
	{
		cin >> moves;
		while (moves>0)
		{
			cin >> who >> where;

			if (who == 'O')
				o.insert( pair<int, int>(priority, where) );
			else
				b.insert( pair<int, int>(priority, where) );

			++priority;
			--moves;
		}

		//process case
		results.push_back(process(o, b));

		o.clear();
		b.clear();
		priority=1;
		
		--cases;
		++cindex;
	}
	
	int index=1;
	for (vector<int>::iterator iter=results.begin(); iter!=results.end(); iter++)
		cout << "Case #" << index++ << ": " << *iter << endl;

	return 0;
}