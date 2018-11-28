#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>
#include <fstream>

using namespace std;

struct timetable
{
	string arrival;
	string departure;
	string type;
} tmptt;

string makeTime(string text, int minute)
{
	int hour,min;
	stringstream sstmp;
	string stmp;

	hour = atoi(text.substr(0,2).c_str());
	min = atoi(text.substr(3,2).c_str());
	
	min += minute;
	if (min > 59)
	{
		min -= 60;
		hour++;
	}
	if (hour < 10)
		sstmp << "0";
	sstmp << hour;
	sstmp << ":";
	if (min < 10)
		if (min == 0)
			sstmp << "00";
		else
			sstmp << "0";
	sstmp << min;
	sstmp >> stmp;
	
	return stmp;
}

void sort1 (vector<timetable> &schedule)
{
	int i,j;
	
	for (i=0; i<schedule.size()-1; i++)
	{
		for (j=0; j<schedule.size()-1;j++)
		{
			if (schedule[j].departure.compare(schedule[j+1].departure) > 0)
			{
				tmptt = schedule[j];
				schedule[j] = schedule[j+1];
				schedule[j+1] = tmptt;
			}
			else if (schedule[j].departure.compare(schedule[j+1].departure) == 0 && schedule[j].type == "ba")
			{
				tmptt = schedule[j];
				schedule[j] = schedule[j+1];
				schedule[j+1] = tmptt;
			}
		}
	}

}
void sort2 (vector<timetable> &schedule)
{
	int i,j;
	
	for (i=0; i<schedule.size()-1; i++)
	{
		for (j=0; j<schedule.size()-1;j++)
		{
			if (schedule[j].arrival.compare(schedule[j+1].arrival) > 0)
			{
				tmptt = schedule[j];
				schedule[j] = schedule[j+1];
				schedule[j+1] = tmptt;
			}
			else if (schedule[j].arrival.compare(schedule[j+1].arrival) == 0 && schedule[j].type == "ab")
			{
				tmptt = schedule[j];
				schedule[j] = schedule[j+1];
				schedule[j+1] = tmptt;
			}
		}
	}

}
		
int main()
{
	int z,y,count;
	int ab,ba,t, mojood;
	int ab_res, ba_res;
	vector<timetable> schedule, tmpschedule;
	ifstream infile("B-small.in");
	ofstream outfile("train.out");

	infile >> count;
	for (z=0; z<count; z++)
	{
		schedule.clear();
		infile >> t >> ab >> ba;
		for (y=0; y<ab; y++)
		{
			infile >> tmptt.arrival >> tmptt.departure;
			tmptt.type = "ab";
			schedule.push_back(tmptt);
			
		}
		for (y=0; y<ba; y++)
		{
			infile >> tmptt.departure >> tmptt.arrival;
			tmptt.type = "ba";
			schedule.push_back(tmptt);
		}

		// Check arrival
		tmpschedule.clear();
		for (y=0; y<schedule.size(); y++)
		{
			tmpschedule.push_back(schedule[y]);
			if (tmpschedule[y].type == "ba")
				tmpschedule[y].arrival = makeTime(tmpschedule[y].arrival,t);
		}
		ab_res = 0;
		mojood = 0;
		sort2(tmpschedule);
		for (y=0; y<schedule.size(); y++)
		{
			if (tmpschedule[y].type == "ab")
			{
				if (mojood == 0)
					ab_res++;
				else
					mojood--;
			}
			else
				mojood++;
					
		}
		outfile << "Case #" << z+1 << ": " << ab_res;
//		for (y=0; y<schedule.size(); y++)
//			cout << tmpschedule[y].arrival << " " << tmpschedule[y].departure << " " << tmpschedule[y].type << endl;
			
		// Check departure
		tmpschedule.clear();
		for (y=0; y<schedule.size(); y++)
		{
			tmpschedule.push_back(schedule[y]);
			if (tmpschedule[y].type == "ab")
				tmpschedule[y].departure = makeTime(tmpschedule[y].departure,t);
		}
		ba_res = 0;
		mojood = 0;
		sort1(tmpschedule);
		for (y=0; y<schedule.size(); y++)
		{
			if (tmpschedule[y].type == "ba")
			{
				if (mojood == 0)
					ba_res++;
				else
					mojood--;
			}
			else
				mojood++;
					
		}
		outfile << " " << ba_res << endl;

	}

	infile.close();
	outfile.close();
}

