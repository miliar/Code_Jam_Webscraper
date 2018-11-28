#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <bitset>
#include <iostream>
#include <fstream>

using namespace std;

//ifstream fin("A-small.in");
//ofstream fout("A-small.out");
ifstream fin("A-large.in");
ofstream fout("A-large.out");

int main()
{
	int i,j,N,T,t,K;
	fin>>T;
	int all;
	for(t=1;t<=T;t++){
		fin>>N>>K;
		all=(1<<N);
		fout<<"Case #"<<t<<": ";
		if(K%all==all-1){
			fout<<"ON";
		} else {
			fout<<"OFF";
		}
		fout<<endl;
		
	}
    return 0;
}
