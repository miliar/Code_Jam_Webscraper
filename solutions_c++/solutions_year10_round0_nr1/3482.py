#include <iostream>
#include <fstream>
using namespace std;

int getArroundLife(int n){
	if(n == 1){
		return 1;
	}else{
		return 2 * getArroundLife(int (n-1)) +1;
	}
}

int main(){
	ifstream fin("codejamA.in");
	ofstream fout("codejamA.out");
	int n, N, K;
	fin >> n;
	for(int i = 0; i <n ; i++){
		fin >> N;
		fin >> K;
		int life = getArroundLife(N);
		if( (K+1) % (life  + 1) == 0){
			fout << "Case #" << i + 1 << ": ON"<<endl;
		}else{
			fout << "Case #" << i + 1 << ": OFF"<<endl;
		}
	}
	
	return 0;
}
