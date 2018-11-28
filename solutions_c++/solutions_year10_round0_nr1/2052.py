#include <iostream>
#include "fstream"
using namespace std;

int main()
{	
	ifstream fin("C:\\A-large.in");
	ofstream fout("C:\\A-small.out");
	int T, nCase=1;
	fin>>T;
	while(nCase <= T)
	{
		int N,K; //total bits, total snaps.
		fin>>N>>K;
		
		int high = 1<<N;
		if(K % high == high-1)
			fout<<"Case #"<<nCase<<": "<<"ON"<<endl;
		else
			fout<<"Case #"<<nCase<<": "<<"OFF"<<endl;
		++nCase;
	}
	fout<<flush;
	fout.close();
	return 0;
}