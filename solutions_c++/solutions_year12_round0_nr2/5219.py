#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int S;
int maxx(int TT, int PP );
int abs(int A);
int main () {
	ifstream fileIn ("B-small-attempt19.in");
	ofstream fileOut ("B-small-attempt19.out");
	string line;
	int counter;
	getline (fileIn,line);
	int casel = 1;
	while(!fileIn.eof()){
	counter = 0;
	getline(fileIn,line);
	stringstream tmp(line);
	int N,P,T;
	tmp>>N>>S>>P;
	for(int i=0;i<N;i++){
	tmp>>T;
	if (((T/3) >= P ||((T+1)/3) >= P ||((T+2)/3) >= P) && T>P)
			counter++;
	else if((P+2*(P-2))<=T && S>0 && T>P)
	{counter++;S--;}
	}
	if (P==0)
		counter=N;
	if (!fileIn.eof()){
	fileOut<<"Case #"<<casel<<": "<<counter<<"\n";
	casel++;}
	}
	fileIn.close();
	fileOut.close();
  return 0;
}
