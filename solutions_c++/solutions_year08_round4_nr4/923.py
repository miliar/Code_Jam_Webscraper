#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
//#include <map>
//#include <set>

using namespace std;

vector<int> V;
string S, S2;
int n;



int permute(){
	S2="";
	for(int i=0;i<S.length();i+=n){
		for(int j=0;j<n;j++){
			S2+=(S[V[j]+i-1]);
		}
	}
//	cout<<S2<<endl;
	int t=1;
	for(i=1;i<S2.length();i++){
		if(S2[i]!=S2[i-1]) t++;
	}
	return t;
}

	


int main(int argc, char* argv[])
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int i, j, k, l, m, t, z;

	fin>>z;
	for(l=1;l<=z;l++){
		V.clear();
		fin>>n;
		for(i=1;i<=n;i++){
			V.push_back(i);
		}
		fin>>S;
		m=50000;
		do{
			t=permute();
			if(t<m) m=t;
		}while(next_permutation(V.begin(),V.end()));
	

		fout<<"Case #"<<l<<": "<<m<<endl;
	}
	return 0;
}
