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
//	fstream IN("D0.in", ios::in);	fstream OUT("D0.out", ios::out);
//	fstream IN("D1.in", ios::in);	fstream OUT("D1.out", ios::out);
	fstream IN("D2.in", ios::in);	fstream OUT("D2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		int N,a,sum=0;
		IN>>N;
		
		for (int i=1; i<=N; i++) {
			IN>>a;
			if (a!=i) sum++;
			}
		
		OUT<<"Case #"<<test<<": "<<sum<<".000000\n";
		}
	return 0;	
	}

