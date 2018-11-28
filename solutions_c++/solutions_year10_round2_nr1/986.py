/*
 *  R1ProblemA.cpp
 *  CodeJam10
 *
 *  Created by Victor Ochikubo on 5/21/10.
 *  Copyright 2010 Stanford University. All rights reserved.
 *
 */

#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>
#include <numeric>
#include <set>

using namespace std;

typedef unsigned long long int ullint;

const string INPUT_FILE = "A-large.in";
const string OUTPUT_FILE = "A-large.out";

int GetNumCases(ifstream& infile) {
	stringstream sstream;
	string n_str;
	getline(infile, n_str);
	sstream.str(n_str);
	int retval;
	sstream >> retval;
	return retval;
}

// given set of directories already existing
// and set of new directories you want to create (tree?)
// how many mkdir commands do you need to use?
// you start off with just the root directory

// input: T M N
// T = num test cases
// N = path of one directory that already exists (not including root directory)- lowercase alphanumeric
// M = path of one directory

// a path may appear in both lists you have and lists to create
// if directory is listed as being on computer, parent directory will also be listed

// do with string set? string processing, look up until final /
// note that they could have the same name
// can you have string.find() start looking at 0? or just do a substring comparison


// if (dirs.find(key) != dirs.end()) , dirs.containsKey(key)

int CountNumNewDirs(ifstream& infile) {
	stringstream sstream;
	string n_str;
	getline(infile, n_str);
	sstream.str(n_str);
	int n_existing, n_toMake;
	sstream >> n_existing >> n_toMake;
	
	set<string> dirs;
	string haveDir, wantDir, possDir;
	dirs.insert("/");
	for (int i = 0; i < n_existing; ++i) {
		getline(infile, haveDir);
		dirs.insert(haveDir);
	}
	
	// for each string in n_toMake, keep searching forward and taking larger and larger substrings
	// of it, and see if the set contains that string, if not, add it
	ullint count = 0;
	for (int i = 0; i < n_toMake; ++i) {
		getline(infile, wantDir);
		
		if (dirs.find(wantDir) != dirs.end()) continue;
		
		int findPos, currSlash = 0; // take currSlash substring characters
		// look starting at position currSlash + 1
		// at the end, if there's no more currSlashes (never have just root)
		// go one more, add it to the set
		
		
		while(true) {
			findPos = wantDir.find('/', currSlash + 1);
			if (findPos == string::npos) {
				dirs.insert(wantDir);
				++count;
				break;
			} else {
				currSlash = findPos;
				possDir = wantDir.substr(0, currSlash);
				if(dirs.find(possDir) == dirs.end()) {
					dirs.insert(possDir);
					++count;
				}
			}
		}
	}
	
	return count;
}

int main(int argc, char *argv[]) {
	ifstream infile(INPUT_FILE.c_str());
	ofstream outfile(OUTPUT_FILE.c_str());
	if (infile.fail()) cout << "infile failed" << endl;
	int num_cases = GetNumCases(infile);
	
	for (int i = 0; i < num_cases; ++i) {
		int num_mkdir = CountNumNewDirs(infile);
		outfile << "Case #" << i + 1 << ": " << num_mkdir << endl;
	}
	
	infile.close();
	outfile.close();
	
}