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
		int N=0;

		ifs >> N;

		int ccol = -1;
		int opos = 1;
		int bpos = 1;
		int wait = 0;
		int tcount = 0;
		
		for(int in=0;in<N;in++){
			string col;
			int ibno;
			ifs >> col >> ibno;
			if(col == "O"){
				if(ccol == 1){
					int cnt = max(abs(ibno - opos) - wait, 0) + 1;
					wait = cnt;
					tcount += cnt;
				}else{
					int cnt = abs(ibno - opos) + 1;
					wait += cnt;
					tcount += cnt;
				}
				opos = ibno;
				ccol = 0;
			}else{
				if(ccol == 0){
					int cnt = max(abs(ibno - bpos) - wait, 0) + 1;
					wait = cnt;
					tcount += cnt;
				}else{
					int cnt = abs(ibno - bpos) + 1;
					wait += cnt;
					tcount += cnt;
				}
				bpos = ibno;
				ccol = 1;
			}
		}

		cout << "Case #" << i+1 << ": " << tcount << endl;
		ofs << "Case #" << i+1 << ": " << tcount << endl;
	}

	ifs.close();
	ofs.close();

	return 0;
}
