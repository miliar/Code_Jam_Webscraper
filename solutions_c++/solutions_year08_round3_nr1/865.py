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

void ProcessLine(const string& line, vector<int>& freq){
	istringstream iss(line);
	freq.clear();
	copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(freq));
	sort(freq.begin(), freq.end());
}
void ReadPara(const string& line, int& maxPerKey, int& keys, int& letters){
	istringstream iss(line);
	iss >> maxPerKey >> keys >> letters;
}
int main(){
	ifstream ifs("input.in", ios::binary);
	ofstream ofs("output.out", ios::binary);
	
	int numCase;
	string line;
	getline(ifs, line, '\n');
	numCase = str2num<int>(line);
	int maxPerKey, keys, letters;
	vector<long> vecMinPress;
	vector<int> freq;
	int nLetterOfCommonKey;
	int nCommonKeys;
	for (int i = 0; i < numCase; ++i){
		int nTotalPress = 0;
		getline(ifs, line, '\n');
		ReadPara(line, maxPerKey, keys, letters);
		if (letters > maxPerKey * keys){
			vecMinPress.push_back(-1);
			getline(ifs, line, '\n');
			continue;
		}
		getline(ifs, line, '\n');
		ProcessLine(line, freq);
		if (freq.size() != letters)
		{
			cout << "error\n";
		}
		nLetterOfCommonKey = letters / keys;
		nCommonKeys = keys - (letters - nLetterOfCommonKey * keys);
		vector<int>::const_reverse_iterator riter = freq.rbegin();
		for (int i = 0; i < nLetterOfCommonKey; ++i){
			int temp = 0;
			for (int i = 0; i < keys; ++i){
				temp += *riter;
				++riter;
			}
			nTotalPress += temp * (i + 1);
		}
		for (int i = 0; i < keys - nCommonKeys; ++i){
			nTotalPress += (nLetterOfCommonKey + 1) * (*riter);
			++riter;
		}
		vecMinPress.push_back(nTotalPress);	
	}
	for (int i = 0; i < vecMinPress.size(); ++i){
		if (-1 != vecMinPress[i]){
			ofs << "Case #" << (i + 1) << ": " << vecMinPress[i] << endl;
		}
		else {
			ofs << "Case #" << (i + 1) << ": " << "impossible" << endl;
		}
	}
	return 0;
}