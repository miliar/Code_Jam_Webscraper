#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

#include "r1b_a_2010.h"

int main(int argc , char** argv){

	ifstream ifs;
	if(argc>1){
		ifs.open(argv[1]);
	}else{
		ifs.open("input.txt");
	}
	if(!ifs.good())
		return -1;

	int iSize=0;
	ifs >> iSize;

	ofstream ofs("output.txt");
	for(int i=0;i<iSize;i++){
		int N=0, M=0;
		ifs >> N >> M;

		dirs d;
		for(int in=0;in<N;in++){
			string path;
			ifs >> path;
			d.inputpath(path);
		}

		d.initCnt();
		for(int in=0;in<M;in++){
			string path;
			ifs >> path;
			d.inputpath(path);
		}

		cout << "Case #" << i+1 << ": " << d.getCnt() << endl;
		ofs << "Case #" << i+1 << ": " << d.getCnt();
		if(i!=iSize-1)
			ofs << endl;
	}


	ifs.close();
	ofs.close();

	return 0;
}
