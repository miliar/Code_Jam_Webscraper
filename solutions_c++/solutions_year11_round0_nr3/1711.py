#include "stdio.h"
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


class Candy{
	int _num;
	int _Ci[1050];
	int _xorSum;
	int _total;
	int _min;

public:
	Candy(){
		_num = 0;
		_xorSum = 0;
		_total = 0;
		_min = 1000000;
	}

	void read(FileReadData &read){
		_num = read.readNum();
		int iter = 0;
		for(;iter < _num ; iter++){
			_Ci[iter] = read.readNum();
			_xorSum ^= _Ci[iter];
			_total += _Ci[iter];
			if(_min > _Ci[iter]) _min = _Ci[iter];
		}
		return;
	}
	
	void getResult(char *result){
		int value = 0;
		int iter = 0;
		if(0 == _xorSum){
			sprintf(result, "%d", (_total-_min));
		}
		else{
			strcpy(result, "NO");
		}
		return;
	}
};



void main (int argc, char *argv[])
{
	FileReadData read;
	
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\test5.in");
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\C-small-attempt0.in");
	read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\C-large.in");
	ofstream out("E:\\users\\parikshit\\msvc\\folder1\\data\\output7.out");

	if(out.good() && read.good())
		cout << "All okay" << endl;
	else
		cout << "File wrong" << endl;

	int numCases = read.readNum();
	cout << numCases << endl;

	int countCases = 0;

	for(;countCases < numCases;countCases++){
		Candy	candy;
		candy.read(read);
		char result[100];
		candy.getResult(result);
		cout << "Case #" << countCases + 1 << ": " << result << endl;
		out << "Case #" << countCases + 1 << ": " << result << endl;
	}

	//cin.get();
	return;
}