#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

// Problem A
// any S receiving power from its input gives power to output if it is ON
// toggle first, and then lose/gain power
// if N = 1, light is ON if we have an odd number of snaps
// all S start OFF, first one receiving power OFFP OFF OFF OFF ...
// 1 snap: ONP OFFP OFF OFF ...
// 2 snap: OFFP ON OFF OFF ...
// 3 snap: ONP ONP OFFP OFF ... example given ends here. light at 2 is on
// 4 snap: OFFP OFF ON OFF OFF ...
// 5 snap: ONP OFFP ON OFF OFF ...
// 6 snap: OFFP ON ON OFF OFF ...
// 7 snap: ONP ONP ONP OFFP OFF ... light at 2 and 3 is on (light is plugged into last snapper)
// 8 snap: OFFP OFF OFF ON OFF ...
// 9 snap: ONP OFFP OFF ON OFF ...
// 10    : OFFP ON OFF ON OFF ...
// 11    : ONP ONP OFFP ON OFF ... light at 2 is on
// 12    : OFFP OFF ON ON OFF ...
// 13    : ONP OFFP ON ON OFF ...
// 14    : OFFP ON ON ON OFF ...
// 15    : ONP ONP ONP ONP OFFP ... light at 2, 3, 4 is on

// N = 1, start with NUM = 1
// N = 2, 2*1 + 1 = 3
// N = 3, 2*3 + 1 = 7 (after NUM snaps it is on, or NUM + a*(NUM + 1)

// from left, propagate the ONs, repeat predictably
// difference equation for closed-form solution? then memoize the powers of whatever we need - 1 to 100 for K? 
// for K? probably won't work with large dataset though

const string INPUT_FILE = "A-large.in";
const string OUTPUT_FILE = "A-large.out";
const int MAX_N = 30;

void MakeSpecialNums(vector<int>& special_nums) {
	special_nums.push_back(0);
	/*
	for (int i = 1; i <= MAX_N; ++i) {
		int last_num = special_nums[i - 1];
		special_nums.push_back(last_num * 2 + 1);
	}
	 */
	for (int i = 1; i <= MAX_N; ++i) {
		int last_num = (1 << i) - 1;
		special_nums.push_back(last_num);
	}
}

template <typename T>
void PrintVector(vector<T>& vec) {
	for (int i = 0; i < vec.size(); ++i) {
		cout << vec[i] << endl;
	}
}

struct IntPair {
	int first;
	int second;
};

IntPair GetNextNumbers(ifstream& infile) {
	stringstream sstream;
	string str;
	getline(infile, str);
	sstream.str(str);
	IntPair pair;
	sstream >> pair.first >> pair.second;
	return pair;
}

// pair.first = N
// pair.second = K
bool SnapperOn(vector<int>& special_nums, IntPair& pair) {
	int thisNum = special_nums[pair.first];
	if (pair.second >= thisNum) {
		pair.second -= thisNum;
		return (pair.second % (thisNum + 1) == 0);
		// subtract num, mod with num + 1 should be 0
	} else return false;
}

int main (int argc, char * const argv[]) {
	vector<int> special_nums;
	MakeSpecialNums(special_nums);
	//PrintVector(special_nums);
	
	ifstream infile(INPUT_FILE.c_str());
	ofstream outfile(OUTPUT_FILE.c_str());
	if (infile.fail()) cout << "infile failed" << endl;
	stringstream sstream;
	string n_str; // get # of test cases
	getline(infile, n_str); 
	sstream.str(n_str);
	int num_cases;
	sstream >> num_cases;
	string offOn;

	for (int i = 0; i < num_cases; ++i) {
		IntPair pair = GetNextNumbers(infile);
		//cout << "pair = " << pair.first << " " << pair.second << endl;
		bool isOn = SnapperOn(special_nums, pair);
		offOn = isOn ? "ON" : "OFF";
		outfile << "Case #" << i+1 << ": " << offOn << endl;
	}
	
	infile.close();
	outfile.close();
	
    return 0;
}

// Problem B
// optimum anniversary is, given smallest y that gives largest possible T
// that is the largest multiple of all of them at that later time

// given a vector of integers, without using any extra space, O(1) space, go through and make it 
// so that any integer in there that there's at least 2 copies of, make 1
// or, alternately, any integer that's unique, make 1