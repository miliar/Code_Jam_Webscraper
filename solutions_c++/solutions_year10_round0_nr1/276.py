#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;
#define lint long long

string sol(int n,int k){
	int all = 1<<n;all--;
	return (k&all) == all?"ON":"OFF";
}
int main(){
	int cas,it;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> cas;
	for(it=1;it<=cas;it++){
		int N,K;
		fin >> N >> K;
		fout << "Case #" << it << ": " << sol(N,K) << endl;
	}
	fin.close();fout.close();
	return 0;
}
