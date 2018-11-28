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
	int i,j,N,M,T,t,K;
	int a[1001],b[1001];
	fin>>T;
	int all;
	for(t=1;t<=T;t++){
		fin>>N;
		all=0;
		for(i=0;i<N;i++){
			fin>>a[i]>>b[i];
		}
		for(i=0;i<N;i++){
			for(j=0;j<i;j++){
				if( (a[i]-a[j])*(b[i]-b[j])<0 ){
					all++;
				}
			}
		}
		fout<<"Case #"<<t<<": ";
		
		fout<<all<<endl;
		
	}
    return 0;
}
