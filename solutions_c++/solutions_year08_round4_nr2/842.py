#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;



int main(){
	ifstream fin("A-small.in");
	ofstream fout ("output.txt");
	int C;
	fin >> C;
	
	for(int i=0;i<C;i++){
		bool found = false;
		int N, M, A;
		fin >> N >> M >> A;

		for(int j=0;j<=N;j++){
			if (found) break;
			for (int k=0;k<=M;k++){
				if (found) break;
				for(int l=-N;l<=N;l++){
					if(found) break;
					if((j!=0) && ((A+k*l)%j !=0) && ((A-k*l)%j !=0)) continue;
					for(int m=0;m<=M;m++){
						if(found) break;
						if(abs(j*m-k*l)==A){
							if(abs(j-l)<=N){
								if(found == false){
									found = true;
									if(l<0){
										fout << "Case #"<< i+1 <<": " << -l << " " << 0 << " " <<
											j-l <<" "<< k << " "<< 0 << " " << m << endl;    
									}
									else {
										fout << "Case #"<< i+1 <<": " << 0 << " " << 0 << " " <<
											j <<" "<< k << " "<< l << " " << m << endl;
									}
								}
							}
						}
					}
				}
			}
		}
		if(found == false){
			fout << "Case #"<< i+1 <<": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
};