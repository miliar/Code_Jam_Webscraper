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
	fstream IN("A2.in", ios::in);
	fstream OUT("A2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		long long N,K;
		IN>>N>>K;
		bool res=((K+1)%((long long)1<<N)!=0);

		OUT<<"Case #"<<test<<": ";
		if (res) OUT<<"OFF";
		else OUT<<"ON";
		OUT<<"\n";
		}
	return 0;	
	}

