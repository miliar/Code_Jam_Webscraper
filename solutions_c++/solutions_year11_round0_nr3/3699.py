#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;

unsigned long int test,xor,sum,min;

ifstream fin("C-large.in");
ofstream fout("out111.txt");

int main() {
	unsigned long int i,j,k,N;
	fin >> test;
	for(i = 1;i <= test;++i) {
		sum = xor = 0;
		min = 1000001;
		fin >> N;
		for(j = 1; j <= N;++j) {
			fin >> k;
			xor = xor ^ k;
			sum += k;
			if(min > k)min = k;
		}
		if(xor == 0) {
			fout << "Case #"<<i<<": " << sum - min << endl;
		}
		else {
			fout << "Case #"<<i<<": " << "NO" << endl;
		}
	}
	return 0;
}