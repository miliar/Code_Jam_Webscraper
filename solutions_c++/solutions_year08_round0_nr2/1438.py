#include <iostream>
#include <list>
#include <deque>
#include <algorithm>
using namespace std;

enum Station { A = 0, B = 1 };

struct Trip
{
	int dep, arr;
	Station from;
	
	Trip(Station f, int d, int a): dep(d), arr(a), from(f)
	{
	}
	Station to()
	{
		if (from == A)
			return B;
		return A;
	}
};

struct SortByDep
{
	bool operator()(const Trip& t1, const Trip& t2) const 
	{
		return t1.dep < t2.dep;
	}
};

struct IsGreater
{
	bool operator()(const int& i1, const int& i2) const 
	{
		return i1 > i2;
	}
};

int main(int argc, char** argv)
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		list<Trip> timetable;
		int t, na, nb;
		cin >> t;
		cin >> na >> nb;
		for (int j = 1; j <= na; j++)
		{
			int h1, m1, h2, m2;
			cin >> h1;
			cin.ignore(1, ':');
			cin >> m1 >> h2;
			cin.ignore(1, ':');
			cin >> m2;
			timetable.push_back( Trip(A, h1 * 60 + m1, h2 * 60 + m2) );
		}
		
		for (int j = 1; j <= nb; j++)
		{
			int h1, m1, h2, m2;
			cin >> h1;
			cin.ignore(1, ':');
			cin >> m1 >> h2;
			cin.ignore(1, ':');
			cin >> m2;
			timetable.push_back( Trip(B, h1 * 60 + m1, h2 * 60 + m2) );
		}
		timetable.sort(SortByDep());	
		
		int tn[2] = { 0 };
		deque<int> stations[2];
		for (list<Trip>::iterator it = timetable.begin(); it != timetable.end(); it++)
		{
			Trip trip = *it;
			deque<int>& from = stations[trip.from];
			deque<int>& to = stations[trip.to()];
			
			if (from.empty() || (from.front() > trip.dep))
			{
				tn[(*it).from]++;
				to.push_back(trip.arr + t);
				push_heap(to.begin(), to.end(), IsGreater());
				continue;
			}
			
			pop_heap(from.begin(), from.end(), IsGreater());
			from.pop_back();
			to.push_back(trip.arr + t);
			push_heap(to.begin(), to.end(), IsGreater());
			continue;
		}
		cout << "Case #" << i << ": " << tn[0] << " " << tn[1] << endl;
	
	}
	return 0;
}
