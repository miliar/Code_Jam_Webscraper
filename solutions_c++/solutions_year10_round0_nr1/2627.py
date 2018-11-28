/*
ID: zinking1
PROG: Snapper chain
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
using namespace std;

typedef  long long int64;
ifstream ifile("A-large.in");
ofstream ofile("A-large.out");

string getResult( int64 N, int64 K ){
	int64 m = 1 << N;
	int64 s = m-1;
	int64 kk = K % m;
	if( kk == s ) return "ON";
	else return "OFF";
}

int main(){

	int T=0;
	ifile >> T;
	int i = 0;
	while( i < T ){
		int64 N,K;
		ifile >> N >> K;
		ofile <<"Case #" << i+1 << ": "<< getResult(N,K) << endl;
		i++; 
	}
}
