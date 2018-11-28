#include <vector>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <iostream>
#include <fstream>
#include <functional>
using namespace std;


template<typename T>
T MinThree(T a, T b, T c){
	return (a < b ? a : b) < c ? (a < b ? a : b) : c;
}

template<typename T>
string num2str(T num){
	ostringstream oss;
	oss << num;
	return oss.str();
}

template<typename T>
T str2num(const string& str){
	istringstream iss(str);
	T result;
	iss >> result;
	return result;
}
void ReadNANB(const string& line, int& NA, int& NB){
	istringstream iss(line);
	iss >> NA;
	iss >> NB;
}
void ReadTime(const string& line, int& departure, int& arrival){
	departure = 0;
	arrival = 0;

	string subline;
	size_t startPos, endPos;
	startPos = endPos = 0;
	endPos = line.find(':', startPos);
	subline = line.substr(startPos, endPos - startPos);
	departure += str2num<int>(subline) * 60;
	startPos = endPos + 1;
	endPos = startPos + 2;
	subline = line.substr(startPos, endPos - startPos);
	departure += str2num<int>(subline);
	startPos = endPos + 1;
	endPos = line.find(':', startPos);

	subline = line.substr(startPos, endPos - startPos);
	arrival += str2num<int>(subline) * 60;
	startPos = endPos + 1;
	endPos = startPos + 2;
	subline = line.substr(startPos, endPos - startPos);
	arrival += str2num<int>(subline);
}
int main(){
	ifstream ifs("input.in");
	ofstream ofs("output.out");

	string line;
	int numCase;
	getline(ifs, line, '\n');
	numCase = str2num<int>(line);
	int turnRoundTime;
	int NA, NB;

	int departure, arrival;
	for (int i = 0; i < numCase; ++i){
		getline(ifs, line, '\n');
		turnRoundTime = str2num<int>(line);
		getline(ifs, line, '\n');
		ReadNANB(line, NA, NB);

		//get from A to B
		multimap<int, int> ADepartureSorted, AArrivalSorted;
		for (int i = 0; i < NA; ++i){
			getline(ifs, line, '\n');
			ReadTime(line, departure, arrival);
			ADepartureSorted.insert(pair<int, int>(departure, arrival));
			AArrivalSorted.insert(pair<int, int>(arrival, departure));
		}
		//B to A
		multimap<int, int> BDepartureSorted, BArrivalSorted;
		for (int i = 0; i < NB; ++i){
			getline(ifs, line, '\n');
			ReadTime(line, departure, arrival);
			BDepartureSorted.insert(pair<int, int>(departure, arrival));
			BArrivalSorted.insert(pair<int, int>(arrival, departure));
		}
		int ATrainNeeded, BTrainNeeded;
		ATrainNeeded = BTrainNeeded = 0;

		//compute A train needed
		multimap<int, int>::iterator AIterDepart = ADepartureSorted.begin();
		multimap<int, int>::iterator BIterArrival = BArrivalSorted.begin();
		while (AIterDepart != ADepartureSorted.end() && BIterArrival != BArrivalSorted.end()){
			if (BIterArrival->first + turnRoundTime <= AIterDepart->first){
				++AIterDepart;
				++BIterArrival;
			}
			else {
				++ATrainNeeded;
				++AIterDepart;
			}
		}
		while (AIterDepart != ADepartureSorted.end()){
			++AIterDepart;
			++ATrainNeeded;
		}
		//compute B train needed
		multimap<int, int>::iterator BIterDepart = BDepartureSorted.begin();
		multimap<int, int>::iterator AIterArrival = AArrivalSorted.begin();
		while (BIterDepart != BDepartureSorted.end() && AIterArrival != AArrivalSorted.end()){
			if (AIterArrival->first + turnRoundTime <= BIterDepart->first){
				++BIterDepart;
				++AIterArrival;
			}
			else {
				++BTrainNeeded;
				++BIterDepart;
			}
		}
		while (BIterDepart != BDepartureSorted.end()){
			++BIterDepart;
			++BTrainNeeded;
		}
		ofs << "Case #" << (i + 1) << ": " << ATrainNeeded << " " << BTrainNeeded << endl;
	}

	return 0;
}