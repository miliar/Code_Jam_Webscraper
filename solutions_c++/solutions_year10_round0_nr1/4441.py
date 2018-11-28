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
using namespace std;

const int MAX_T = 10000;	    // Max. number of test cases
const int MAX_N = 30;		    // Max. number of Snappers
const int MAX_K = 100000000 + 1;    // Max. times of snapping fingers

void Flip(bitset<MAX_N> &bt, const int &N, const int &K)
{
    bitset<MAX_N> bt1, bt2;
    for(int j = 0; j < K; ++j) {
	bt2.flip(0);
	for(int i = 1; i < N; ++i) {
	    if(bt1.test(i - 1)) {
		bt2.flip(i);
	    }
	    else {
		break;
	    }
	}
	bt1 = bt2;
    }
    bt = bt1;
}

void Output(const bitset<MAX_N> &bt, const int &N, const int &TestNo)
{
    int i = 0;
    for(i = 0; i < N; ++i) {
	if(!bt.test(i)) break;
    }
    cout << "Case #" << TestNo << ": ";
    if(i == N) cout << "ON" << endl;
    else cout << "OFF" << endl;
}

int main()
{
    string inputfile;
    cin >> inputfile;
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
	Flip(bt, N, K);
	Output(bt, N, TestNo);
    }

    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
