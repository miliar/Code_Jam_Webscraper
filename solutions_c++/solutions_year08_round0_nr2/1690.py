#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(){
	ifstream fin;
	fin.open("A-small.in");
	ofstream fout;
	fout.open("output.txt");
	int N;
	fin >> N;
	for(int i=0;i<N;i++){
		int A[30*60]={0};
		int B[30*60]={0};
		int T;
		fin >> T;
		int NA;
		int NB;
		fin >> NA;
		fin >> NB;
		for(int j=0;j<NA;j++){
			char c;
			string s;
			fin >> s;
			int hours,mins;
			sscanf(s.c_str(),"%d%c%d",&hours,&c,&mins);
			A[hours*60+mins]--;
			fin >> s;
			sscanf(s.c_str(),"%d%c%d",&hours,&c,&mins);
			B[hours*60+mins+T]++ ;
		}
		for(int j=0;j<NB;j++){
			char c;
			string s;
			fin >> s;
			int hours,mins;
			sscanf(s.c_str(),"%d%c%d",&hours,&c,&mins);
			B[hours*60+mins]--;
			fin >> s;
			sscanf(s.c_str(),"%d%c%d",&hours,&c,&mins);
			A[hours*60+mins+T] ++;
		}
		int Aps[30*60]={0};
		int Bps[30*60]={0};
		for(int i=0;i<24*60;i++){
			if (i==0){
				Aps[i] = A[i];
				Bps[i] = B[i];
			}
			else{
				Aps[i] = Aps[i-1]+A[i];
				Bps[i] = Bps[i-1]+B[i];
			}
		}
		int n1 = *(min_element(&Aps[0],&(Aps[24*60])));
		int n2 = *(min_element(&Bps[0],&(Bps[24*60])));
		if(n1<0) n1 = abs(n1);
		else n1 = 0;
		if(n2<0) n2 = abs(n2);
		else n2 = 0;
		fout << "Case #" << i+1 << ": " << n1 <<" " << n2 << endl;

	}
	return 0;
};