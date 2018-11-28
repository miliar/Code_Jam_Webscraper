#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iostream>
#include <utility>

using namespace std;

#define FOR(i, a, b) for (int i(a); i <= b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0); i < n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef _int64 i64;
typedef unsigned _int64 ui64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

int main()
{
	ifstream infile("p1L.in");
	if(! infile){
		cerr << "error: unable to open input file: "
			<< infile <<endl;
		return -1;
	}
	ofstream outfile("p1L.out");
	if(! outfile){
		cerr << "error: unable to open output file: "
			<< outfile <<endl;
		return -2;
	}
	int testCase;
	infile >> testCase;
	int N,K; 
	REP(a, testCase){
		outfile<<"Case #"<<a+1<<": ";
		infile >> N;
		infile >> K;
		i64 res=1,k=K;
		REP(b, N){
			res*=2;
		}
		if((k%res)==(res-1)){
			outfile<<"ON"<<endl;
		}
		else{
			outfile<<"OFF"<<endl;
		}
	}
	return 0;
}