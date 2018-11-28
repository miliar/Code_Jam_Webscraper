#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <sstream>

using namespace std;

class TrainTimetable
{
public:
	static pair<int, int> getTrains(vector<pair<int, int> > timesA, vector<pair<int, int> > timesB)
	{
		if (timesA.size() == 0)
			return pair<int, int>(0, timesB.size());
		if (timesB.size() == 0)
			return pair<int, int>(timesA.size(), 0);
		pair<int, int> res = make_pair(0, 0);
		pair<int, int> a = timesA[0];
		pair<int, int> b = timesB[0];
		int arrtime = 0;
		if (a < b)
		{
			arrtime = a.second;
			timesA.erase(timesA.begin());
			res.first = 1;
		}
		else
			res.second = 1;

		while (true)
		{
			pair<int, int> toSearchB(arrtime, 0);
			vector<pair<int, int> >::iterator iterB = lower_bound(timesB.begin(), timesB.end(), toSearchB);
			if (iterB == timesB.end()) 
				break;

			pair<int, int> toSearchA(iterB->second, 0);
			timesB.erase(iterB);
			vector<pair<int, int> >::iterator iterA = lower_bound(timesA.begin(), timesA.end(), toSearchA);
			if (iterA == timesA.end()) 
				break;
			arrtime = iterA->second;
			timesA.erase(iterA);
		}

		pair<int, int> rec = getTrains(timesA, timesB);
		res.first += rec.first;
		res.second += rec.second;

		return res;
	}
};

int main()
{
	ifstream ifstr("B-large.in");
	ofstream ofstr("B-large.out");
	int count;
	ifstr >> count;
	for (int i = 1; i <= count; ++i)
	{
		int t;
		ifstr >> t;
		int counta, countb;
		ifstr >> counta >> countb;
		vector<pair<int, int> > timesA, timesB;
		for (int j = 0; j < counta; ++j)
		{
			string temp;
			ifstr >> temp;
			replace(temp.begin(), temp.end(), ':', ' ');
			istringstream istr1(temp);
			int h1, m1;
			istr1 >> h1 >> m1;
			ifstr >> temp;
			replace(temp.begin(), temp.end(), ':', ' ');
			istringstream istr2(temp);
			int h2, m2;
			istr2 >> h2 >> m2;
			timesA.push_back(make_pair(60 * h1 + m1, 60 * h2 + m2 + t));
		}
		for (int j = 0; j < countb; ++j)
		{
			string temp;
			ifstr >> temp;
			replace(temp.begin(), temp.end(), ':', ' ');
			istringstream istr1(temp);
			int h1, m1;
			istr1 >> h1 >> m1;
			ifstr >> temp;
			replace(temp.begin(), temp.end(), ':', ' ');
			istringstream istr2(temp);
			int h2, m2;
			istr2 >> h2 >> m2;
			timesB.push_back(make_pair(60 * h1 + m1, 60 * h2 + m2 + t));
		}
		
		std::sort(timesA.begin(), timesA.end());
		std::sort(timesB.begin(), timesB.end());
		pair<int, int> p = TrainTimetable::getTrains(timesA, timesB);
		ofstr << "Case #" << i << ": " << p.first << " " << p.second << "\n";
	}

	return 0;
}
