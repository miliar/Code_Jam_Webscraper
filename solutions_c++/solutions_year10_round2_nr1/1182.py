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
	int N, M;
	stream1 >> N >> M;
	//cout << "N: " << N << " M: " << M << endl;

	set<string> parents;
	for(int i = 0; i < N; ++i) {
	    getline(input, line);
//	    cout << "line: " << line << endl;
	    /*
	    for(int j = 0; j < line.length(); ++j) {
		if(line[j] == '/') line[j] = " ";
	    }*/
	    string delimit("/");
	    string::size_type pos = 0;
	    string::size_type pos1 = pos + 1;
//	    cout << "pose=" << line.find_first_of(delimit, 1) << endl;
	    for(; (pos = line.find_first_of(delimit, pos1)) != string::npos; ) {
		pos1 = pos + 1;
//		cout << "pos: " << pos << endl;
		string tmp(line, 0, pos);
//		cout << " tmp: " << tmp << endl;
		parents.insert(tmp);
	//	pair< set<string>::iterator, bool> ret = parents.insert(tmp);
	//	if(ret.second) counter++;
	    }
	    parents.insert(line);
	    /*
	    while(pos = (line.find_first_of(delimit, pos1)) != string::npos) {
	//	cout << " pos: " << pos << endl;
		pos1 = pos + 1;	
		string tmp(line, 0, pos);
	//	cout << tmp << endl;
		parents.insert(tmp);
	    }*/
	//    istringstream stream2(line);
	}
	//cout << "parents size: " << parents.size() << endl;
//	for(set<string>::iterator it = parents.begin(); it != parents.end(); ++it) {
	    //cout << *it << endl;
//	}

	int counter = 0;
//	cout << " M: " << M << endl;
	for(int i = 0; i < M; ++i) {
	    getline(input, line); 
	    //cout << "line: " << line << endl;
	    string delimit("/");
	    string::size_type pos = 0;
	    string::size_type pos1 = pos + 1;
//	    cout << "pose=" << line.find_first_of(delimit, pos1) << endl;

	    for(; (pos = line.find_first_of(delimit, pos1)) != string::npos; ) {
		pos1 = pos + 1;
		//cout << "pos: " << pos << endl;
		string tmp(line, 0, pos);
		//cout << " tmp: " << tmp << endl;
		pair< set<string>::iterator, bool> ret = parents.insert(tmp);
		if(ret.second) counter++;
	    }
	    pair< set<string>::iterator, bool> ret = parents.insert(line);
	    if(ret.second) counter++;
/*
	    while(pos = (line.find_first_of(delimit, pos1 )) != string::npos) {
		pos1 = pos + 1;	
//		cout << "pos: " << pos << endl;
		string tmp(line, 0, pos);
		pair< set<string>::iterator, bool> ret = parents.insert(tmp);
		if(ret.second) counter++;
	    }
	    */
	}
	cout << "Case #" << TestNo << ": " << counter << endl; 
    }


    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
