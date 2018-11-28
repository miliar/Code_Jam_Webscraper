#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;



int main(){

	ifstream	infile;
	ofstream	outfile;
	outfile.open("output");
	infile.open("A-large.in");

	string line;
	getline(infile,line);
 	long T = atoi(line.c_str());
	
	for (int i = 0 ; i < T ; i++)
	{
		getline(infile,line);
		int pos = line.find(" ");
		string sub;
		sub = line.substr(0,pos+1);
		int N = atoi(sub.c_str());
		sub = line.substr(pos+1,line.length() - pos);
		int K = atoi(sub.c_str());

		long H = 1<<N;

		if((K+1)%H == 0 && (K+1)/H > 0) outfile<<"Case #"<<i+1<<": ON"<<endl;
		else outfile<<"Case #"<<i+1<<": OFF"<<endl;
	}

	infile.close();
	outfile.close();
	return 0;
}
