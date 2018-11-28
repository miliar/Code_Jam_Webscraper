#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <iostream>
#include <fstream>
#include <functional>
#include <cmath>
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
void ProcessLine(const string& line, const int count, vector<int>& vec){
	vec.clear();
	istringstream iss(line);
	//int value;
	//for (int i = 0; i < count; ++i){
	//	iss >> value;
	//	vec.push_back(value);
	//}
	copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(vec));
}
//string ProcessDouble(const double input){
//	double temp(input);
//	while (temp >= 1000){
//		temp /= 1000;
//	}
//	int num = int(temp) % 1000;
//	int nZeroPad;
//	if (num >= 100){
//		nZeroPad = 0;
//	}
//	else if (num >= 10)
//	{
//		nZeroPad = 1;
//	}
//	else if (num >= 1){
//		nZeroPad = 2;
//	}
//	else {
//		nZeroPad = 3;
//	}
//	string result = num2str(num);
//	result.insert(0, nZeroPad, '0');
//
//	return result;
//}
int main(){
	ifstream ifs("input.in");
	ofstream ofs("output.out");

	string line;
	int numCase;
	getline(ifs, line, '\n');
	numCase = str2num<int>(line);
	int count;
	vector<int> first, second;
	for (int i = 0; i < numCase; ++i){
		long result = 0;
		getline(ifs, line, '\n');
		//count = str2num<int>(line);
		getline(ifs, line, '\n');
		ProcessLine(line, count, first);
		getline(ifs, line, '\n');
		ProcessLine(line, count, second);
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		//for (int i = 0; i < first.size(); ++i){
		//	result += first[i] * second[first.size() - 1 - i];
		//}
		ofs << "Case #" << (i + 1) << ": " << /*result*/inner_product(first.begin(), first.end(), second.rbegin(), 0) << endl;
	}
	return 0;
}