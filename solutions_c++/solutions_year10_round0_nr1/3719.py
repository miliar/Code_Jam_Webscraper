#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int T, N, K;

	fin>>T;
	int tmp = 0;
	for(int t=1;t<=T;t++){
		fin>>N>>K;
		tmp = 1<< N;
		//cout<<tmp<<'\t';
		fout<<"Case #"<<t<<": ";
		if(K>0 && (K+1)%tmp == 0){
			fout<<"ON"<<endl;
		}else{
			fout<<"OFF"<<endl;
		}
	}
	return 0;
}