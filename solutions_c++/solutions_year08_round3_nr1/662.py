#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;
int C;

int compare(const void *a,const void *b){
	return *((int*)b)-*((int*)a);
}

int main(){
	ifstream fin("A-small.in");
	ofstream fout("A.txt");
	
	fin >> C;
	fin.ignore();
	for(int i=0;i<C;i++){
		int P,K,L;
		unsigned int freq[100];
		fin >> P >> K >> L;
		if(P*K<L) {fout << "Case #"<<i+1<<": Impossible"<<endl; continue;}
		for(int j=0;j<L;j++){
			fin >> freq[j];
		}
		qsort(freq,L,sizeof(int),compare);
		int sol=0,mult=1;
		for(int j=0;j<L;j++){
			if(j+1>K*mult) mult++;
			sol+=mult*freq[j];
		}
		fout << "Case #"<<i+1<<": "<<sol<<endl;
	}
	
	return 0;
}