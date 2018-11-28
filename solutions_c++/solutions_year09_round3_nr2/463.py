#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

#include "R3_B.h"

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
	clsb mass;
	for(int i=0;i<iSize;i++){
		mass.clearall();
		int N;
		ifs >> N;
		for(int j=0;j<N;j++){
			int x,y,z,vx,vy,vz;
			ifs >> x >> y >> z >> vx >> vy >> vz;
			mass.Xo.push_back(x);
			mass.Yo.push_back(y);
			mass.Zo.push_back(z);
			mass.Vx.push_back(vx);
			mass.Vy.push_back(vy);
			mass.Vz.push_back(vz);
		}
		double d,t;
		mass.getMin(d,t);

		cout << setprecision(12) << showpoint;
		ofs << setprecision(12) << showpoint;
		cout << "Case #" << i+1 << ": " << d << " " << t << endl;
		ofs << "Case #" << i+1 << ": " << d << " " << t << endl;
	}
	ifs.close();
	ofs.close();

	return 0;
}
