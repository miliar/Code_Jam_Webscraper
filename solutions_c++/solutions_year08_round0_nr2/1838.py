#include <list>
#include <fstream>
#include <stack>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

const int size = 101;


ifstream fin("input.txt");
ofstream fout("output.txt");

class Time
{
public:
	int hh;
	int mm;
	long total;
	Time(string s)
	{
		string hStr = s.substr(0, 2);
		string mStr = s.substr(3, 2);
		hh = atoi(hStr.c_str());
		mm = atoi(mStr.c_str());
		total = hh * 60 + mm;
	}
	Time(long t)
	{
		total = t;
		hh = t / 60;
		mm = t % 60;
	}
	Time(int hh, int mm)
	{
		this->hh = hh; this->mm = mm;
		total = hh * 60 + mm;
	}
	int compare(Time * t)
	{
		if (hh < t->hh || (hh == t->hh && mm < t->mm))
		{
			return 1;
		}else if (hh == t->hh && mm == t->mm)
		{
			return 0;
		}else 
			return -1;
	}
	void print()
	{
		cout << hh << ":" << mm << endl;
	}
};
class TimeTable{
public:
	Time * start, * end;
	TimeTable(Time * s, Time * e)
	{
		start = s;
		end = e;
	}
	TimeTable(TimeTable * t)
	{
		start = new Time(t->start->hh, t->start->mm);
		end = new Time(t->end->hh, t->end->mm);
	}
};
vector<TimeTable *>aList;
vector<TimeTable *>bList;

int main()
{
	int n;
	fin >> n;
	int aNum, bNum;
	int delay;
	string timeStr;
	int i;
	for (int m=0; m<n; m++)
	{
		aList.clear();
		bList.clear();

		fin >> delay >> aNum >> bNum;
		for (i=0; i<aNum; i++)
		{
			fin >> timeStr;
			Time * s = new Time(timeStr);
			
			fin >> timeStr;
			Time * e = new Time(timeStr);
			aList.push_back(new TimeTable(s, e));
		}
		for (i=0; i<bNum; i++)
		{
			fin >> timeStr;
			Time * s = new Time(timeStr);

			fin >> timeStr;
			Time * e = new Time(timeStr);
			bList.push_back(new TimeTable(s, e));
		}
		int aNeed = 0, aCurrent = 0, bNeed = 0, bCurrent = 0;
		long current = 0;
		vector<TimeTable *> aStatusList, aWaitList, bStatusList, bWaitList;
		for(current = 0; current < 24 * 60; current ++)
		{
			for (i=aWaitList.size() - 1; i>=0; i--)
			{
				if (current == aWaitList[i]->end->total)
				{
					aCurrent++;
					//cout << "run 0" << endl;
					aWaitList.erase(aWaitList.begin() + i);
				}
			}
			for (i=bWaitList.size() - 1; i>=0; i--)
			{
				if (current == bWaitList[i]->end->total)
				{
					bCurrent++;
					//cout << "run 1" << endl;
					bWaitList.erase(bWaitList.begin() + i);
				}
			}
			for (i=aStatusList.size() -1; i>=0; i--)
			{
				TimeTable * table = aStatusList[i];
				if (current == aStatusList[i]->end->total)
				{
					//cout << "run 2" << endl;
					aStatusList.erase(aStatusList.begin() + i);
					if (delay == 0)
					{
						bCurrent ++;
					}else{
						table->end->total += delay;
						bWaitList.push_back(table);
					}
				}
			}
			for (i=bStatusList.size() - 1; i>=0; i--)
			{
				TimeTable * table = bStatusList[i];
				if (current == bStatusList[i]->end->total)
				{
					//cout << "run 3" << endl;
					bStatusList.erase(bStatusList.begin() + i);
					if (delay == 0)
					{
						aCurrent ++;
					}else{
						table->end->total += delay;
						aWaitList.push_back(table);
					}
				}
			}
			for (i=0; i<aList.size(); i++)
			{
				TimeTable * table = aList[i];
				if (table->start->total == current)
				{
					aStatusList.push_back(new TimeTable(table));
					if (aCurrent == 0)
					{
						aNeed ++;
					}else
						aCurrent --;
				}
			}
			for (i=0; i<bList.size(); i++)
			{
				TimeTable * table = bList[i];
				if (table->start->total == current)
				{
					bStatusList.push_back(new TimeTable(table));
					if (bCurrent == 0)
					{
						bNeed ++;
					}else
						bCurrent --;
				}
			}
			
		}
		fout << "Case #" << m+1<<": "<< aNeed <<" " << bNeed << endl;
	}
	return 0;
}