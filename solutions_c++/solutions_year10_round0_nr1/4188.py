// Google CodeJam Qualification Round 2010 
// Name: Haiyan Luo
// Email: petrel.luo@gmail.com
// C++ under Ubuntu Linux, compiled by GNU g++
// Compile: run "g++ -o [target] probelm1.C"
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <bitset>
#include <cmath>
using namespace std;

const int MAX_T = 10000;	    // Max. number of test cases
const int MAX_N = 30;		    // Max. number of Snappers
const int MAX_K = 100000000 + 1;    // Max. times of snapping fingers

void Flip(bitset<MAX_N> &bt, const int &N, const int &K, const int &TestNo)
{
    // Preprocessing to speed up
    for(int i = 0; i < N; ++i) {
	if( (K / (int)pow((double)2, (double)i) % 2 != 1)) {
	    cout << "Case #" << TestNo << ": " << "OFF" << endl;
	    return;
	}
    }

    bitset<MAX_N> bt2;
    for(int j = 0; j < K; ++j) {
	bt2.flip(0);
	for(int i = 1; i < N; ++i) {
	    if(bt.test(i - 1)) {
		bt2.flip(i);
	    }
	    else {
		break;
	    }
	}
	bt = bt2;
    }

    cout << "Case #" << TestNo << ": ";
    if(bt.count() == N) cout << "ON" << endl;
    else cout << "OFF" << endl;
}

int main()
{
    string inputfile("A-small-attempt0.in");
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
	int N, K;
	stream1 >> N >> K;
	bitset<MAX_N> bt;
	Flip(bt, N, K, TestNo);
    }

    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
