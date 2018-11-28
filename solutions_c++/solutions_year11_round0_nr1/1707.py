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

typedef enum robotId{
	E_ROBOT_O,
	E_ROBOT_B
}robotId;

typedef struct robotInfo{
	int button[200];
	int currIndex;
	int maxIndex;
	int currPosition;
}robotInfo;

class Robots{
	robotId		_order[200];
	int			_maxOrder;
	int			_currOrder;
	robotInfo	_robO;
	robotInfo	_robB;

public:
	Robots(){ 
		_maxOrder			= 0;
		_currOrder			= 0;
		_robO.currIndex		= 0;
		_robO.currPosition	= 1;
		_robO.maxIndex		= 0;
		_robB.currIndex		= 0;
		_robB.currPosition	= 1;
		_robB.maxIndex		= 0;
	}

	void read(FileReadData &read){
		_maxOrder = read.readNum();

		int iter = 0;
		for(;iter < _maxOrder; iter++){
			char roboName[10];
			read.read(roboName);
			if(0 == strcmp(roboName, "O")){
				_order[iter] = E_ROBOT_O;
				_robO.button[_robO.maxIndex] = read.readNum();
				_robO.maxIndex++;
			}
			else{
				_order[iter] = E_ROBOT_B;
				_robB.button[_robB.maxIndex] = read.readNum();
				_robB.maxIndex++;
			}
		}
	}

	int steps(){
		int time = 0;
		for(;;time++){
			if(_currOrder == _maxOrder) break;
			bool actionTaken = false;
			if(_robO.currIndex < _robO.maxIndex){
				if(_robO.currPosition == _robO.button[_robO.currIndex]){
					if(_order[_currOrder] == E_ROBOT_O){
						actionTaken = true;
						_robO.currIndex++;
					}
					else{
					}
				}
				else{
					if(_robO.currPosition < _robO.button[_robO.currIndex]){
						_robO.currPosition++;
					}
					else{
						_robO.currPosition--;
					}
				}
			}
			if(_robB.currIndex < _robB.maxIndex){
				if(_robB.currPosition == _robB.button[_robB.currIndex]){
					if(_order[_currOrder] == E_ROBOT_B){
						actionTaken = true;
						_robB.currIndex++;
					}
					else{
					}
				}
				else{
					if(_robB.currPosition < _robB.button[_robB.currIndex]){
						_robB.currPosition++;
					}
					else{
						_robB.currPosition--;
					}
				}
			}
			if(actionTaken == true) _currOrder++;
		}
		return time;
	}
};


void main (int argc, char *argv[])
{
	FileReadData read;
	
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\test5.in");
	//read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\A-small-attempt.in");
	read.open("E:\\users\\parikshit\\msvc\\folder1\\data\\A-large.in");
	ofstream out("E:\\users\\parikshit\\msvc\\folder1\\data\\output5.out");

	if(out.good() && read.good())
		cout << "All okay" << endl;
	else
		cout << "File wrong" << endl;

	int numCases = read.readNum();
	cout << numCases << endl;

	int countCases = 0;

	for(;countCases < numCases;countCases++){
		Robots	robo;
		robo.read(read);
		int result = robo.steps();
		cout << "Case #" << countCases + 1 << ": " << result << endl;
		out << "Case #" << countCases + 1 << ": " << result << endl;
	}

	//cin.get();
	return;
}