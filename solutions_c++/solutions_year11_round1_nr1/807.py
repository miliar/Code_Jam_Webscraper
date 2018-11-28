#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
using namespace std;

int main() {

	ifstream fin("A.in");
	ofstream fout("A.out");

	int T,t;
	long long N,PD,PG;

	fin>>T;
	long long D, mcm, mcd;
	for(int t=1;t<=T;t++) {
		bool rta = false;
		fin>>N>>PD>>PG;

		for(mcd=100;mcd>0;mcd--) if(PD%mcd==0 && 100%mcd==0) break;
		if(PD>0) {
			mcm = (100*PD)/mcd;
			D = mcm/PD;
			if(D<=N) {
				rta = true;
				if(PG==100 && PD!=100) rta = false;
				if(PG==0 && PD!=0) rta = false;
			}
		}
		if(PD==0 && PG==100) rta = false;
		if(PD==0 && PG==0) rta = true;
		fout<<"Case #"<<t<<": ";
		if(rta) {
			fout<<"Possible"<<endl;
		}
		else {
			fout<<"Broken"<<endl;
		}
	}

	return 0;
}
