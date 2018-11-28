
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

#define SIZE		100
class Painting{
	int R;
	int C;
	int RC;
	char color[SIZE*SIZE];
	bool result;

public :
	Painting() : R(0), C(0), RC(0){
	}

	void read(FileReadData &read){
		R = read.readNum();
		C = read.readNum();
		RC = R*C;

		int iter = 0;
		for(;iter < R; iter++){
			read.read(&(color[iter*C]));
		}
	}

	bool checkNchng(int i){
		if((color[i] == '#')&&
			(color[i+1] == '#')&&
			(color[i+C] == '#')&&
			(color[i+C+1] == '#')){
			color[i] = '/';
			color[i+1] = '\\';
			color[i+C] = '\\';
			color[i+C+1] = '/';
			return true;
		}
		else return false;
	}

	bool change() {
		int iter = 0;
		for (;iter < RC; iter++){
			if('#' == color[iter]){
				if(false == checkNchng(iter)) {
					result = false;
					return false;
				}
			}
		}
		result = true;
		return true;
	}

	void print(ofstream &out){
		if(result == false){
			cout << "Impossible" << endl;
			out << "Impossible" << endl;
		}
		else{
			int i1 = 0;
			for(;i1<R;i1++){
				int i2 = 0;
				for(;i2 < C;i2++){
					cout << color[i1*C+i2];
					out << color[i1*C+i2];
				}
				cout << endl;
				out << endl;
			}
		}
	}
};



void main (int argc, char *argv[])
{
	FileReadData read;
	
	//read.open("H:\\projects\\codejam\\data\\A-test.in");
	read.open("H:\\projects\\codejam\\data\\A-small-attempt.in");
	//read.open("H:\\projects\\codejam\\data\\A-large-attempt.in");
	ofstream out("H:\\projects\\codejam\\data\\output.out");

	if(out.good() && read.good())
		cout << "All okay" << endl;
	else
		cout << "File wrong" << endl;

	int numCases = read.readNum();
	cout << numCases << endl;

	int countCases = 0;

	for(;countCases < numCases;countCases++){
		Painting pt;
		pt.read(read);
		pt.change();
		cout << "Case #" << countCases + 1 << ": " << endl;
		out << "Case #" << countCases + 1 << ": " <<  endl;
		pt.print(out);
	}

	//cin.get();
	return;
}