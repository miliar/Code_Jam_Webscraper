// Google Code Jam 2008,  Qualification Round, problem B: Train Timetable
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solve_timetable(ifstream& in_stream, unsigned int& trains_A, unsigned int& trains_B);
unsigned int time_to_minutes(const string& str_time);

struct timetable_entry
{
	unsigned int station;
	unsigned int demarture;
	unsigned int arrival;
};

int main(int argc, char* argv[])
{
	if (argc < 3)
	{
		cerr << "TrainTimetable <input_file> <output_file>" << endl;
		return -1;
	}

	ifstream input_file;
	try
	{
		input_file.open(argv[1]);
	}
	catch (exception& e)
	{
		cerr << "Unable to open input file" << endl << e.what() << endl;
		return -1;
	}
	ofstream output_file;
	try
	{
		output_file.open(argv[2]);
	}
	catch (exception& e)
	{
		cerr << "Unable to open output file" << endl << e.what() << endl;
		return -1;
	}

	unsigned int cases_count = 0;
	input_file >> cases_count;
	for (unsigned int case_number = 1; case_number <= cases_count; ++case_number)
	{
		unsigned int trains_A, trains_B;
		trains_A = trains_B = 0;
		solve_timetable(input_file, trains_A, trains_B);
		output_file << "Case #" << case_number << ": " << trains_A << " " << trains_B << endl;
	}

	return 0;
}

bool sort_by_departure_pred(const timetable_entry& x, const timetable_entry& y)
{
	return x.demarture < y.demarture;
}

void solve_timetable(ifstream& in_stream, unsigned int& trains_A, unsigned int& trains_B)
{
	static const unsigned int max_time = 24 * 60;
	unsigned int turnaround_time = 0;
	in_stream >> turnaround_time;

	unsigned int cases_A = 0, cases_B = 0;
	in_stream >> cases_A >> cases_B;

	string departure_str, arrival_str;
	timetable_entry new_entry;
	vector<timetable_entry> timetable;
	for (unsigned int i = 0; i < cases_A + cases_B; ++i)
	{
		in_stream >> departure_str >> arrival_str;
		new_entry.station = (i < cases_A) ? 0 : 1;
		new_entry.demarture = time_to_minutes(departure_str);
		new_entry.arrival = time_to_minutes(arrival_str);
		timetable.push_back(new_entry);
	}

	sort(timetable.begin(), timetable.end(), sort_by_departure_pred);
	trains_A = trains_B = 0;

	while (!timetable.empty())
	{
		unsigned int current_station = timetable[0].station;
		if (current_station == 0)
		{
			trains_A++;
		}
		else
		{
			trains_B++;
		}
		current_station = 1 - current_station;
		unsigned int current_time = timetable[0].arrival + turnaround_time;
		vector<unsigned int> records_to_remove;
		records_to_remove.push_back(0);

		for (size_t i = 1; i < timetable.size(); ++i)
		{
			if ((timetable[i].station == current_station) &&
				(timetable[i].demarture >= current_time))
			{
				records_to_remove.push_back(i);
				current_station = 1 - current_station;
				current_time = timetable[i].arrival + turnaround_time;
			}
		}
		
		for (size_t i = records_to_remove.size(); i > 0; --i)
		{
			timetable.erase(timetable.begin() + records_to_remove[i-1]);
		}
	}
}

// HH:MM -> minutes
unsigned int time_to_minutes(const string& str_time)
{
	return ((str_time[0] - '0') * 10 + str_time[1] - '0') * 60 +
		((str_time[3] - '0') * 10 + str_time[4] - '0');
}
