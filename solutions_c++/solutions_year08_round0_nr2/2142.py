// code.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


const int minutes_in_houre = 60;

class my_time
{
private:
	int time_mm, time_hh;
public:
	my_time()
	{
		time_mm=0; 
		time_hh=0;
	};
	my_time(int minutes)
	{
		time_mm = minutes % minutes_in_houre; 
		time_hh = minutes / minutes_in_houre;
	};
	my_time(const my_time& other)
	{
		time_mm = other.get_MM();
		time_hh = other.get_HH();
	}
	my_time& operator+(my_time& second)
	{
		my_time res(*this);
		res.set_MM(res.get_MM() + second.get_MM());
		res.set_HH(res.get_HH() + second.get_HH() + res.get_MM()/minutes_in_houre);
		res.set_MM(res.get_MM() % minutes_in_houre);
		return res;
	}
	my_time& operator+(const int& second)
	{
		my_time res(second);
		res.set_MM(res.get_MM() + get_MM());
		res.set_HH(res.get_HH() + get_HH() + res.get_MM()/minutes_in_houre);
		res.set_MM(res.get_MM() % minutes_in_houre);
		return res;
	}
	bool operator==(my_time& b)
	{
		return ((get_HH()==b.get_HH())&&(get_MM()==b.get_MM()));
	}
	bool operator>(my_time& b)
	{
		return (get_HH()*60+get_MM() > b.get_HH()*60+b.get_MM());
	}
	bool operator<(my_time& b)
	{
		return (get_HH()*60+get_MM() < b.get_HH()*60+b.get_MM());
	}
	bool operator>=(my_time& b)
	{
		return (get_HH()*60+get_MM() >= b.get_HH()*60+b.get_MM());
	}
	bool operator<=(my_time& b)
	{
		return (get_HH()*60+get_MM() <= b.get_HH()*60+b.get_MM());
	}
	int get_MM() const { return time_mm; };
	int get_HH() const { return time_hh; };
	void set_MM(int MM) { time_mm = MM; };
	void set_HH(int HH)	{ time_hh = HH; };
};

struct raise
{
	my_time from, to;
	bool used;
};

struct result_structure
{ 
	int A_station_trains_count, B_station_trains_count; 
};

typedef std::vector<raise> raise_vector;

struct source_structure
{
	int turnaround_time, A_station_reises_count, B_station_reises_count; 
	raise_vector A_2_B_raises, B_2_A_raises;
};


typedef std::vector<source_structure> vector_source_structure;

struct train
{
	char station, started_from;
	my_time ready_time;	
};


//////////////////////////////////////////////////////////////////////////

void sort_vectors(source_structure& source)
{
	int min = 0; raise temp; 
	for (int i =  0; i < source.A_station_reises_count; i++)
	{
		min = i;
		for (int j =  i + 1; j < source.A_station_reises_count; j++)
			if ((source.A_2_B_raises.at(j).from.get_HH() < source.A_2_B_raises.at(min).from.get_HH()) ||
				((source.A_2_B_raises.at(j).from.get_HH() == source.A_2_B_raises.at(min).from.get_HH()) && 
				(source.A_2_B_raises.at(j).from.get_MM() < source.A_2_B_raises.at(min).from.get_MM()))) 
				min = j;
		if (min != i)
		{
			temp = source.A_2_B_raises.at(min);
			source.A_2_B_raises.at(min) = source.A_2_B_raises.at(i);
			source.A_2_B_raises.at(i) = temp;
		}
		source.A_2_B_raises.at(i).used = false;
	}
	for (int i =  0; i < source.B_station_reises_count; i++)
	{
		min = i;
		for (int j =  i + 1; j < source.B_station_reises_count; j++)
			if ((source.B_2_A_raises.at(j).from.get_HH() < source.B_2_A_raises.at(min).from.get_HH()) ||
				((source.B_2_A_raises.at(j).from.get_HH() == source.B_2_A_raises.at(min).from.get_HH()) && 
				(source.B_2_A_raises.at(j).from.get_MM() < source.B_2_A_raises.at(min).from.get_MM()))) 
				min = j;
		if (min != i)
		{
			temp = source.B_2_A_raises.at(min);
			source.B_2_A_raises.at(min) = source.B_2_A_raises.at(i);
			source.B_2_A_raises.at(i) = temp;
		}
		source.B_2_A_raises.at(i).used = false;
	}
}

void startup_train_filler(source_structure& source, std::vector<train>& trains, int& count_a, int& count_b)
{
	if ((source.A_station_reises_count > 0) && (source.B_station_reises_count > 0))
	{
		if (source.A_2_B_raises.at(0).from == source.B_2_A_raises.at(0).from)
		{
			count_a = 1; count_b = 1;
			source.A_2_B_raises.at(0).used = true; source.B_2_A_raises.at(0).used = true; 
			trains.resize(2);
			trains.at(0).started_from = 'A';
			trains.at(0).station = 'B';
			trains.at(0).ready_time = source.A_2_B_raises.at(0).to + my_time(source.turnaround_time);
			trains.at(1).started_from = 'B';
			trains.at(1).station = 'A';
			trains.at(1).ready_time = source.B_2_A_raises.at(0).to + my_time(source.turnaround_time);
		}
		else
		{
			my_time minimum_timeA(24*60);
			for (int stA = 0; stA < source.A_2_B_raises.size(); stA++) 
				if (source.A_2_B_raises.at(stA).from < minimum_timeA) minimum_timeA = source.A_2_B_raises.at(stA).from;
			my_time minimum_timeB(24*60);
			for (int stB = 0; stB < source.B_2_A_raises.size(); stB++) 
				if (source.B_2_A_raises.at(stB).from < minimum_timeB) minimum_timeB = source.B_2_A_raises.at(stB).from;
			if (minimum_timeA < minimum_timeB)
			{
				trains.resize(trains.size()+1);
				trains.at(trains.size()-1).ready_time.set_HH(0);
				trains.at(trains.size()-1).ready_time.set_MM(0);
				trains.at(trains.size()-1).started_from = 'A';
				trains.at(trains.size()-1).station = 'A';		
				count_a++;
			}
			else if (minimum_timeA > minimum_timeB)
			{
				trains.resize(trains.size()+1);
				trains.at(trains.size()-1).ready_time.set_HH(0);
				trains.at(trains.size()-1).ready_time.set_MM(0);
				trains.at(trains.size()-1).started_from = 'B';
				trains.at(trains.size()-1).station = 'B';
				count_b++;
			} 
			else 
			{
				trains.resize(trains.size()+1);
				trains.at(trains.size()-1).ready_time.set_HH(0);
				trains.at(trains.size()-1).ready_time.set_MM(0);
				trains.at(trains.size()-1).started_from = 'A';
				trains.at(trains.size()-1).station = 'A';		
				count_a++;

				trains.resize(trains.size()+1);
				trains.at(trains.size()-1).ready_time.set_HH(0);
				trains.at(trains.size()-1).ready_time.set_MM(0);
				trains.at(trains.size()-1).started_from = 'B';
				trains.at(trains.size()-1).station = 'B';
				count_b++;
			}
		}
	}
	else
	{
		if (source.A_station_reises_count > 0)
		{
			count_a = 1;
			source.A_2_B_raises.at(0).used = true;  
			trains.resize(1);
			trains.at(0).started_from = 'A';
			trains.at(0).station = 'B';
			trains.at(0).ready_time = source.A_2_B_raises.at(0).to + my_time(source.turnaround_time);
		}
		if (source.B_station_reises_count > 0)
		{
			count_b = 1;
			source.B_2_A_raises.at(0).used = true; 
			trains.resize(1);
			trains.at(0).started_from = 'B';
			trains.at(0).station = 'A';
			trains.at(0).ready_time = source.B_2_A_raises.at(0).to + my_time(source.turnaround_time);
		}
	}
}

void one_loop(source_structure& source, std::vector<train>& trains)
{
	for (int tr = 0; tr < trains.size(); tr++)
	{
		bool b = true;
		while (b) 
		{
			b = false;
			if (trains.at(tr).station == 'A')
			{
				for (int stA = 0; stA < source.A_2_B_raises.size(); stA++) 
					if (!source.A_2_B_raises.at(stA).used)
						if (source.A_2_B_raises.at(stA).from >= trains.at(tr).ready_time)
						{
							trains.at(tr).station = 'B';
							trains.at(tr).ready_time = source.A_2_B_raises.at(stA).to + my_time(source.turnaround_time);
							source.A_2_B_raises.at(stA).used = true;
							b = true;
							break;
						}
			}
			else
				for (int stB = 0; stB < source.B_2_A_raises.size(); stB++) 
					if (!source.B_2_A_raises.at(stB).used)
						if (source.B_2_A_raises.at(stB).from >= trains.at(tr).ready_time)
						{
							trains.at(tr).station = 'A';
							trains.at(tr).ready_time = source.B_2_A_raises.at(stB).to + my_time(source.turnaround_time);
							source.B_2_A_raises.at(stB).used = true;
							b = true;
							break;
						}				
		}
	}
}

bool train_creating(source_structure& source, std::vector<train>& trains, int& count_a, int& count_b)
{
	bool bbb = true;
	for (int stA = 0; stA < source.A_2_B_raises.size(); stA++)
		if (!source.A_2_B_raises.at(stA).used){	bbb = false; break;	}
	bool bbb1 = true;
	for (int stB = 0; stB < source.B_2_A_raises.size(); stB++)
		if (!source.B_2_A_raises.at(stB).used){ bbb1 = false; break; }
	if ((!bbb) && (bbb1)) 
	{
		trains.resize(trains.size()+1);
		trains.at(trains.size()-1).ready_time.set_HH(0);
		trains.at(trains.size()-1).ready_time.set_MM(0);
		trains.at(trains.size()-1).started_from = 'A';
		trains.at(trains.size()-1).station = 'A';		
		count_a++;
		return false;
	} else if ((!bbb1) && (bbb))
	{
		trains.resize(trains.size()+1);
		trains.at(trains.size()-1).ready_time.set_HH(0);
		trains.at(trains.size()-1).ready_time.set_MM(0);
		trains.at(trains.size()-1).started_from = 'B';
		trains.at(trains.size()-1).station = 'B';
		count_b++; 
		return false;				
	} else if ((!bbb)&&(!bbb1))
	{
		my_time minimum_timeA(24*60);
		for (int stA = 0; stA < source.A_2_B_raises.size(); stA++) if (!source.A_2_B_raises.at(stA).used)
			if (source.A_2_B_raises.at(stA).from < minimum_timeA) minimum_timeA = source.A_2_B_raises.at(stA).from;
		my_time minimum_timeB(24*60);
		for (int stB = 0; stB < source.B_2_A_raises.size(); stB++) if (!source.B_2_A_raises.at(stB).used)
			if (source.B_2_A_raises.at(stB).from < minimum_timeB) minimum_timeB = source.B_2_A_raises.at(stB).from;
		if (minimum_timeA < minimum_timeB)
		{
			trains.resize(trains.size()+1);
			trains.at(trains.size()-1).ready_time.set_HH(0);
			trains.at(trains.size()-1).ready_time.set_MM(0);
			trains.at(trains.size()-1).started_from = 'A';
			trains.at(trains.size()-1).station = 'A';		
			count_a++;
			return false;
		}
		else if (minimum_timeA > minimum_timeB)
		{
			trains.resize(trains.size()+1);
			trains.at(trains.size()-1).ready_time.set_HH(0);
			trains.at(trains.size()-1).ready_time.set_MM(0);
			trains.at(trains.size()-1).started_from = 'B';
			trains.at(trains.size()-1).station = 'B';
			count_b++;
			return false;
		} 
		else 
		{
			trains.resize(trains.size()+1);
			trains.at(trains.size()-1).ready_time.set_HH(0);
			trains.at(trains.size()-1).ready_time.set_MM(0);
			trains.at(trains.size()-1).started_from = 'A';
			trains.at(trains.size()-1).station = 'A';		
			count_a++;

			trains.resize(trains.size()+1);
			trains.at(trains.size()-1).ready_time.set_HH(0);
			trains.at(trains.size()-1).ready_time.set_MM(0);
			trains.at(trains.size()-1).started_from = 'B';
			trains.at(trains.size()-1).station = 'B';
			count_b++;
			return false;
		}
	}
	return true;
}

result_structure process(source_structure& source)
{
	sort_vectors(source);

	int count_a =0; int count_b=0;
	std::vector<train> trains;
 
	startup_train_filler(source, trains, count_a, count_b);

 	bool bb = true;
 	while (bb)
 	{
 		one_loop(source, trains);

 		bool bbb = train_creating(source, trains, count_a, count_b);

 		bb = !bbb;
 	}
	result_structure res; res.A_station_trains_count = count_a; res.B_station_trains_count = count_b;
	return res;
};
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
 	vector_source_structure data; 
 	int val, cases_count = 0;

 	std::ifstream input_file("in.txt");
	std::ofstream output_file("out.txt");
 	
	char buffer[100];	

 	if (input_file.is_open())
 	{
 		input_file.getline(buffer,100);
 		cases_count = atoi(buffer);
		data.resize(cases_count); 		

		for (vector_source_structure::iterator i = data.begin(); i != data.end(); i++)
		{
			input_file.getline(buffer,100);
			val = atoi(buffer);
			(*i).turnaround_time = val;

			input_file.getline(buffer,100);
			char* a = find(buffer, buffer+99,' ');
			*a = 0; a++;
			(*i).A_station_reises_count = atoi(buffer);
			(*i).B_station_reises_count = atoi(a);		
			(*i).A_2_B_raises.resize((*i).A_station_reises_count);
			(*i).B_2_A_raises.resize((*i).B_station_reises_count);
			
			for (raise_vector::iterator j = (*i).A_2_B_raises.begin(); j != (*i).A_2_B_raises.end(); j++)
			{
				input_file.getline(buffer,100);
				buffer[2] = 0;
				buffer[5] = 0;
				buffer[8] = 0;
				(*j).from.set_HH(atoi(buffer));
				(*j).from.set_MM(atoi(&(buffer[3])));
				(*j).to.set_HH(atoi(&(buffer[6])));
				(*j).to.set_MM(atoi(&(buffer[9])));
			}
			for (raise_vector::iterator j = (*i).B_2_A_raises.begin(); j != (*i).B_2_A_raises.end(); j++)
			{
				input_file.getline(buffer,100);
				buffer[2] = 0;
				buffer[5] = 0;
				buffer[8] = 0;
				(*j).from.set_HH(atoi(buffer));
				(*j).from.set_MM(atoi(&(buffer[3])));
				(*j).to.set_HH(atoi(&(buffer[6])));
				(*j).to.set_MM(atoi(&(buffer[9])));
			}			
 		}
 	}
	int counter = 1;
 	for (vector_source_structure::iterator i = data.begin(); i != data.end(); i++)
 	{
 		result_structure res = process(*i);
 		output_file << "Case #" << counter++ << ": " << res.A_station_trains_count << " " << res.B_station_trains_count << "\n";		
 	}

		

	input_file.close();
	output_file.close();


	return 0;
}

