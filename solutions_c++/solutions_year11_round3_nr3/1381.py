
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

#define SIZE		20000

class Music{
	int N;
	int L;
	int H;
	int *F;
	int min;
	int max;

public :
	Music() : N(0), L(0), H(0), min(0), max(0) {
		F = (int*)malloc(sizeof(int) * SIZE);
	}

	~Music(){
		free(F);
	}

	bool checkiffactor(int fq){
		int rem = 0;
		int i = 0;
		for(;i < N ; i++){
			if(0 != F[i]%fq) return false;
		}
		return true;
	}

	bool checkifmult(int fq){
		int rem = 0;
		int i = 0;
		for(;i < N ; i++){
			if(0 != fq%F[i]) return false;
		}
		return true;
	}

	int read(FileReadData &read){
		N = read.readNum();
		L = read.readNum();
		H = read.readNum();
		min = H;
		max = L;
		int iter = 0;
		for(;iter < N; iter++){
			F[iter] = read.readNum();
			if(min > F[iter]) min = F[iter];
			if(max < F[iter]) max = F[iter];
		}
		//if((min < L) && (max > H)) return -1;
		int fq = L;
		for(;fq <= H;fq++){
			int iter = 0;
			for(;iter < N ; iter++){
				if(F[iter] == fq) continue;
				if(F[iter] > fq) if(0 == F[iter]%fq) continue;
				if(0 == fq%F[iter]) continue;

				break;
			}
			if(iter == N) return fq;
		}
		return -1;
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
		Music sp;
		int result = sp.read(read);
		if(0 < result){
			cout << "Case #" << countCases + 1 << ": " << result << endl;
			out << "Case #" << countCases + 1 << ": " << result << endl;
		}
		else{
			cout << "Case #" << countCases + 1 << ": " << "NO" << endl;
			out << "Case #" << countCases + 1 << ": " << "NO" << endl;
		}
	}

	//cin.get();
	return;
}