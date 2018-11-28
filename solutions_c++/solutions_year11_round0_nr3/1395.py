#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <math.h>
#include <bitset>
#include <ctime>
#include <sys/time.h>

using namespace std;

int main (void) {
	fstream IN("C2.in", ios::in);
	fstream OUT("C2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
				
	for (int test=1; test<=NUM_TEST; test++) {
		int N;
		IN>>N;
		
		long long XOR=0;
		long long sum=0;
		long long min_=100000000;
		long long a;
		
		for (int i=0; i<N; i++) {
			IN>>a;
			XOR^=a;
			sum+=a;
			min_=min(min_,a);
			}

		OUT<<"Case #"<<test<<": ";
		if (XOR!=0) OUT<<"NO";
		else OUT<<(sum-min_);
		OUT<<"\n";
		}
	return 0;	
	}
