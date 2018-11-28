// Google CodeJam Round 1
// Name: GuitarCool 
// Email: itsmfe@gmail.com
// C++ under Ubuntu Linux, compiled by GNU g++
// Compile: run "g++ -o [target] [Source File]"

#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <bitset>
#include <cmath>
#include <vector>
#include <map>
#include <list>
#include <set>
using namespace std;

int main()
{
    string inputfile("A-large.in");
    ifstream input;
    input.open(inputfile.c_str());
    if(!input) throw runtime_error("Error in opening data file!");  

    string line;
    getline(input, line);
    istringstream stream(line);
    int T = 0;
    stream >> T;
    int TestNo = 0;

    while(getline(input, line)) {
	++TestNo;
	istringstream stream1(line);
	int N;
	stream1 >> N;
//	cout << "N: " << N << endl;

	map<int, int> map_lines;
	for(int i = 0; i < N; ++i) {
	    getline(input, line);
	    istringstream stream2(line);
	    int a, b;
	    stream2 >> a >> b;
	    map_lines.insert(make_pair(a,b));
	}
/*
	for(map<int, int>::iterator it = map_lines.begin(); it != map_lines.end(); ++it) {
	    cout << it-> first << "," << it->second << endl;
	}
	*/

	int counter = 0;
	for(map<int, int>::iterator it = map_lines.begin(); it != map_lines.end(); ++it) {
	    map<int, int>::iterator it1 = it;
	    ++it1; 
	    for(; it1 != map_lines.end(); ++it1) {
		if((it->first < it1->first && it->second > it1->second) || it->first > it1->first && it->second < it1->second ) ++counter;
	    }
	}
	cout << "Case #" << TestNo << ": " << counter << endl; 
    }


    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
