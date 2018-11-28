
#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

class FileReadData{
	ifstream _read;

public :
	FileReadData(){}
	~FileReadData(){ _read.close();	}
	void open(char *afilename){ _read.open(afilename);}
	bool good(){return _read.good();}
	bool read(char *stream){
		if(_read.good()){
			_read >> stream;
			return true;
		}
		else{ return false; }
	}
	int readNum(){ int value;
		if(_read.good()){
			_read >> value;
			return value;
		}
		else{ return -1;}
	}
};

#define SIZE	200
typedef struct team {
	float games;
	char result[SIZE];
	float iresult[SIZE];
	float igame[SIZE];
	float iwp;
	float iowp[SIZE];
	float iowpTot;
	float ioowp;
	float value;
}team;

class Rpi {
	int		numteam;
	team	team[SIZE];

public : 
	Rpi(): numteam(0) {
		int iter = 0;
		for(;iter < SIZE;iter++) {
			team[iter].games = 0;
			team[iter].ioowp = 0;
			team[iter].iowpTot = 0;
			team[iter].iwp	 = 0;
			team[iter].value = 0;
		}
	}

	void read(FileReadData &read) {
		numteam = read.readNum();
		int iter = 0;
		for(;iter < numteam;iter++) {
			read.read(team[iter].result);
			int iter2 = 0;
			for(;iter2 < numteam;iter2++) {
				if(team[iter].result[iter2] == '1'){
					team[iter].iresult[iter2] = 0;
					team[iter].igame[iter2] = 1;
					team[iter].iwp++;
					team[iter].games++;
				}
				else if(team[iter].result[iter2] == '0'){
					team[iter].iresult[iter2] = 1;
					team[iter].igame[iter2] = 1;
					team[iter].games++;
				}
				else{
					team[iter].iresult[iter2] = 0;
					team[iter].igame[iter2] = 0;
				}
			}
		}
	}

	void secondPass() {
		int iter = 0;
		for(;iter < numteam;iter++){
			int iter2 = 0;
			for(;iter2 < numteam;iter2++) {
				if((iter != iter2) && (team[iter].igame[iter2] != 0)) {
					float games = team[iter2].games - team[iter].igame[iter2];
					team[iter].iowp[iter2] = team[iter2].iwp - team[iter].iresult[iter2];
					team[iter].iowpTot += (team[iter].iowp[iter2]/games);
				}
				else{
					team[iter].iowp[iter2] = 0;
				}
			}
			team[iter].iowpTot = team[iter].iowpTot/team[iter].games;
		}
	}

	void thirdPass() {
		int iter = 0;
		for(;iter < numteam;iter++){
			int iter2 = 0;
			for(;iter2 < numteam;iter2++) {
				if((iter != iter2) && (team[iter].igame[iter2] != 0))
					team[iter].ioowp += team[iter2].iowpTot;
			}
			team[iter].ioowp = team[iter].ioowp / team[iter].games;
		}
	}

	void result(ofstream &out){
		float result = 0;
		int iter = 0;
		for(;iter < numteam;iter++) {
			team[iter].iwp = team[iter].iwp / team[iter].games;
			//team[iter].value = (team[iter].iwp * (numteam - 1) * (numteam - 1) + (2*team[iter].iowpTot *(numteam - 1) + team[iter].ioowp) * team[iter].games) / ( 4* team[iter].games * (numteam - 1) * (numteam - 1));
			team[iter].value = 0.25*team[iter].iwp + 0.5 *team[iter].iowpTot + 0.25 * team[iter].ioowp;
			cout << team[iter].value << endl;
			out <<  team[iter].value << endl;
		}
	}
};

void main (int argc, char *argv[])
{
	FileReadData read;
	
	//read.open("H:\\projects\\codejam\\data\\A-test.in");
	//read.open("H:\\projects\\codejam\\data\\A-small-attempt.in");
	read.open("H:\\projects\\codejam\\data\\A-large-attempt.in");
	ofstream out("H:\\projects\\codejam\\data\\output.out");

	if(out.good() && read.good())
		cout << "All okay" << endl;
	else
		cout << "File wrong" << endl;

	int numCases = read.readNum();
	cout << numCases << endl;

	int countCases = 0;

	for(;countCases < numCases;countCases++){
		Rpi rpi;
		float result = 0;
		rpi.read(read);
		rpi.secondPass();
		rpi.thirdPass();
		cout << "Case #" << countCases + 1 << ": " << endl;
		out << "Case #" << countCases + 1 << ": " <<  endl;
		rpi.result(out);
	}

	//cin.get();
	return;
}