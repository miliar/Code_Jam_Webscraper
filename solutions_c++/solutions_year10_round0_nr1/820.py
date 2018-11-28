#include <iostream>
#include <fstream>
using namespace std;

string ifilename = "J:\\A-large.in";
string ofilename = "J:\\A-large.out.txt";

int main(){
	
	ifstream infile;
	ofstream outfile;
	outfile.open(ofilename.c_str());
	infile.open(ifilename.c_str());
	int ncases=0;
	infile >> ncases;
	for(int i=0;i<ncases;i++){
		long long N,K;
		infile >> N >> K;		
		long long l1 = 1;
		if(K%(l1<<N)==((l1<<N)-l1))
			outfile << "Case #" << i+1 << ": ON" << endl;
		else
			outfile << "Case #" << i+1 << ": OFF" << endl;		
	}	
	return 0;

}