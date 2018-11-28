#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
class HHMM
{
public:
	int _hour;
	int _minute;
	int _type;

	HHMM(int hour,int minute, int type)
	{
		_hour = hour;
		_minute =minute;
		_type = type;
		if (_minute>=60)
		{
			_hour += (_minute-_minute%60)/60;
			_hour %= 24; 
			_minute = _minute %60;
		}
	}
	HHMM & operator+(int minut)
	{
		_minute += minut;
		if (_minute >= 60)
		{
			_hour +=(_minute-_minute%60)/60;
			_hour %=24;
			_minute = _minute % 60;
		}
		return *this;
	}
	bool operator <(const HHMM & next)
	{
		if (this->_hour > next._hour)
		{
			return false;
		}
		else if (this->_hour == next._hour && this->_minute > next._minute)
		{
			return false;
		}
		else
		{
			return true;
		}

	}
	bool operator==(const HHMM &next)
	{
		return (this->_hour == next._hour) && (this->_minute==next._minute);
	}

};

class SortedTimeList
{
private:
	vector<HHMM> _schedule;
	
public:
	SortedTimeList()
	{
	}
	void Insert(HHMM t)
	{
		bool done= false;
		vector<HHMM>::iterator it = _schedule.begin();
		for ( ;it != _schedule.end();it++)
		{
			if(t == *it)
			{
				it->_type+=t._type;
				done =  true;
				break;
			}

			if (t<*it)
			{
				_schedule.insert(it,t);
				done = true;
				break;
			}
			
		}
		if (!done)
		{
			_schedule.push_back(t);
		}
		
	}
	int Count() const
	{
		int res= 0;
		int cnt = 0;
		for (vector<HHMM>::const_iterator cit = _schedule.begin(); cit != _schedule.end(); ++cit)
		{
			
			cnt += cit->_type;
			if (res < cnt)
				{
					res = cnt;
				}
			
		}
		return res;
	}

};
int main()
{

		FILE *fin=fopen("test.in","r");
		ofstream fout("test.out");

		int N = 0;
		fscanf(fin,"%d",&N);

		for (int i = 0; i < N; i++)
		{
			int T = 0;
			fscanf(fin,"%d",&T);
			
			int cntA = 0, cntB = 0;
			fscanf(fin,"%d %d",&cntA,&cntB);
			SortedTimeList lsA, lsB;

			int hour,minute;
			for (int j =0; j< cntA; j++)
			{
				fscanf(fin,"%d:%d",&hour,&minute);
				cout<<hour<<":"<<minute<<"   ";
				lsA.Insert(HHMM(hour,minute,1));
				fscanf(fin,"%d:%d",&hour,&minute);
				cout<<hour<<":"<<minute<<endl;
				lsB.Insert(HHMM(hour,minute+T,-1));
			}
			for (int j= 0; j<cntB;j++)
			{
				fscanf(fin,"%d:%d",&hour,&minute);
				lsB.Insert(HHMM(hour,minute,1));
				fscanf(fin,"%d:%d",&hour,&minute);
				lsA.Insert(HHMM(hour,minute+T,-1));
			}
			fout<<"Case #"<<i+1<<": "<<lsA.Count()<<" "<<lsB.Count()<<endl;
		}

		fclose(fin);
		fout.close();

		return 0;
}
