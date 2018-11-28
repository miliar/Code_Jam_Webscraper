#include <iostream>
#include <fstream> 
#include <cstdlib> 
#include <cmath> 
#include <algorithm>
#include <vector> 
#include <string> 
#include <bitset> 
#include <set>
#include <sstream>
using namespace std; 
ifstream fin ("C-small.in");
ofstream fout ("output.out");
int main(){
	int T;
	fin >> T;
	for(int a=0;a<T;a++){
		fout << "Case #" << (a + 1) << ": ";
		int R, k, N;
		fin >> R >> k >> N;
		int sum = 0;
		int g[N];
		for(int i=0;i<N;i++){
			fin >> g[i];
			sum += g[i];
		}
		if(sum <= k){
			 fout << R*sum << "\n";
			 continue;
		}
		int numgroups[N];
		int amount[N];
		for(int i=0;i<N;i++){
			int j = 0; int sum = 0;
			while(sum <= k){
				sum += g[(j+i)%N];
				j++;
			}
			amount[i] = sum - g[(j-1 + N+i)%N];
			numgroups[i] = j - 1;
			//cout << numgroups[i] << " " << amount[i] << "\n";
		}
		int lasttime[N];
		int eurossince[N];
		for(int i=0;i<N;i++){
			lasttime[i] = -1;
			eurossince[i] = 0;
		}
		int pos = 0;
		int monies = 0;
		bool done = false;
		for(int i=1;i<=R;i++){
			if(!done && lasttime[pos] != -1){
				int left = R - i;
				int numcycles = left/(i - lasttime[pos]);
				monies += numcycles * (eurossince[pos] + amount[pos]);
				left %= (i - lasttime[pos]);
				R = left + i;
				done = true;
			}
			
			lasttime[pos] = i;
			for(int j=0;j<N;j++){
				eurossince[j] += amount[pos];
			}
			eurossince[pos] = 0;
			monies += amount[pos];
			pos += numgroups[pos];
			pos %= N;
		}
		fout << monies << "\n";
	}
}
