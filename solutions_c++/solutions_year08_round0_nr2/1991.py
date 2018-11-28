#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;
int N,T,NA,NB;

struct time{
	int DH,DM;
	int AH,AM;
};
vector <struct time> NA_times;
vector <struct time> NB_times;

bool compare(struct time a,struct time b){
	return ((a.DH*60)+a.DM) <= ((b.DH*60)+b.DM);
}

void recurse_NA(struct time,int);
void recurse_NB(struct time,int);

void recurse_NA(struct time x,int index){
	NB_times.erase(NB_times.begin()+index);
	int arrTimeB=(x.AH*60)+x.AM;
	for(int i=0;i<NA_times.size();i++){
		struct time temp=NA_times.at(i);
		int depTimeA=(temp.DH*60)+temp.DM;
		if(arrTimeB+T<=depTimeA){
			return recurse_NB(temp,i);
		}
	}
}

void recurse_NB(struct time x,int index){
	NA_times.erase(NA_times.begin()+index);
	int arrTimeA=(x.AH*60)+x.AM;
	for(int i=0;i<NB_times.size();i++){
		struct time temp = NB_times.at(i);
		int depTimeB=(temp.DH*60)+temp.DM;
		if(arrTimeA+T<=depTimeB){
			return recurse_NA(temp,i);
		}
	}
}
	

int main(){
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	
	fin>>N;
	for(int i=0;i<N;i++){
		int countA=0,countB=0;
		fin>>T>>NA>>NB;
		for(int j=0;j<NA;j++){
			struct time temp;
			fin>>temp.DH;
			fin.ignore();
			fin>>temp.DM>>temp.AH;
			fin.ignore();
			fin>>temp.AM;
			NA_times.push_back(temp);
		}
		for(int j=0;j<NB;j++){
			struct time temp;
			fin>>temp.DH;
			fin.ignore();
			fin>>temp.DM>>temp.AH;
			fin.ignore();
			fin>>temp.AM;
			NB_times.push_back(temp);
		}
		sort(NA_times.begin(),NA_times.end(),compare);
		sort(NB_times.begin(),NB_times.end(),compare);
		while(!NA_times.empty() || !NB_times.empty()){
			if(NA_times.empty()) {countB+=NB_times.size(); break;}
			if(NB_times.empty()) {countA+=NA_times.size(); break;}
			if(compare(NA_times.at(0),NB_times.at(0))){
				countA++;
				recurse_NB(NA_times.at(0),0);
			}
			else{
				countB++;
				recurse_NA(NB_times.at(0),0);
			}
		}
		fout<<"Case #"<<i+1<<": "<<countA<<" "<<countB<<endl;
		NA_times.clear();
		NB_times.clear();
	}
	return 0;
}
