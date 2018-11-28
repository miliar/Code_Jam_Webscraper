#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;
int main (int argc, char * const argv[]) {
	ofstream outFile;
	ifstream inFile;
	outFile.open("C-large.out");
	inFile.open("C-large.in.txt");
	string searchString="welcome to code jam";
	int numFound[19];
	string parsedString;
	int n;
	inFile>>n;
	getline(inFile,parsedString);
	for(int c=0; c<n; c++){
		getline(inFile,parsedString);
		for(int j=0; j<19;j++){
			numFound[j]=0;
		}
		for(int i=0; i<parsedString.size(); i++){
			for(int j=searchString.size()-1; j>=0; j--){
				if(parsedString[i]==searchString[j]){
						if(j==0)
							numFound[0]++;
						else{
							numFound[j]+=numFound[j-1];
						}
						while(numFound[j]>=10000)
							numFound[j]-=10000;
				}
			}
		}
		outFile<<"Case #"<<c+1<<": "<<setw(4)<<setfill('0')<<numFound[18]<<endl;
	}
	outFile.close();
	inFile.close();
    return 0;
}
