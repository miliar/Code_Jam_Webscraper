#include<stdlib.h>
#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;
string sourceS= "abcdefghijklmnopqrstuvwxyz" ;
string mapping= "ynficwlbkuomxsevzpdrjgthaq" ;
map<char,char> translator;
void makeMap() {
for(int i =0 ; i<sourceS.length();i++)
{
	translator[mapping[i]] = sourceS[i];
}
translator[' '] = ' ' ;

}
int main ()
{
	makeMap();
	int numCases;
	ofstream result ("output.txt");
	ifstream myfile ("A-small-attempt0.in");
	if(myfile.is_open()) {
		while(myfile.good()) {
		string answer;
		string googlerese;
		getline(myfile,googlerese);
		int numCases = atoi(googlerese.c_str());
		
	for(int i =1;i<=numCases;i++) {
	answer="";
	getline(myfile, googlerese) ;
	for(int index =0;index < googlerese.length();index++) {
	answer+=translator[googlerese[index]];
	}
	result<<"Case #"<<i<<": "<<answer<<endl;
	}
	}
		myfile.close();
		result.close();
	}
	return 0;
}
