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

void process(const int &N, int &K, const int &TestNo)
{
    int t = static_cast<int>(pow(2, N));
    while(K > t) {
	K = K - t;
    }    
    cout << "Case #" << TestNo << ": ";
    if(K == t - 1) {
	 cout << "ON" << endl;
    }   
    else  {
	cout << "OFF" << endl;
    }
}

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
	int N, K;
	stream1 >> N >> K;
	process(N, K, TestNo);
    }

    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
