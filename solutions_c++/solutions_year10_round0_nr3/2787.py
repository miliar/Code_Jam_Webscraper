#include <iostream>
#include <fstream>
using namespace std;

#include "qr_C.h"

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
		if(ifs.eof())
			break;
			long r, k, n;
			ifs >> r >> k >> n;
			vector<int> *vq = new vector<int>;
			for(long in=0;in<n;in++){
				int g;
				ifs >> g;
				vq->push_back(g);
			}
			rcst nrcst(r,k,vq);
			int iret = nrcst.makeMoney();
			cout << "Case #" << i+1 << ": " << iret << endl;
			ofs << "Case #" << i+1 << ": " << iret << endl;
	}

	ifs.close();
	ofs.close();

	return 0;
}
