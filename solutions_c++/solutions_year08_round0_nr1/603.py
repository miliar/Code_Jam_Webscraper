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

int SearchSwitchDistance(const string queries[], const int numQueries, const string& engine){
	int distance(0);
	for (int i = 0; i < numQueries; ++i){
		if (0 == engine.compare(queries[i])){
			break;
		}
		++distance;
	}
	return distance;
}

int main(){
	ifstream ifs("input.in");
	string line;
	int numCase;
	getline(ifs, line, '\n');
	numCase = str2num<int>(line);
	ofstream ofs("output.out");
	int numEngines;
	int numQueries;
	vector<string> engines;
	vector<string> queries;
	vector<int> distance;

	for (int i = 0; i < numCase; ++i){
		engines.clear();
		queries.clear();
		getline(ifs, line, '\n');
		numEngines = str2num<int>(line);
		
		for (int i = 0; i < numEngines; ++i){
			getline(ifs, line, '\n');
			engines.push_back(line);
		}
		getline(ifs, line, '\n');
		numQueries = str2num<int>(line);
		for (int i = 0; i < numQueries; ++i){
			getline(ifs, line, '\n');
			queries.push_back(line);
		}
		int startPos = 0;
		int switchTimes = 0;
		while (startPos != queries.size()){
			distance.clear();
			for (int i = 0; i < numEngines; ++i){
				distance.push_back(SearchSwitchDistance(&queries[startPos], queries.size() - startPos, engines[i]));
			}
			startPos += *max_element(distance.begin(), distance.end());
			++switchTimes;
		}
		--switchTimes;
		if (switchTimes < 0)
			switchTimes = 0;
		ofs << "Case #" << (i + 1) <<": " << switchTimes <<endl;
	}
	return 0;
}