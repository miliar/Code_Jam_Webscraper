#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Time
{
public:
	int minutes;	
};

class Trip
{
public:
	Time t1, t2;
	bool isAb;
	bool isDeparted;
	bool isClosed;
	int trainId;

	Trip() : trainId(-1), isDeparted(false), isClosed(false) {}
};

istream &operator>>(istream &in, Time &t)
{
	int h, m;
	in >> h;
	in.get();
	in >> m;
	t.minutes = h*60 + m;
	return in;
}

ostream &operator<<(ostream &out, Time &t)
{
	out << setw(2) << setfill('0') << t.minutes/60 << ":" << setw(2) << t.minutes%60;
	return out;
}

void RunTest(ifstream &in, int &outA, int &outB)
{
	int t, na, nb;
	outA = 0;
	outB = 0;

	in >> t >> na >> nb;
//	cout << "t: " << t << " na: " << na << " nb: " << nb << endl;

	vector<Trip> table(na + nb);
	for(int i = 0; i < na; i++)
	{
		Trip t;
		in >> t.t1 >> t.t2;
		t.isAb = true;
		table[i] = t;
	}

	for(int i = 0; i < nb; i++)
	{
		Trip t;
		in >> t.t1 >> t.t2;
		t.isAb = false;
		table[i + na] = t;
	}

	while(1)
	{
		// find free min starting time
		int minTime = 9999999;
		int minIndex = -1;
		for(unsigned i = 0; i < table.size(); i++)
		{
			if(!table[i].isDeparted && table[i].t1.minutes < minTime)
			{
				minTime = table[i].t1.minutes;
				minIndex = i;
			}
		}

		if(minIndex == -1)
			break;

		Trip &toGo = table[minIndex];

		int waitingTime = 9999999;
		int waitingIndex = -1;

		for(unsigned i = 0; i < table.size(); i++)
		{
			if(!table[i].isClosed && table[i].isDeparted && table[i].isAb != toGo.isAb && table[i].t2.minutes + t <= toGo.t1.minutes
				&& table[i].t2.minutes < waitingTime)
			{
				waitingTime = table[i].t2.minutes;
				waitingIndex = i;
			}
		}

		toGo.isDeparted = true;

		if(waitingIndex != -1)
		{
			Trip &toCont = table[waitingIndex];
			toCont.isClosed = true;
		}
		else
		{
			if(toGo.isAb)
				outA++;
			else
				outB++;
		}
	}
}


int main(int argc, char* argv[])
{
	if(argc != 2)	cout << "specify input file";
	ifstream in(argv[1]);

	int n;
	in >> n;

	for(int i = 0; i < n; i++)
	{
		int a, b;
		RunTest(in, a, b);
		cout << "Case #" << (i + 1) << ": " << a << " " << b << endl;
	}

	return 0;
}
