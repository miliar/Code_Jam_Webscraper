#include<iostream>
#include<fstream>
#include <string>
#include <cstdlib>
#include <map>
using namespace std;


void main(){
	ifstream fin;
	ofstream fout;

	int ntest, N, S, p, count;

	fin.open("B-large.in");
	fout.open("Output.txt");

	if(fin.good() == true) {
		fin >> ntest; cout<<"Number of test case is "<<ntest<<endl;
		fin.ignore();
		for(int j=0; j<ntest; j++){
			fin>>N; 
			fin>>S;
			fin>>p;
			int totalscore;
			int minS=3*p-5, maxS=3*p-2; 
			count=0;
			for(int i=0; i<N; i++){
				fin>> totalscore;
				if(totalscore>=maxS){
					count++;
					continue;
				}
				if(S>0 && p>1){
					if(totalscore<maxS && totalscore>minS){
						count++;
						S--;				
					}
				}

			}
			fout<<"Case #"<<j+1<<": "<<count<<endl;
		}
	}
	fout.close();
	fin.close();
}