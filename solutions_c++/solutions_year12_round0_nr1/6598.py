#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
	char lang[26];
	string s;
	
	lang[0]='y';
	lang[1]='h';
	lang[2]='e';
	lang[3]='s';
	lang[4]='o';
	lang[5]='c';
	lang[6]='v';
	lang[7]='x';
	lang[8]='d';
	lang[9]='u';
	lang[10]='i';
	lang[11]='g';
	lang[12]='l';
	lang[13]='b';
	lang[14]='k';
	lang[15]='r';
	lang[16]='z';
	lang[17]='t';
	lang[18]='n';
	lang[19]='w';
	lang[20]='j';
	lang[21]='p';
	lang[22]='f';
	lang[23]='m';
	lang[24]='a';
	lang[25]='q';
	
	ifstream myReadFile;
	myReadFile.open("A-small-attempt3.in");
	ofstream outputFile;
	outputFile.open("output.txt");
	int j = 1;
	if (myReadFile.is_open()) {
		getline(myReadFile,s);
		while (!myReadFile.eof()) {
			getline(myReadFile,s);
			for (int i=0; i < s.length(); i++){
				if(s[i]!=' '){
					s[i]=lang[s[i]-97];
					//cout<<s[i];
				}
			}
			cout<<"Case #"<<j<<": "<<s<<endl;
			j++;
			//outputFile << s;
		}
	}

	return 0;
}
