// Made by KIA :) 
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <deque>
#include <bitset>
#include <stdio.h>

using namespace std;

FILE* in = fopen("A.in","r");
FILE* out = fopen("A.out","w");

int main(){
	int testnum = 0;
	
	fscanf(in,"%d", &testnum);
	int m[41][41];
	int left[41];
	int Ans = 0;
	for(int test = 0; test < testnum; ++test){
		int side = 0;
		fscanf(in, "%d\n", &side);
		for(int i1 = 0; i1< side; ++i1){
			left[i1] = 0;
			for(int i2 = 0; i2< side; ++i2){
				char c = fgetc(in);
				if(c == '0'){
					m[i1][i2] = 0;}
				else{ 
					m[i1][i2] = 1;}
				if( m[i1][i2] == 1){
					left[i1] = i2+1;
				}
			}
			fscanf(in,"\n");
		}
		Ans = 0;
		for(int r=0; r< side; ++r){
			if(left[r]>(r+1)){
				
				for(int j=r+1; j<side; ++j){
					if(left[j]<=(r+1)){
						int t = left[j];
						for(int k=j; k>=r+1;--k){
							left[k]= left[k-1];
						}
						left[r] = t;
						Ans+=j-r;
						break;
					}
				}
			}
		}
		fprintf(out,"Case #%d: %d\n", test+1, Ans);
	}

	return 0;
}