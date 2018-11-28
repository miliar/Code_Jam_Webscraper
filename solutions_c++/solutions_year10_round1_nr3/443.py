#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("g101ac.out");
	ifstream fin ("g101ac.in");
	int length;
	fin>>length;
	for(int n=0; n<length; n++){
		long long a1, a2, b1, b2;
		fin>>a1>>a2>>b1>>b2;
		long long total=0;
		for(long long i=a1; i<=a2; i++){
			long long lower=i*618033989/1000000000, upper=i*1618033988/1000000000;
			if(lower>=b1 && lower<=b2)
				total+=lower-b1+1;
			if(upper>=b1 && upper<=b2)
				total+=b2-upper;
			if(lower>b2 || upper<b1)
				total+=b2-b1+1;
		}
		fout<<"Case #"<<n+1<<": "<<total<<endl;
	}
	return 0;
}
