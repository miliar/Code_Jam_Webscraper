#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <set> // Multiset required because there can be duplicate times.

using namespace std;


// Converts 24-hour time of the form HH:MM into the number of minutes since 00:00.
int convertTimeToMinutes(const string& time)
{
	int nMinutes = 0;
	istringstream iss(time);
	istringstream iss2;
	string temp;
	int tempNum = 0;
	getline(iss, temp, ':');
	iss2.str(temp);
	iss2 >> tempNum;
	nMinutes = 60*tempNum;
	getline(iss, temp, ':');
	iss2.clear();
	iss2.seekg(0,ios::beg);
	iss2.str(temp);
	iss2 >> tempNum;
	nMinutes += tempNum;
	return nMinutes;
}

int countUnsatisfiedTimes(const multiset<int>& schedule, const multiset<int>& available)
{
	int count = 0;
	multiset<int>::const_iterator it1 = schedule.begin();
	multiset<int>::const_iterator it2 = available.begin();
	for (; it1 != schedule.end(); it1++)
	{
		if (it2 != available.end() && *it2 <= *it1)
		{
			// Satisfied
			it2++;
		}
		else
		{
			// Unsatisfied
			count++;
		}
	}
	return count;
}

int main (int argc, char** argv)
{
	if (argc < 3)
	{
		cerr << "Usage: " << argv[0] << ": INPUT OUTPUT" << endl;
		return 1;
	}
	ifstream infile;
	ofstream outfile;
	infile.open(argv[1]);
	outfile.open(argv[2]);
	string line;
	getline(infile, line);
	istringstream iss;
	int nCases = 0;
	iss.str(line);
	iss >> nCases;
	for (int i = 0; i < nCases; i++)
	{
		getline(infile, line);
		iss.clear();
		iss.seekg(0,ios::beg);
		iss.str(line);
		int turnaroundTime = 0;
		iss >> turnaroundTime;
		getline(infile, line);
		iss.clear();
		iss.seekg(0,ios::beg);
		iss.str(line);
		istringstream iss2;
		getline(iss, line, ' ');
		iss2.str(line);
		int nA = 0;
		iss2 >> nA;
		getline(iss, line, ' ');
		iss2.clear();	
		iss2.seekg(0,ios::beg);
		iss2.str(line);
		int nB = 0;
		iss2 >> nB;

		multiset<int> departScheduleA;
		multiset<int> availableScheduleA;
		multiset<int> departScheduleB;
		multiset<int> availableScheduleB;		

		for (int j = 0; j < nA; j++)
		{
			string depart;
			string arrive;
			getline(infile, line);
			iss.clear();
			iss.seekg(0,ios::beg);
			iss.str(line);
			getline(iss, depart, ' ');
			getline(iss, arrive, ' ');
			departScheduleA.insert(convertTimeToMinutes(depart));
			availableScheduleB.insert(convertTimeToMinutes(arrive) + turnaroundTime);
		}
		for (int k = 0; k < nB; k++)
		{
			string depart;
			string arrive;
			getline(infile, line);
			iss.clear();
			iss.seekg(0,ios::beg);
			iss.str(line);
			getline(iss, depart, ' ');
			getline(iss, arrive, ' ');
			departScheduleB.insert(convertTimeToMinutes(depart));
			availableScheduleA.insert(convertTimeToMinutes(arrive) + turnaroundTime);
		}

		outfile << "Case #" << (i+1) << ": " 
			<< countUnsatisfiedTimes(departScheduleA, availableScheduleA) << " " 
			<< countUnsatisfiedTimes(departScheduleB, availableScheduleB) << endl;
	}
	infile.close();
	outfile.close();
}
