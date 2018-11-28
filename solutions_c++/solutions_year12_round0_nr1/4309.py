#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char transTable[26];

void init(){
	
	transTable[0]='y';
	transTable[1]='h';
	transTable[2]='e';
	transTable[3]='s';
	transTable[4]='o';
	transTable[5]='c';
	transTable[6]='v';
	transTable[7]='x';
	transTable[8]='d';
	transTable[9]='u';
	transTable[10]='i';
	transTable[11]='g';
	transTable[12]='l';
	transTable[13]='b';
	transTable[14]='k';
	transTable[15]='r';
	transTable[16]='z';
	transTable[17]='t';
	transTable[18]='n';
	transTable[19]='w';
	transTable[20]='j';
	transTable[21]='p';
	transTable[22]='f';
	transTable[23]='m';
	transTable[24]='a';
	transTable[25]='q';//estw



}

int main(int argc, char* argv[])
{
	ifstream fin ("A-small-attempt1.in");
	//ifstream fin ("B-large.in");
    ofstream fout ("output.out");
	init();

	int cases;
	fin >> cases;

	cout<<cases;
	
	string buffer;
	getline(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		getline(fin,buffer); //if needed to read the next lines as lines*/

		int counter=0;
		while(counter<buffer.size()){
			char letter=buffer.at(counter);
			
			if(letter!=' '){
				//cout<<buffer.at(counter);
				char newLetter=transTable[letter-97];
				fout<<newLetter;
			}else{
				fout<<' ';
			}

			
			counter++;
		}
		//cout<<output<<endl;
		fout<<endl;
	}

	fin.close();
	fout.close();

	system("pause");
	return 0;
}