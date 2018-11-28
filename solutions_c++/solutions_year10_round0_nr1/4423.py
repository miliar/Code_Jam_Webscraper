#include <iostream>
#include <fstream>

using namespace std;


int main(int argc,char* argv[]) {
	ifstream f(argv[1]);
	
	int numcases;
	f>> numcases;

	ofstream out("codejam.out");
	for(int i=0;i<numcases;i++) {
		int n,k;
		f>>n;
		f>>k;

		bool* deviceson = new bool[n+2];
		bool* devicesrecv = new bool[n+2];
		memset(deviceson,0,(n+2)*sizeof(bool));
		memset(devicesrecv,0,(n+2)*sizeof(bool));
		deviceson[0]=true;
		devicesrecv[1]=true;

		for(int j=0;j<k;++j) {
			// Perform snap
			for(int s=0;s<(n+1);++s) {
				if(devicesrecv[s]) deviceson[s] = !deviceson[s];
			}
			// Perform update
			devicesrecv[1]=true;
			for(int s=1;s<(n+1);++s) {
				if(devicesrecv[s] && deviceson[s]) devicesrecv[s+1] = true;
				else devicesrecv[s+1] = false;
			}
		}
		out << "Case #" << (i+1) << ": ";
		if(devicesrecv[n+1]) out << " ON" << endl;
		else out << " OFF" << endl;

		delete[] deviceson;
		delete[] devicesrecv;
	}

	return 0;
}