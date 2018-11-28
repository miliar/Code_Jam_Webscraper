#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <fstream>
#include <sstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long CalcNum(string str){
	istringstream strin(str);
	long long res;
	strin>>res;
	return res;
}

int main(){
	int N,Test;
	long long d[41][210];
	fin>>N;
	for (int Test=1;Test<=N;Test++){
		string str;
		fin>>str;
		memset(d,0,sizeof(d));
		d[0][0]=1;
		for (int i=1;i<=str.size();i++){
			for (int j=0;j<i;j++){
				for (int k=0;k<210;k++){
					long long x=k+CalcNum(str.substr(j,i-j));
					x%=210;
					d[i][x]+=d[j][k];
					if (j==0) continue;
					x=k-CalcNum(str.substr(j,i-j));
					x%=210;
					if (x<0) x+=210;
					d[i][x]+=d[j][k];
				}
			}
		}
		long long res=0;
		for (int i=0;i<210;i++){
			if (i%2==0||i%3==0||i%5==0||i%7==0){
				res+=d[str.size()][i];
			}
		}
		fout<<"Case #"<<Test<<": "<<res<<endl;
	}
	fout.close();
	return 0;
}