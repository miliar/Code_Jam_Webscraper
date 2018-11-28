#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
using namespace std;


struct node
{
	int hour;
	int minute;
};
typedef struct node DateTime;

struct node1
{
	string start;
	string end;
	string station;
};

typedef struct node1 TimeSchedule;

bool TimeCompare(const TimeSchedule& t1, const TimeSchedule& t2)
{
	return t1.start < t2.start ;
}

DateTime ParseTime(string t)
{
	const char *str = t.c_str();
	DateTime dateTime;
	dateTime.hour = (int)(str[0]-'0')*10 + (int)(str[1]-'0');
	dateTime.minute = (int)(str[3]-'0')*10 + (int)(str[4]-'0');
	return dateTime;
}

DateTime AddDateTime(DateTime t1, int t2)
{
	DateTime sumTime;
	if(t1.minute+t2 >= 60)
	{
		sumTime.minute = (t1.minute+ t2) % 60;
		sumTime.hour = t1.hour + (t1.minute+ t2)/60;
	}
	else 
	{
		sumTime.minute = t1.minute+ t2;
		sumTime.hour = t1.hour;
	}
	return sumTime;
}
string ConverteToString(DateTime t)
{
	char str[6];
	str[0] = (char)(t.hour/10 + '0');
	str[1] = (char)(t.hour%10 + '0');
	str[2] = ':';
	str[3] = (char)(t.minute/10 + '0');
	str[4] = (char)(t.minute%10 + '0');
	str[5] = '\0';
	
	string tempString(str);
	return tempString;

}

int main()
{
	int NACount, NBCount;
	vector<TimeSchedule> timeScheduleVector;
	vector<TimeSchedule>::iterator timeScheduleIterator;
	vector<string> NABuffer, NBBuffer;
	vector<string>::iterator NABufferIterator, NBBufferIterator; 
	ofstream fout;
	fout.open("output.txt");
	int testCase;
	cin >> testCase;
	for(int i = 0 ; i<testCase; i++)
	{
		timeScheduleVector.clear();
		NABuffer.clear();
		NBBuffer.clear();
		//read turnRound time
		int turnRound = 0;
		cin >> turnRound;
		//read the number of trains sending in station A and B.
		int NATrains, NBTrains;
		cin >> NATrains >> NBTrains;

		string startTime, endTime;
		for(int j = 0 ; j<NATrains; j++)
		{
			cin >> startTime >> endTime;
			TimeSchedule time;
			time.start = startTime;
			time.end = endTime;
			time.station = "A";
			timeScheduleVector.push_back(time);
		}
		for(int j = 0 ; j<NBTrains; j++)
		{
			cin >> startTime >> endTime;
			TimeSchedule time;
			time.start = startTime;
			time.end = endTime;
			time.station = "B";
			timeScheduleVector.push_back(time);
		}
			
		sort(timeScheduleVector.begin(), timeScheduleVector.end(), TimeCompare);
		NACount = 0;
		NBCount = 0;

		for(timeScheduleIterator = timeScheduleVector.begin(); timeScheduleIterator != timeScheduleVector.end(); timeScheduleIterator ++)
		{
			
			//NA station
			if(timeScheduleIterator->station == "A")
			{
				int flag = 0;
				for(NABufferIterator = NABuffer.begin(); NABufferIterator != NABuffer.end(); NABufferIterator ++)
				{
					DateTime tempTime = ParseTime(*NABufferIterator);
					tempTime = AddDateTime(tempTime, turnRound);
					string tempString = ConverteToString(tempTime);
					if(tempString <= timeScheduleIterator->start)
					{
						NABuffer.erase(NABufferIterator);
						flag = 1;
						NBBuffer.push_back(timeScheduleIterator->end);
						break;
					}
				}
				if(flag == 0)
				{
					NACount ++;
					NBBuffer.push_back(timeScheduleIterator->end);
				}
			}

			//NB station
			if(timeScheduleIterator->station == "B")
			{
				int flag = 0;
				for(NBBufferIterator = NBBuffer.begin(); NBBufferIterator != NBBuffer.end(); NBBufferIterator ++)
				{
					DateTime tempTime = ParseTime(*NBBufferIterator);
					tempTime = AddDateTime(tempTime, turnRound);
					string tempString = ConverteToString(tempTime);
					if(tempString <= timeScheduleIterator->start)
					{
						NBBuffer.erase(NBBufferIterator);
						flag = 1;
						NABuffer.push_back(timeScheduleIterator->end);
						break;
					}
				}
				if(flag == 0)
				{
					NBCount ++;
					NABuffer.push_back(timeScheduleIterator->end);
				}
			}
		}

		fout << "Case #"<< i+1 << ": " << NACount << " "<< NBCount << endl;
	
	}
	fout.close();
}