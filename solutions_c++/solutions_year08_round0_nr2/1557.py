// Train Timetable.cpp : Defines the entry point for the console application.
//

#include <string>
#include <vector>

#include <iostream>
#include <sstream>

#include <algorithm>


struct train_time
{
	train_time(const std::string& str_departure,const std::string& str_arrive)
	{
		short minutes;
		short hours;
		std::istringstream (str_departure.substr(0,2)) >> hours;
		std::istringstream (str_departure.substr(3,2)) >> minutes;

		departure = hours*60 + minutes;

		std::istringstream (str_arrive.substr(0,2)) >> hours;
		std::istringstream (str_arrive.substr(3,2)) >> minutes;

		arrive = hours*60 + minutes;
	}
	short departure; // Departure time (in minutes ex. "21:20" = 21*60 + 20 = 1280
	short arrive;    // arrive time (in minutes ex. "21:20" = 21*60 + 20 = 1280
};

typedef std::vector<train_time> array_train_time;

using std::string;

using std::cin;
using std::cout;

long count_minimum_trains(const array_train_time& a_to_b, const array_train_time& b_to_a,long tta);

class compare_by_arrive
{
public:
	bool operator ()(const train_time& a, const train_time& b)
	{
		return a.arrive < b.arrive;
	}
};

class compare_by_departure
{
public:
	bool operator ()(const train_time& a, const train_time& b)
	{
		return a.departure < b.departure;
	}
};


int main(int argc, char* argv[])
{
	unsigned long total_cases;       // Total of cases to be tested

	unsigned long tournarround_time;// Tourn arround time 

	unsigned long total_ab;         // Total of trip from A to B
	unsigned long total_ba;         // Total of trip from A to B

	string departure;         
	string arrive;			 
	string str_total_a;       
	string str_total_b;				  // The query to search engine

	array_train_time a_train_times;       // Array of search engines names
	array_train_time b_train_times;              // Array of queries strings

	cin >> total_cases;

	cin.ignore();
	cin.clear();

	for(unsigned long i = 1; i <= total_cases; i++)
	{
		cin >> tournarround_time;
		cin.ignore();
		cin.clear();

		a_train_times.clear();
		b_train_times.clear();

		std::getline(cin,str_total_a,' ');
		std::getline(cin,str_total_b);

		std::istringstream(str_total_a) >> total_ab;
		std::istringstream(str_total_b) >> total_ba;

		for(unsigned long j = 0; j < total_ab; j++)
		{
			std::getline(cin,departure,' ');
			std::getline(cin,arrive);
			a_train_times.push_back(train_time(departure,arrive));
		}

		for(unsigned long k = 0; k < total_ba; k++)
		{
			std::getline(cin,departure,' ');
			std::getline(cin,arrive);
			b_train_times.push_back(train_time(departure,arrive));
		}

		std::sort(a_train_times.begin(), a_train_times.end(), compare_by_departure());
		std::sort(b_train_times.begin(), b_train_times.end(), compare_by_arrive());
		
		long min_a = count_minimum_trains(a_train_times, b_train_times,tournarround_time);

		std::sort(b_train_times.begin(), b_train_times.end(), compare_by_departure());
		std::sort(a_train_times.begin(), a_train_times.end(), compare_by_arrive());

		long min_b = count_minimum_trains(b_train_times,a_train_times,tournarround_time);

		cout << "Case #" << i <<": " << min_a << " " << min_b << std::endl;
	}
	return 0;
}

long count_minimum_trains(const array_train_time& a_to_b, const array_train_time& b_to_a,long tta)
{
	long total_trains =  0;
	array_train_time::const_iterator it_a;
	array_train_time::const_iterator it_b;
	array_train_time::const_iterator it_avaiable_b;

	it_avaiable_b = b_to_a.begin();


	for(it_a = a_to_b.begin(); it_a != a_to_b.end(); it_a++)
	{
		const train_time & time_a = *it_a;

		for(it_b = it_avaiable_b; it_b != b_to_a.end(); )
		{
			const train_time & time_b = *it_b;

			if(time_a.departure >= time_b.arrive + tta)
			{
				it_avaiable_b = it_b + 1;
				break;
			}
			it_b++;			
		}
		if(it_b == b_to_a.end())
			total_trains++;		
	}
	
	return total_trains;
}


