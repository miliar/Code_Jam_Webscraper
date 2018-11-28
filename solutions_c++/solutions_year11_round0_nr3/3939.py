#include <iostream>
#include <fstream>

using namespace std;

int main() {
	
	ifstream fin("C.in");
	ofstream fout("C.out");
	
	int T, N;
	int P, S;
	int xP, xS;
	int v[1100];
	
	fin>>T;
	for(int k=0;k<T;k++) {
		fin>>N;
		for(int i=0;i<N;i++) {
			fin>>v[i];
		}
		
		// Test all:
		int max = -1;
		for(int i=0;i<(1<<N);i++) {
			P = S = 0;
			xP = xS = 0;
			for(int j=0;j<N;j++) {
				if(i&(1<<j)) {
					S += v[j];
					xS ^= v[j];
					// XOR xS
				}
				else {
					P += v[j];
					xP ^= v[j];
					// XOR xP
				}
			}
			if(xP == xS && max<S && P!=0 && S!=0) {
				max = S;
			}
		}
		if(max==-1) fout<<"Case #"<<k+1<<": NO"<<endl;
		else fout<<"Case #"<<k+1<<": "<<max<<endl;
	}
}
