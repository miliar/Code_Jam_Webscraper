// googlecode.cpp : Train Timetable
// Author: Priyank Bolia <http://priyank.co.in>
// Date: 17th July, 2008

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <stdlib.h>

using namespace std;

typedef pair<int, int> TrainTime;
typedef vector<int> Time;
typedef vector<pair<int, int>> TimeTable;

std::vector<std::string> tokenize_str(const std::string & str,
									  const std::string & delims);
bool value_comparer(const std::pair<int, int>& lhs,
					const std::pair<int, int>& rhs);
TrainTime ConvertToTimeTableEntry(string &s, int turnAround);
size_t TrainsNeeded(TimeTable &a, TimeTable &b);

int main()
{
	ifstream inputFile ("B-large.in");
	ofstream outputFile ("output.in");
	if(!inputFile.is_open())
		return 0;
	if(!outputFile.is_open())
		return 0;
	int totalCases = 0;
	inputFile >> totalCases;
	for (int i=0; i < totalCases; ++i)  
	{
		int turnaroundTime = 0;
		int trainsFromA = 0;
		int trainsFromB = 0;
		TimeTable stationA;
		TimeTable stationB;
		string line;
		inputFile >> turnaroundTime;
		getline(inputFile, line);	//Get to next line
		inputFile >> trainsFromA;
		inputFile >> trainsFromB;
		getline(inputFile, line);	//Get to next line
		for (int j=0; j < trainsFromA; ++j)  
		{
			getline(inputFile, line);
			stationA.push_back(ConvertToTimeTableEntry(line, turnaroundTime));
		}
		for (int j=0; j < trainsFromB; ++j)  
		{
			getline(inputFile, line);
			stationB.push_back(ConvertToTimeTableEntry(line, turnaroundTime));
		}
		std::sort(stationA.begin(), stationA.end(), value_comparer);
		std::sort(stationB.begin(), stationB.end(), value_comparer);
		outputFile << "Case #" << (i+1) << ": " << TrainsNeeded(stationA, stationB) << " " << TrainsNeeded(stationB, stationA) << endl;
	}
	inputFile.close();
	outputFile.close();
	return 0;
}

size_t TrainsNeeded(TimeTable &a, TimeTable &b)
{
	size_t trainsNeeded = 0;
	Time trainsArrivingFromB;
	for(TimeTable::const_iterator iter = b.begin(); iter != b.end(); ++iter)
	{
		trainsArrivingFromB.push_back((*iter).second);
	}
	std::sort(trainsArrivingFromB.begin(), trainsArrivingFromB.end(), less<int>());
	size_t indexB = 0;
	if(trainsArrivingFromB.size() == 0)
	{
		trainsNeeded = (size_t)a.size();
	}
	else
	{
		for(TimeTable::const_iterator iter = a.begin(); iter != a.end(); ++iter)
		{
			if(indexB < trainsArrivingFromB.size() && (*iter).first < trainsArrivingFromB[indexB])
				++trainsNeeded;
			else if(indexB == trainsArrivingFromB.size())
				++trainsNeeded;
			else
				++indexB;
		}
	}
	return trainsNeeded;
}

bool value_comparer(const std::pair<int, int>& lhs,
					const std::pair<int, int>& rhs)
{
	return lhs.first < rhs.first;
}

TrainTime ConvertToTimeTableEntry(string &s, int turnAround)
{
	vector<string> timing(tokenize_str(s, " "));
	vector<string> startTime(tokenize_str(timing[0], ":"));
	vector<string> finishTime(tokenize_str(timing[1], ":"));
	int startAtMin = (atoi(startTime[0].c_str())*60) + atoi(startTime[1].c_str());
	int finishAtMin = (atoi(finishTime[0].c_str())*60) + atoi(finishTime[1].c_str());
	return make_pair<int, int>(startAtMin, finishAtMin+turnAround);
}

std::vector<std::string> tokenize_str(const std::string & str,
									  const std::string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<string> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}

	return tokens;
}
