#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("in4.txt");
ofstream fout("out.txt");

int T;
int n, k;
bool flag;

int step(int k){
	int s = 1;
	for (int i=0;i<k;i++)
		s=s*2;
	return s;
}

int main(){
	fin>>T;
	for (int i=0;i<T;i++){
		fin>>n>>k;
		flag = (k>=step(n-1))&&((k+1)%step(n)==0);
		//fout<<n<<"  "<<k<<endl;
		if (flag) fout<<"Case #"<<i+1<<": ON"<<endl;
		else fout<<"Case #"<<i+1<<": OFF"<<endl;
	}

return 0;
}