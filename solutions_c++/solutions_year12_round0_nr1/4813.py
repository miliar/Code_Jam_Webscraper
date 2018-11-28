#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;

int main(){
	ifstream ifile;
	ofstream ofile;
	char trans[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	string templine;
	string templine2="";
	ifile.open("input");
	ofile.open("output");
	getline(ifile,templine);
	int t = atoi(templine.c_str());
	for(int i=0;i<t;++i){
		getline(ifile,templine);
		templine2="";
		for(int j=0;j<templine.length();++j){
			if (templine[j]!=' ')
				templine2 += trans[templine[j]-97];
			else
				templine2 += ' ';
		}
		ofile << "Case #" << i+1 << ": " << templine2 << endl;
	}
	return 0;
}

