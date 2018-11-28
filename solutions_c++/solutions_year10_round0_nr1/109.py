#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	fin>>t;
	for(int ti=1; ti<=t; ti++){
		int n, k;
		fin>>n>>k;
		int jugi = (int) pow((double)2, (double)n);
		//cout<<"n "<<n<<" jugi "<<jugi<<endl;
		fout<<"Case #"<<ti<<": ";
		if(k % jugi == jugi-1){
			fout<<"ON";
		}
		else fout<<"OFF";
		fout<<endl;
	}
}