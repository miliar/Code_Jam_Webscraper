#include <iostream>
#include <fstream> 
#include <cstdlib> 
#include <cmath> 
#include <algorithm>
#include <vector> 
#include <string> 
#include <bitset> 
#include <set>
#include <sstream>
using namespace std; 
ifstream fin ("A-large.in");
ofstream fout ("output.out");
int main(){
	int T;
	fin >> T;
	for(int i=0;i<T;i++){
		int N;
		long long K;
		fin >> N >> K;
		long long pow = 1;
		for(int j=0;j<N;j++){
			pow *= 2;
		}
		fout << "Case #" << (i + 1) << ": ";
		if((K +1)%pow){
			fout << "OFF\n";
		} else {
			fout << "ON\n";
		}
	}
}
