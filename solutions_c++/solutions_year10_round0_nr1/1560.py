#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int n,k,t;

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");
	fin>>t;
	for(int i=0;i<t;++i){
		fin>>n>>k;
		long long p = 1<<n;
		fout<<"Case #"<<(i+1)<<": ";
		if((k+1)%p == 0) fout<<"ON";
		else fout<<"OFF";
		fout<<endl;
	}
}