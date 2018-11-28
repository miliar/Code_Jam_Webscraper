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
#include "BigIntegerLibrary.hh"
using namespace std;

//const int MAX_T  = C;		    // Max. number of test cases
const int MAX_R  = 100000000;	    // Max. number of rounds
const int MAX_k	 = 1000000000;	    // Max. number of people that can hold
const int MAX_N	 = 1000;		    // Max. group number  
const int MAX_gi = 10000000;	    // Max. number of people in each group

BigInteger getMaxDivisor(BigInteger &a, BigInteger &b)   
{   
    BigInteger temp = -1;   
    if(a < b){
	swap(a, b);
    } 
		       
   while(b != 0) {
        a = a % b;   
        temp = a;   
        a = b;   
        b = temp;   
    }   
    return a;   
}   

int main()
{
    string inputfile("B-small-attempt0.in");
    ifstream input;
    input.open(inputfile.c_str());
    if(!input) throw runtime_error("Error in opening data file!");  

    string line;
    getline(input, line);
    istringstream stream(line);
    int C = 0;
    stream >> C;
    int TestNo = 0;

    while(getline(input, line)) {
	++TestNo;
	istringstream stream1(line);
	int N;
	stream1 >> N; 
	BigInteger bi[N];

	for(int i = 0; i < N; ++i) {
	    int tmp;
	    string s;
	    stream1 >> s;
	    bi[i] = stringToBigInteger(s);
	    //cout << bi[i] << endl;
	}
	
	sort(bi, bi + N);
	BigInteger max_divisor;
	if(N > 2) {
	    BigInteger b1 = bi[N - 1]- bi[N - 2];
	    BigInteger b2 = bi[N - 1] - bi[N - 3];
	    max_divisor = getMaxDivisor(b1, b2);
	    for(int i = N - 2; i >= 2; --i) {
		b1 = bi[i]- bi[i-1];
		b2 = bi[i] - bi[i - 2];
		BigInteger tmp = getMaxDivisor(b1, b2);
		if (tmp < max_divisor) max_divisor = tmp;
	    }
	}
	else if(N == 2) {
	    max_divisor = bi[N - 1] - bi[N - 2];
	}
	
	BigInteger result;
	if (bi[0] % max_divisor == 0) result = 0;
	else result =  max_divisor - (bi[0] % max_divisor);

	cout << "Case #" << TestNo << ": " << result << endl;	

    }

    if(TestNo != C) throw runtime_error("Error in reading test cases");

    input.close();
}
