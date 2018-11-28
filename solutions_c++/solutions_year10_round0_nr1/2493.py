#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt.in");
ofstream fout("output.txt");
int main()
{
	int T,N,K,tmp;
	fin>>T;
	for(int i=1;i<=T;i++){
		fout<<"Case #"<<i<<": ";
		fin>>N>>K;
		K++;
		tmp=1;
		for(int i=0;i<N;i++)
			tmp*=2;
		if(K%tmp==0) fout<<"ON"<<endl;
		else fout<<"OFF"<<endl;		
	}
}
