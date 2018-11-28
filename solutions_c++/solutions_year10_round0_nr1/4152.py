#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	ifstream input("A-large.in");
	ofstream output("output1.txt");
	int T;
	input>>T;
	int N;
	int K;
	for(int i=1;i<=T;i++)
	{
		input>>N;
		input>>K;
		if((K+1)%(1<<N)==0)
			output<<"Case #"<<i<<": ON";
		else
			output<<"Case #"<<i<<": OFF";
		if(i<T)
			output<<endl;
	}
    return 0;
}
