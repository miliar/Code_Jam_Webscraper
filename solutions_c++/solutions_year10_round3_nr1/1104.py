#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

class abpair{
public:
	int mA;
	int mB;
	int mAid;
	int mBid;
	abpair(int a, int b){
		mA = a;
		mB = b;
	}
};

bool compbyA(const abpair& p1, const abpair& p2){
	return p1.mA < p2.mA;
}

bool compbyB(const abpair& p1, const abpair& p2){
	return p1.mB < p2.mB;
}

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
		vector<abpair> vp;

		for(int in=0;in<N;in++){
			int a,b;
			ifs >> a >> b;
			vp.push_back(abpair(a,b));
		}

		//std::sort(vp.begin(), vp.end(), compbyB);
		//for(int in=0;in<N;in++){
		//	vp.at(in).mBid = in;
		//}

		std::sort(vp.begin(), vp.end(), compbyA);
		//for(int in=0;in<N;in++){
		//	vp.at(in).mAid = in;
		//}

		int iCnt = 0;
		for(int in=0;in<N;in++){
			for(int j=in+1;j<N;j++){
				if(vp.at(in).mB > vp.at(j).mB){
					iCnt++;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << iCnt << endl;
		ofs << "Case #" << i+1 << ": " << iCnt << endl;
	}


	ifs.close();
	ofs.close();

	return 0;
}
