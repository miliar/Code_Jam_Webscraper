#include <iostream>
#include <fstream>
#include <sstream>
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
//	fstream IN("A0.in", ios::in);	fstream OUT("A0.out", ios::out);
//	fstream IN("A1bis.in", ios::in);	fstream OUT("A1bis.out", ios::out);
	fstream IN("A2.in", ios::in);	fstream OUT("A2.out", ios::out);
	
	int NUM_TEST;
	IN>>NUM_TEST;

	for (int test=1; test<=NUM_TEST; test++) {
		long long N;
		int Pg,Pd;
		IN>>N>>Pd>>Pg;
		
		bool F=true;
		
		if ((Pg==100) && (Pd!=100)) F=false;
		if ((Pg==0) && (Pd!=0)) F=false;
		
		int a=100;
		if (Pd%2==0) a/=2;
		if (Pd%4==0) a/=2;
		if (Pd%5==0) a/=5;
		if (Pd%25==0) a/=5;
		
		if (N<a) F=false;
		
		OUT<<"Case #"<<test<<": ";
		if (F==true) OUT<<"Possible";
		if (F==false) OUT<<"Broken";
		OUT<<"\n";
		}
	return 0;	
	}

