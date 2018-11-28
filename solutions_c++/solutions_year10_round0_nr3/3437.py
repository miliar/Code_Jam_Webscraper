// Google CodeJam Qualification Round 2010 
// Name: Haiyan Luo
// Email: petrel.luo@gmail.com
// C++ under Ubuntu Linux, compiled by GNU g++
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <queue>
using namespace std;

const int MAX_T  = 50;		    // Max. number of test cases
const int MAX_R  = 100000000;	    // Max. number of rounds
const int MAX_k	 = 1000000000;	    // Max. number of people that can hold
const int MAX_N	 = 1000;		    // Max. group number  
const int MAX_gi = 10000000;	    // Max. number of people in each group

int main()
{
    string inputfile("C-small-attempt1.in");
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
	int R, k, N;
	stream1 >> R >> k >> N;
	getline(input, line);
	istringstream stream2(line);
	queue<int> q;
	for(int i = 0; i < N; ++i) {
	    int tmp;
	    stream2 >> tmp ;
	    q.push(tmp);
	}
//	cout << "R: " << R << " k: " << k << " N: " << N << endl;
	int sum = 0;
	for(int round = 0; round < R; ) {
	    int round_sum = 0;
	    queue<int> tmp_q;
	    while(1) {
		if(!q.empty() && (round_sum + q.front()) <= k) {
		    round_sum += q.front();
		    tmp_q.push(q.front());
		    q.pop();
		}
		else {
		   ++round;
		   while(!tmp_q.empty()) {
			q.push(tmp_q.front());
			tmp_q.pop();
		   }
		   break;
		}
	    }
	    sum += round_sum;
	}

	cout << "Case #" << TestNo << ": " << sum << endl;	

    }

    if(TestNo != T) throw runtime_error("Error in reading test cases");

    input.close();
}
