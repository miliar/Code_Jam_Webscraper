#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
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
		double N=0;
		int pd, pg;

		ifs >> N >> pd >> pg;
		
		if(pg == 0){
			if(pd == 0){
				cout << "Case #" << i+1 << ": " << "Possible" << endl;
				ofs << "Case #" << i+1 << ": " << "Possible" << endl;
			}else{
				cout << "Case #" << i+1 << ": " << "Broken" << endl;
				ofs << "Case #" << i+1 << ": " << "Broken" << endl;
			}
		}else if(pg == 100){
			if(pd == 100){
				cout << "Case #" << i+1 << ": " << "Possible" << endl;
				ofs << "Case #" << i+1 << ": " << "Possible" << endl;
			}else{
				cout << "Case #" << i+1 << ": " << "Broken" << endl;
				ofs << "Case #" << i+1 << ": " << "Broken" << endl;
			}
		}else{
			int pd2 = pd;
			if(pd2%2 == 0){
				pd2/=2;
				if(pd2%2 == 0){
					pd2/=2;
				}
			}
			if(pd2%5 == 0){
				pd2/=5;
				if(pd2%5 == 0){
					pd2/=5;
				}
			}
			int D = 100 * pd2 / pd;

			if((double)D < N + 1.0e-6){
				cout << "Case #" << i+1 << ": " << "Possible" << endl;
				ofs << "Case #" << i+1 << ": " << "Possible" << endl;
			}else{
				cout << "Case #" << i+1 << ": " << "Broken" << endl;
				ofs << "Case #" << i+1 << ": " << "Broken" << endl;
			}
		}
	}

	ifs.close();
	ofs.close();

	return 0;
}
