#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(){
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");

	int T;
	fin>>T;
	for(int Case=1;Case<=T;Case++){
		fout<<"Case #"<<Case<<": ";
		int n,k;
		fin>>n>>k;
		int mask = (1<<n)-1;
		if((k & mask) == mask)
			fout<<"ON";
		else 
			fout<<"OFF";
		fout<<endl;
	}

	fin.close();
	fout.close();
}