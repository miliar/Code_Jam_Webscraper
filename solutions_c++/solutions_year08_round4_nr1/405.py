#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
using namespace std;

//ifstream fin("A-small-attempt0.in");
ifstream fin("A-large.in");
ofstream fout("A.txt");

int gate[10001],change[10001];
int d[10001][2];

int main(){
	int N,Test,V,M;
	fin>>N;
	for (Test=1;Test<=N;Test++){
		fin>>M>>V;
		for (int i=0;i<M;i++){
			d[i][0]=d[i][1]=1000000;
		}
		for (int i=0;i<M;i++){
			if (i<M/2){
				fin>>gate[i]>>change[i];
			}else{
				fin>>gate[i];
			}
			if (i>=M/2){
				d[i][gate[i]]=0;
			}
		}
		for (int i=M/2-1;i>=0;i--){
			int r0,r1,k0=1000000,k1=1000000;
			if (gate[i]){
				r0=min(d[i+i+1][0],d[i+i+2][0]);
				r1=d[i+i+1][1]+d[i+i+2][1];
				if (change[i]){
				k0=d[i+i+1][0]+d[i+i+2][0]+1;
				k1=min(d[i+i+1][1],d[i+i+2][1])+1;
				}
			}else{
				r0=d[i+i+1][0]+d[i+i+2][0];
				r1=min(d[i+i+1][1],d[i+i+2][1]);
				if (change[i]){
				k0=min(d[i+i+1][0],d[i+i+2][0])+1;
				k1=d[i+i+1][1]+d[i+i+2][1]+1;
				}
			}
			d[i][0]=min(r0,k0);
			d[i][1]=min(r1,k1);
		}
		if (d[0][V]>M){
			fout<<"Case #"<<Test<<": IMPOSSIBLE"<<endl;

		}else{
			fout<<"Case #"<<Test<<": "<<d[0][V]<<endl;
		}
	}
	fout.close();
	return 0;
}