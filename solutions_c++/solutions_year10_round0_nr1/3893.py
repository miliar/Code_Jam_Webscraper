#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

typedef long long int64;
typedef long double ld;

int main (int argc, char * const argv[]) {
    
	fstream INP("A-large.in.txt", fstream::in);
	fstream OUT("output.txt",fstream::out);
	
	int T;
	
	INP>>T;
	
	for(int i=1;i<=T;i++)
	{
		int64 N, K;
		INP>>N>>K;
		
		bool res= ( (K+1)%(1<<N) ==0);
		if(res)
			OUT <<"Case #"<<i<<": ON"<<endl;
		else 
			OUT <<"Case #"<<i<<": OFF"<<endl;
		

		
		
	}
	
	
    return 0;
}
