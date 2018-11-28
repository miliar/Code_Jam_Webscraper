#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main(){
	long long  N,Test,P,K,L,res;
	long long d[1000];
	fin>>N;
	for (Test=1;Test<=N;Test++){
		res=0;
		fin>>P>>K>>L;
		for (int i=0;i<L;i++){
			fin>>d[i];
		}
		sort(d,d+L,greater<int>());
		int now=0;
		
		for (int i=0;i<L;i++){
			if (i%K==0) now++;
			res+=now*d[i];
		}
		fout<<"Case #"<<Test<<": "<<res<<endl;
	}
	fout.close();
	return 0;
}