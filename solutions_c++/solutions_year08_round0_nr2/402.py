#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <utility>
#include <functional>

using namespace std;
enum Station {A,B};
typedef size_t Ticks;
struct Schedule
{
	Station type;
	Ticks	start;
	Ticks	end;
	bool operator<(const Schedule s)
	{
		return start < s.start;
	}
};
Ticks TimeToTicks(std::string strTime)
{
	Ticks ticks = 0;
	ticks = atoi(&(strTime.c_str()[3]));
	strTime.resize(2);
	ticks += atoi(strTime.c_str())*60;
	return ticks;
}
int main()
{
	int i,j,testCases;
	size_t turnAround;
	string departTime,arriveTime;
	cin >> testCases;
	vector<Ticks> hA,hB;
	vector<Schedule> timeTable;
	size_t cA,cB;
	int nA,nB;
	for (i = 1; i <= testCases; i ++)
	{
		hA.clear();
		hB.clear();
		make_heap(hA.begin(),hA.end(),greater<Ticks>());
		make_heap(hB.begin(),hB.end(),greater<Ticks>());
		timeTable.clear();
		cA = 0;
		cB = 0;
		cin >> turnAround >> nA >> nB;

		Schedule s;
		s.type = A;
		for (j = 0; j < nA; j ++)
		{
			cin >> departTime >> arriveTime;
			s.start = TimeToTicks(departTime);
			s.end = TimeToTicks(arriveTime);
			timeTable.push_back(s);
		}
		s.type = B;
		for (j = 0; j < nB; j ++)
		{
			cin >> departTime >> arriveTime;
			s.start = TimeToTicks(departTime);
			s.end = TimeToTicks(arriveTime);
			timeTable.push_back(s);
		}
		sort(timeTable.begin(),timeTable.end());
		size_t k;
		for (k = 0; k < timeTable.size(); k ++)
		{
			switch(timeTable[k].type)
			{
			case A:
				if (hA.empty() || hA[0] > timeTable[k].start)
				{
					cA ++;
				}
				else
				{
					pop_heap(hA.begin(),hA.end(),greater<Ticks>());
					hA.pop_back();
				}
				hB.push_back(timeTable[k].end+turnAround);
				push_heap(hB.begin(),hB.end(),greater<Ticks>());
				break;
			case B:
				if (hB.empty() || hB[0] > timeTable[k].start)
				{
					cB ++;
				}
				else
				{
					pop_heap(hB.begin(),hB.end(),greater<Ticks>());
					hB.pop_back();
				}
				hA.push_back(timeTable[k].end+turnAround);
				push_heap(hA.begin(),hA.end(),greater<Ticks>());
				break;
			default:
				break;
			}
		}
		cout << "Case #" << i << ": " << cA << " " << cB << "\n";
	}
	return 0;
}
