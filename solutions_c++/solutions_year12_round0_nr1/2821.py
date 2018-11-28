#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <map>
using namespace std;


void main(int argc, char* argv[]){
	char testString[110];
	int numtest;
	
	ifstream fin;
	//fin.open(argv[1]);
	fin.open("A-small-attempt2.in");
	ofstream fout;	
	fout.open("Output.txt");
	char charMap[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	

	if(fin.good() == true) {
		fin >> numtest; cout<<"Number of test case is "<<numtest<<endl;
		fin.ignore();
		for(int i=0; i<numtest; i++){
			fin.getline(testString,110);
			//fin.ignore();
			cout<<"Line "<<i+1<<" is "<< testString<<endl;
		//Do the conversion and write into the output file
			char *str=testString;
			while((*str)!='\0'){
				int index = (*str) -'a';
				if((*str)!=' '){
					(*str)=charMap[index];
				}
				str++;
			}
			fout <<"Case #"<<i+1<<": "<<testString<<"\n";
		}
		

	}
	fout.close();
}