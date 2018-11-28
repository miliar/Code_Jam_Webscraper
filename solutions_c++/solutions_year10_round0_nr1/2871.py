#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

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
		int N=0, K=0;
		ifs >> N >> K;
		bool bon = true;

		int iBit = 0;
		for(int in=0;in<N;in++){
			iBit = (int)pow(2, (double)in);
			if((K & iBit) != iBit){
				bon = false;
				break;
			}
		}

		if(bon){
			cout << "Case #" << i+1 << ": ON" << endl;
			ofs << "Case #" << i+1 << ": ON" << endl;
		}else{
			cout << "Case #" << i+1 << ": OFF" << endl;
			ofs << "Case #" << i+1 << ": OFF" << endl;
		}
	}

	ifs.close();
	ofs.close();

	return 0;
}
