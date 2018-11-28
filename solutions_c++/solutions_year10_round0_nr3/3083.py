#include <stdint.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <map>

using namespace std;


int main(){
	FILE *f;
	int ncase;
	f = fopen("case.txt", "r");
	
	fscanf(f, "%d", &ncase);
	
	//cout << ncase << endl;
	
	
	for(int i=0;i<ncase;i++){
		int n;
		
		vector <int> vec;
		uint64_t r, k;
		int num;
		
		fscanf(f, "%llu %llu %d\n", &r, &k, &num);
		
		//cout << "r:" << r << endl;
		//cout << "k:" << k << endl;
		//cout << "num:" << num << endl;
		
		for(int k=0;k<num;k++){
			int val;
			fscanf(f, "%d", &val);
			vec.push_back(val);
		}
		
		//for(int j=0;j<vec.size();j++)
		//	cout << vec[j] << " ";
		//cout << endl;
		
		int money = 0;
		int trynum = 0;
		while(trynum<r){
			int restspace = k;
			int j;
			
			//cout << "rest:" << restspace << endl;
			
			int idx = -1;
			for(j=0;j<vec.size();j++){
				if(restspace >= vec[j]){
					restspace = restspace - vec[j];
					//cout << "rest:" << restspace << endl;
					idx++;
				}else{
					break;
				}
			}
			money = money + (k-restspace);
			
			if(idx!=vec.size()-1){
				vector <int> newvec;
				
				for(int k=idx+1;k<vec.size();k++){
					newvec.push_back(vec[k]);
				}
				for(int k=0;k<idx+1;k++){
					newvec.push_back(vec[k]);
				}
				
				vec = newvec;
			}
			//for(int j=0;j<vec.size();j++)
			//	cout << vec[j] << " ";
			//cout << endl;
			
			
			/*
			if(j!=vec.size()-1){
				vector <int> newvec1, newvec2;
				newvec1.assign(vec[0], vec[j]);
				newvec2.assign(vec[j+1], vec.end());
				
				
			}*/
			trynum++;
		}
		
		cout << "Case #" << i+1 << ": ";
		cout << money << endl;
	}
	
	fclose(f);
	return 0;
}


