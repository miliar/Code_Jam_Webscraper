#define _GLIBCXX_FULLY_DYNAMIC_STRING 1
#undef _GLIBCXX_DEBUG
#undef _GLIBCXX_DEBUG_PEDANTIC
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
	
	int T,N,K;
	fstream filestr;
	ofstream outstr;
	filestr.open("/Users/HOOI/Downloads/A-large.in");
	outstr.open("/Users/HOOI/Downloads/GoogleCodeJam/SnapperLargeOut.txt");
	filestr >> T;
	for (int i=0;i<T;i++){
		filestr >> N >> K;
		if ( (K+1)%(1<<N) == 0) outstr << "Case #"<<i+1<<": ON"<<endl, cout << "Case #"<<i+1<<": ON"<<endl;
		else outstr << "Case #"<<i+1<<": OFF"<<endl,cout << "Case #"<<i+1<<": OFF"<<endl;

	}
	filestr.close();
	outstr.close();
	return 0;
}