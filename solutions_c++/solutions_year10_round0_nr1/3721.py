#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

int main(){
	ifstream dataInput("A-large.in");		//input the file stream

	int T = 0;							//the number of test cases
	dataInput>>T;			//get the number of cases

	ofstream dataOutput("out");	//
	for(int i=1;i<=T;i++){	//manage every case
		long N = 0,	//there are N Snappers
			K = 0;	//you make K snaps
		dataInput>>N>>K;	//get N and K
		dataOutput<<"Case #"<<i<<": ";
		if((K+1)%(int)pow(2,N) == 0)	//ON
			dataOutput<<"ON"<<endl;
		else							//OFF
			dataOutput<<"OFF"<<endl;
	}
}
		
