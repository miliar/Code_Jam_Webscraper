#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define PB push_back
#define For(i,n) for (i = 0; i < n; i++)
#define bend(v) v.begin (), v.end ()

ifstream fin("input.in");
ofstream fout("output.out");

class Event
{
public:
	int minutes;
	int hours;
	int type; // 0 = a train is ready and 1 means a train should be ready
	int station; // 0 = A and 1 = B

	Event(int minutes, int hours, int type, int station)
	{
		this->hours = hours;
		this->minutes = minutes;
		this->type = type;
		this->station = station;
	}
};

bool operator < (const Event &a, const Event &b)
{
	if (a.hours > b.hours)
		return true;
	else if (a.hours < b.hours)
		return false;
	else if (a.minutes > b.minutes)
		return true;
	else if (a.minutes < b.minutes)
		return false;
	else if (a.type > b.type)
		return true;
	return false;
}

int tempH, tempM;

void add(int h, int m, int t)
{
	m += t;
	if (m >= 60)
	{
		m -= 60;
		h++;
	}
	if (h >= 24)
	{
		h = -1;
		m = -1;
	}
	tempH = h;
	tempM = m;
}

int main ()
{
	int tno;
	fin >> tno;

	for (int ts = 0; ts < tno; ts++)
	{

		priority_queue<Event> events;


		int  A= 0, B = 0;
		int t;
		fin >> t;

		int h, m, na, nb;
		char c;

		fin >> na >> nb;

		for (int i = 0; i < na; i++)
		{
			fin >> h >> c >> m;
			events.push(Event(m, h, 1, 0));

			fin >> h >> c >> m;
			add(h, m, t);
			if (tempH != -1 && tempM != -1)
				events.push(Event(tempM, tempH, 0, 1));

		}

		for (int i = 0; i < nb; i++)
		{
			fin >> h >> c >> m;
			events.push(Event(m, h, 1, 1));

			fin >> h >> c >> m;
			add(h, m, t);
			if (tempH != -1 && tempM != -1)
				events.push(Event(tempM, tempH, 0, 0));
		}

		int curra = 0, currb = 0;
		while (! events.empty())
		{
			Event e = events.top();
			events.pop();
			if (e.type == 0) // a train is here
			{
				if (e.station == 0)
				{
					curra++;
				}
				else
				{
					currb++;
				}
			}
			else
			{
				if (e.station == 0)
				{
					if (curra != 0)
						curra--;
					else
						A++;
				}
				else
				{
					if (currb != 0)
						currb--;
					else
						B++;
				}
			}
		}





		fout << "Case #" << ts + 1 << ": " << A << " " << B << endl;
		
	}

	return 0;
}