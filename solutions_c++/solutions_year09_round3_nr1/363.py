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
	outFile.open("A-large.out");
	inFile.open("A-large.in.txt");
	int T;
	string theString;
	inFile>>T;
	int loc;
	int* valArray;
	int currentVal;
	long long int totalVal;
	for(int c=0; c<T; c++){
		
		currentVal=0;
		totalVal=0;
		inFile>>theString;
		valArray=new int[theString.length()];
		for(int i=0;i<theString.length();i++){
			loc=theString.find(theString[i]);
			if(loc<i){
				valArray[i]=valArray[loc];
			}
			else {
				if(currentVal<2)
					valArray[i]=1-currentVal;
				else
					valArray[i]=currentVal;
				currentVal++;
			}
		}
		if(currentVal<2)
			currentVal=2;
		for(int i=0; i<theString.length()-1;i++){
			totalVal+=valArray[i];
			totalVal*=currentVal;
		}
		totalVal+=valArray[theString.length()-1];
		
		outFile<<"Case #"<<c+1<<": "<<totalVal<<endl;
		delete[] valArray;
	}
	outFile.close();
	inFile.close();
    return 0;
}
