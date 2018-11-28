/*

CodeJam Round 1 Program A

*/

#include <iostream>
#include <fstream>
#include <ctype.h>
#include <string>
#include <math.h>

using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open ("input.in");
	outfile.open ("output.out");
	unsigned long long k;
	long n;
	unsigned long long cases;

	infile>>cases;

	for (int cnt2 = 0; cnt2 < cases; cnt2++){
		infile>>n>>k;

		if((k+1)%long long(pow(2.0,n)) == 0){
			outfile<<"Case #"<<cnt2+1<<": "<<"ON"<<endl;
		}
		else
			outfile<<"Case #"<<cnt2+1<<": "<<"OFF"<<endl;
	}

	return 0;
}