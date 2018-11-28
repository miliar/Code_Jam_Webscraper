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
ifstream fin ("A-large.in");
ofstream fout ("output.out");
int main(){
	int T;
	fin >> T;
	for(int aa=0;aa<T;aa++){
		fout << "Case #" << (aa + 1) << ": ";
		int N, K;
		fin >> N >> K;
		string stuff[N];
		for(int i=0;i<N;i++){
			fin >> stuff[i];
		}
		string lol[N];
		for(int i=0;i<N;i++){
			for(int j=N-1;j>=0;j--){
				if(stuff[i][j] != '.'){
					lol[i].push_back(stuff[i][j]);
				}
			}
			while(lol[i].length() != N){
				lol[i].push_back('.');
			}
		}
		bool winred = false, winblue = false;
		for(int i=0;i<N;i++){
			for(int j=0;j<N-K+1;j++){
				bool yesr = true; bool yesb = true;
				for(int k=j;k<j+K;k++){
					if(lol[i][k] != 'R'){
						yesr = false;
					}
					if(lol[i][k] != 'B'){
						yesb = false;
					}
				}
				winred |= yesr; winblue |= yesb;
			}
		}
		
		for(int i=0;i<N-K+1;i++){
			for(int j=0;j<N;j++){
				bool yesr = true; bool yesb = true;
				for(int k=i;k<i+K;k++){
					if(lol[k][j] != 'R'){
						yesr = false;
					}
					if(lol[k][j] != 'B'){
						yesb = false;
					}
				}
				winred |= yesr; winblue |= yesb;
			}
		}
		
		for(int i=0;i<N-K+1;i++){
			for(int j=0;j<N-K+1;j++){
				bool yesr = true; bool yesb = true;
				for(int k=0;k<K;k++){
					if(lol[i+k][j+k] != 'R'){
						yesr = false;
					}
					if(lol[i+k][j+k] != 'B'){
						yesb = false;
					}
				}
				winred |= yesr; winblue |= yesb;
			}
		}
		
		for(int i=K-1;i<N;i++){
			for(int j=0;j<N-K+1;j++){
				bool yesr = true; bool yesb = true;
				for(int k=0;k<K;k++){
					if(lol[i-k][j+k] != 'R'){
						yesr = false;
					}
					if(lol[i-k][j+k] != 'B'){
						yesb = false;
					}
				}
				winred |= yesr; winblue |= yesb;
			}
		}
		string asdf[4] = {"Neither", "Red", "Blue", "Both"};
		fout << asdf[(int)winred + 2*((int)winblue)] << "\n";
	}
}
