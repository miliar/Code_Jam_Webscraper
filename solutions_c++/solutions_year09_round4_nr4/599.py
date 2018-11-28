#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <math.h>
using namespace std;
int main (int argc, char * const argv[]) {
	ofstream outFile;
	ifstream inFile;
	outFile.open("A-small.out");
	inFile.open("A-small.in.txt");
	int C,N;
	int x[3];
	int y[3];
	int r[3];
	inFile>>C;
	string instring;
	int count;
	for(int c=0; c<C; c++){
		count=0;
		inFile>>N;
		for(int i=0; i<N;i++){
			inFile>>x[i]>>y[i]>>r[i];
		}
		double smallest=-1;
		double amount;
		if(N==3){
		for(int i=0; i<3; i++){
			if(i==0)
				amount=(sqrt(pow(x[1]-x[2],2)+pow(y[1]-y[2],2))+r[1]+r[2])/2;
			else if(i==1)
				amount=(sqrt(pow(x[0]-x[2],2)+pow(y[0]-y[2],2))+r[0]+r[2])/2;
			else if(i==2)
				amount=(sqrt(pow(x[1]-x[0],2)+pow(y[1]-y[0],2))+r[1]+r[0])/2;
			amount=max(amount,(double)r[i]);
			if(smallest==-1 || smallest>amount){
				smallest=amount;
			}
		}
		}
		if(N==2){
			smallest=max(r[0],r[1]);
		}
		else if(N==1){
			smallest=r[0];
		}
			
		outFile.precision(20);
		outFile<<"Case #"<<c+1<<": "<<smallest<<endl;
	}
	outFile.close();
	inFile.close();
    return 0;
}
