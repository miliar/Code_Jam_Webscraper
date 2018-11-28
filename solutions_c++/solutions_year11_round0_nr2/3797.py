/*
 *  qualB.cpp
 *  codejam11
 *
 *  Created by Victor Ochikubo on 5/7/11.
 *  Copyright 2011 Stanford University. All rights reserved.
 *
 */


#include <iostream>
#include <sstream>
#include <fstream>

#include <stack>
#include <set>
#include <map>
#include <vector>


// store the letters in a stack as you go
// pop off the last one each time you get a new element
// if combines, combine
// if opposed to this new one, clear the list
// or, if opposed to any base in the list before, clear the list
// otherwise, add the one you just popped back, (ADD IT TO THE SET OF UNUSED BASE), add the new one in
// then build the string

// to determine combines: map of letter pairs, in both directions, to the one it combines to
// to determine opposed: map of base elements to vector of letters it is opposed to

using namespace std;

const string INFILE = "B-large.in";
const string OUTFILE = "B-large.out";


void OpenFile(ifstream& input) {
	input.open(INFILE.c_str());
	if (input.fail()) {
		cout << "Error: Couldn't open file." << endl;
	}
}

void OpenOutputFile(ofstream& output) {
	output.open(OUTFILE.c_str());
	if (output.fail()) {
		cout << "Error: Couldn't open output file." << endl;
	}
}

size_t GetNumCases(ifstream& input) {
	stringstream s;
	string str;
	getline(input, str);
	// cout << str << endl; // for testing only, should be a single number
	s << str;
	size_t numCases = 0;
	s >> numCases;
	return numCases;
}

void ProcessCase(ifstream& input, map<string, char>& combinesMap, map<char, vector<char> >& opposedMap, string& invokeList) {
	string str;
	getline(input, str);
	stringstream s;
	s << str;
	
	size_t numConstraints = 0;
	
	s >> numConstraints;
	for (size_t i = 0; i < numConstraints; ++i) {
		s >> str;
		// read into the combinesmap

		char firstElem = str[0];
		char secondElem = str[1];
		char makes = str[2];
		
		combinesMap.insert(make_pair(string("") + firstElem + secondElem, makes));
		combinesMap.insert(make_pair(string("") + secondElem + firstElem, makes));
		
		// for testing
		/*
		map<string, char>::iterator it;
		it = combinesMap.find(string("QF"));
		if (it != combinesMap.end())
			cout << it->second << endl;
		it = combinesMap.find(string("FQ"));
		if (it != combinesMap.end())
			cout << it->second << endl;
		 */
	}
	
	s >> numConstraints;
	for (size_t i = 0; i < numConstraints; ++i) {
		s >> str;
		// read into the opposedmap
		
		char first = str[0];
		char second = str[1];
		
		map<char, vector<char> >::iterator it;
		if ((it = opposedMap.find(first)) != opposedMap.end()) {
			it->second.push_back(second);
		} else { // make the vector
			vector<char> temp;
			temp.push_back(second);
			opposedMap.insert(make_pair(first, temp));
		}
		
		if ((it = opposedMap.find(second)) != opposedMap.end()) {
			it->second.push_back(first);
		} else {
			vector<char> temp;
			temp.push_back(first);
			opposedMap.insert(make_pair(second, temp));
		}
		
	}
	
	s >> numConstraints;
	s >> invokeList;

}


// pop off the last one each time you get a new element
// if combines, combine
// if opposed to this new one, clear the list
// or, if opposed to any base in the list before, clear the list, clear the USED
// otherwise, add the one you just popped back, (ADD IT TO THE SET OF USED BASE), add the new one in
// then build the string

// stack.push(elem), elem = stack.top(), stack.pop()

void RunCase(stack<char>& currentRun, map<string,char>& combinesMap, map<char,vector<char> >& opposedMap, string& invokeList) {
	set<char> currentBase; // all the base elements that are hidden somewhere further down in your current run
	for (size_t i = 0; i < invokeList.size(); ++i) {
		char currInv = invokeList[i];
		
		if (currentRun.empty()) {
			currentRun.push(currInv);
			continue;
		}
		
		char last = currentRun.top();
		currentRun.pop();
		
		map<string,char>::iterator cit;
		map<char,vector<char> >::iterator oit;
		if ((cit = combinesMap.find(string("") + last + currInv)) != combinesMap.end()) {
			currentRun.push(cit->second);
		} else {
			// check for opposed
			if ((oit = opposedMap.find(currInv)) != opposedMap.end()) {
				// there is some opposed, 
				// now check and see if it's anything in currentBase, or last
				
				bool cleared = false;
				
				for (size_t j = 0; j < oit->second.size(); ++j) {
					if (oit->second[j] == last ||
						currentBase.find(oit->second[j]) != currentBase.end()) {
						// clear the sets and the stack
						stack<char> empty;
						currentRun = empty;
						currentBase.clear();
						cleared = true;
					}
				}
				
				if (!cleared) {
					currentRun.push(last);
					currentBase.insert(last);
					currentRun.push(currInv);
				}
			
			} else { // nothing opposed
				currentRun.push(last);
				currentBase.insert(last);
				
				currentRun.push(currInv);
			}
		}
		
	}
}

string SizeToString(size_t num) {
	stringstream s;
	s << num;
	return s.str();
}

void DoOutput(ofstream& output, stack<char>& currentRun, size_t caseNum) {
	string builder = "]";
	
	while (!currentRun.empty()) {
		builder = currentRun.top() + builder;
		currentRun.pop();
		
		if (!currentRun.empty()) {
			builder = ", " + builder;
		}
	}
	
	string outStr = string("Case #");
	outStr += SizeToString(caseNum);
	outStr += string(": [") + builder;
	//builder = string("Case #") + caseNum + string(": ") + string("[") + builder;
	
	cout << outStr << endl;
	
	output << outStr << endl;
}

void DoCase(ifstream& input, ofstream& output, size_t caseNum) {
	map<string, char> combinesMap;
	map<char, vector<char> > opposedMap;
	string invokeList;
	
	
	// cout << "case # " << caseNum << endl;
	
	ProcessCase(input, combinesMap, opposedMap, invokeList);
		
	stack<char> currentRun;
	
	RunCase(currentRun, combinesMap, opposedMap, invokeList);
	
	DoOutput(output, currentRun, caseNum);
}


int main() {
	
	ifstream input;
	OpenFile(input);
	ofstream output;
	OpenOutputFile(output);
	
	size_t numCases = GetNumCases(input);
	
	cout << "numCases = " << numCases << endl;
	
	for (size_t i = 0; i < numCases; ++i) {
		DoCase(input, output, i + 1);
	}
	
	
	return 0;
}

