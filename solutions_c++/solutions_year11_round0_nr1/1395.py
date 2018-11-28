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

int ABS(int a) {
	if (a>=0) return a;
	return -a;
	}

int main (void) {
	fstream IN("A2.in", ios::in);
	fstream OUT("A2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;
		
	for (int test=1; test<=NUM_TEST; test++) {
		int N;
		IN>>N;
		
		vector <int> pos(2,1);
		vector <int> tim(2,0);
		int TIME=0;
		
		char b;
		int p,x;
		for (int i=0; i<N; i++) {
			IN>>b>>p;
			if (b=='O') x=0;
			else x=1;
			
			tim[x]=tim[x]+ABS(p-pos[x]);
			if (tim[x]<TIME) tim[x]=TIME;
			tim[x]++;
			pos[x]=p;
			
			TIME=tim[x];			
			}
		
		OUT<<"Case #"<<test<<": "<<TIME<<"\n";
		}
	return 0;	
	}

