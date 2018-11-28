#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

unsigned long main() {
	unsigned long T, N, k;
	long *A = new long[1000000];
	unsigned long xor = 0;
	unsigned long min=0;
	unsigned long sum = 0;
	fin>>T;
	for(unsigned long t =1 ; t<=T; ++t) {
		xor = 0;
		fin>>N;
		for(k=0;k<N;++k) {
			fin>>A[k];
			xor ^= A[k];
		}
		if(xor) {
			fout<<"Case #"<<t<<": NO"<<endl;
		}
		else {
			min = A[0];
			sum = A[0];
			for(k=1;k<N;++k) {
				if(min > A[k])
					min = A[k];
				sum += A[k];
			}
			sum -= min;
			fout<<"Case #"<<t<<": "<<sum<<endl;
		}
	}
	return 0;
}