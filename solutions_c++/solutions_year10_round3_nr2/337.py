#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t;
	fin>>t;
	for(int ti=1; ti<=t; ti++){
		long long int l, p, c;
		fin>>l>>p>>c;
		long double div;
		int cnt=0;
		//solve
		div =(double) p / (double) l;
		while(div > c){
			div = sqrt(div);
			cnt++;
		}
		//cout<<div<<endl;
		fout<<"Case #"<<ti<<": "<<cnt<<endl;
	}
}