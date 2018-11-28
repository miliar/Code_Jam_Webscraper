#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <iostream>
#include <utility>
#include <sstream>
#include <cstring>
#include <boost/dynamic_bitset.hpp>
#include <boost/regex.hpp>


//use library: boost
//http://www.boost.org/


using namespace std;
using namespace boost;
template<typename T> void P(T& t)
{
	cerr << t << endl;
}

enum Station { STA, STB };

struct TTime
{
	enum Station from;
	int start;
	int end;
	TTime(Station f, int s, int e) : from(f), start(s), end(e) {}

	void print()
	{
		cerr << (from ? "B" : "A") << ":" << start << "~" << end << endl; 
	}

};


struct TTimeCompare
{
	bool operator()(const TTime &a, const TTime &b)
	{
		if(a.start < b.start)
		{
			return true;

		}
		else if(a.start > b.start)
		{
			return false;
		}
		else
		{
			return a.end < b.end;
		}
	}
};


struct Train
{
	Station waitOn;
	int okTime;
	
	Train(Station w, int t) : waitOn(w), okTime(t) {}

};

TTime makeTTime(Station st, smatch &m)
{
	int hour = atoi(m.str(1).c_str());
	int min = atoi(m.str(2).c_str());
	int houre = atoi(m.str(3).c_str());
	int mine = atoi(m.str(4).c_str());
	cerr << hour << ":" << min <<  "`" << houre << ":" << mine << endl;

	return TTime(st, hour * 60 + min, houre * 60 + mine);

}


pair<int, int> calcTimeTable()
{
	int tat, na, nb;
	cin >> tat >> na >> nb;
	string s;
	getline(cin, s);
	s.reserve(100);

	vector<TTime> timeTable;
	timeTable.reserve(100);

	regex reg( "(\\d+):(\\d+) (\\d+):(\\d+)" );
	smatch match;

	for(int i=0; i<na; i++)
	{
		getline(cin, s);
		if(!regex_search(s, match, reg))
		{
			cerr << "error:" << s << endl;
			exit(1);
		}
		timeTable.push_back(makeTTime(STA, match));

		
	
	}

	for(int i=0; i<nb; i++)
	{
		getline(cin, s);
		if(!regex_search(s, match, reg))
		{
			cerr << "error:" << s << endl;
			exit(1);
		}
		timeTable.push_back(makeTTime(STB, match));
	}
	
	sort(timeTable.begin(), timeTable.end(), TTimeCompare());
	for(int i=0;i<timeTable.size();i++)
	{
		timeTable[i].print();	
	}

	vector<Train> trains;

	int useA = 0;
	int useB = 0;

	for(int i=0;i<timeTable.size();i++)
	{
		TTime &tm = timeTable[i];
			
		bool newTrain = true;
		for(int j=0;j<trains.size();j++)
		{
			Train& train = trains[j];
			if(tm.from == train.waitOn && train.okTime <= tm.start)
			{
				train.okTime = tm.end + tat;
				train.waitOn = train.waitOn == STA ? STB : STA;
				newTrain = false;
				break;
			}
		}
		if(newTrain)
		{
			if(tm.from == STA)
			{
				useA++;
			}
			else
			{
				useB++;
			}
			trains.push_back(Train(tm.from == STA ? STB : STA, tm.end + tat));
		}
			
	}
	return make_pair(useA, useB);


}

int main()
{
	
	int testcaseCount;
	cin >> testcaseCount;

	for(int i=0;i<testcaseCount;i++)
	{
		pair<int, int> result = calcTimeTable();
		printf("Case #%d: %d %d\n", i+1, result.first, result.second);  
	}

	cerr << "OK" << endl;
}

