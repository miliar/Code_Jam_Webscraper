#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>



struct StationTime
{
	int hour;
	int minutes;

	StationTime(int hour, int min)
	{
		this->hour = hour;
		this->minutes = min;
	}

	void add(int min)
	{
		this->minutes += min;
		if(this->minutes > 60)
		{
			this->minutes -= 60;
			this->hour++;
		}
	}

	bool operator<(const StationTime &time)
	{
		if(this->hour < time.hour)
			return true;
		else if((this->hour == time.hour) && (this->minutes < time.minutes))
			return true;
		return false;
	}

	bool lessthan(const StationTime &time, int turnaround_time)
	{
		StationTime temp(this->hour, this->minutes);
		temp.add(turnaround_time);
		if(temp.hour < time.hour)
			return true;
		else if((temp.hour == time.hour) && (temp.minutes <= time.minutes))
			return true;
		return false;
	}
};

struct Station
{
	std::vector<StationTime> *incoming;
	std::vector<StationTime> *outgoing;

	Station() 
	{ 
		incoming = new std::vector<StationTime>();
		outgoing = new std::vector<StationTime>();
	}

	void addToIncoming(StationTime &time)
	{
		incoming->push_back(time);
	}

	void addToOutgoing(StationTime &time)
	{
		outgoing->push_back(time);
	}

	void reset()
	{
		incoming->clear();
		outgoing->clear();
	}
	int re_concile(int ta_time);
};

int
Station::re_concile(int ta_time)
{
	std::sort(this->incoming->begin(), this->incoming->end());
	std::sort(this->outgoing->begin(), this->outgoing->end());
	int n = 0;
	for(unsigned int i=0; i < this->incoming->size(); ++i)
	{
		for(unsigned int j=0; j < this->outgoing->size(); ++j)
		{
			if( (*this->incoming)[i].lessthan((*this->outgoing)[j], ta_time) )
			{
				++n;
				++i;
				if( i == this->incoming->size())
					break;
				continue;
			}
		}
		break;
	}
	return n;
}

void main()
{
	Station A, B;
	std::ifstream input_file ("C:\\Temp\\B-large.in");
	std::ofstream  output_file("C:\\Temp\\output_large.out");

	if(input_file.is_open())
	{
		int case_count;
		input_file  >> case_count;
		for(int i=0; i<case_count; i++)
		{
			int turnaround_time;
			int nA, nB;
			input_file >> turnaround_time;
			input_file >> nA >> nB;
			for(int j=0; j<nA; j++)
			{
				int hour1, min1, hour2, min2;
				char sep1, sep2;
				input_file >> hour1 >> sep1 >> min1 >> hour2 >> sep2 >> min2;
				StationTime time1(hour1, min1);
				A.addToOutgoing(time1);
				StationTime time2(hour2, min2);
				B.addToIncoming(time2);
			}
			for(int j=0; j<nB; j++)
			{
				int hour1, min1, hour2, min2;
				char sep1, sep2;
				input_file >> hour1 >> sep1 >> min1 >> hour2 >> sep2 >> min2;
				StationTime time1(hour1, min1);
				B.addToOutgoing(time1);
				StationTime time2(hour2, min2);
				A.addToIncoming(time2);
			}
			int nAreq = nA - A.re_concile(turnaround_time);
			int nBreq = nB - B.re_concile(turnaround_time);
			output_file << "Case #" << (i+1) << ": " << nAreq << " " << nBreq << "\n" ;
			A.reset();
			B.reset();
		}
		input_file.close();
		output_file.close();
	}
}