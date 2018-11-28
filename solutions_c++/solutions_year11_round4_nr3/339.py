#include <bitset>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <deque>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <complex>
using namespace std;
ofstream fout("C-small.out");
ifstream fin("C-small.in");
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		fout << "Case #"<< s+1 << ": ";
		long long N; 
		fin >> N;
		if(N == 1){
			fout << 0 << endl;
			continue;
		}
		int ans = 0;
		for(int i=2;i*i <= N;i++){
			bool p = true;
			
			for(int j=2;j*j<=i;j++){
				if(i % j == 0){
					p = false;
				}
			}
			//cout << i << endl;
			if(p){
				//cout << i << endl;
				int k = i * i;
				
				while(k <= N){
					ans ++;
					k *= i;
					
				}
			}
		}
		//cout << ans + 1 << endl;
		fout << ans + 1 << endl;
	}
}
