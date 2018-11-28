// Codejam Qualifications.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string data[25], patt[10];
int L=0, D=0, N=0, counter=0;

int func(int cs, int dn){
	vector< vector< char> > temp;
	bool isth=false;

	for(int i=0; i<patt[cs].size(); i++){
		temp.push_back( vector< char>());
		if(patt[cs][i]=='('){
			i++;
			while(patt[cs][i]!=')'){
				temp.back().push_back(patt[cs][i]);
				i++;
			}
		} else {
			temp.back().push_back(patt[cs][i]);
		}
	}

	for(int i=0; i<temp.size(); i++){
		for(int j=0; j<temp[i].size(); j++){
			cout << temp[i][j] << " ";
		}
		cout << endl;
	}
	
	for(int i=0; i<L; i++){
		for(int j=0; j<temp[i].size(); j++){
			if (data[dn][i]==temp[i][j]){
				isth=true;
				break;
			}
		}
		if(!isth){
			temp.clear();
			return 0;
		}
		isth = false;
	}
	temp.clear();
	return 1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("A-small-attempt1.in");
	ofstream fout("Output.txt");
	int I=0;
	
	fin >> L;
	fin >> D;
	fin >> N;
	
	for(int i=0; i<D; i++){
		fin >> data[i];
	}
	
	for(int i=0; i<N; i++){
		fin >> patt[i];
	}

	for(int i=0; i<D; i++){
		cout << data[i] << endl;
	}

	for(int i=0; i<N; i++){
		cout << patt[i] << endl;
	}
	
	for(int i=0; i<N; i++){
		for(int j=0; j<D; j++){
			I += func(i,j);
		}
		fout << "Case #" << i+1 << ": " << I << endl;
		I=0;
	}
	

	return 0;
}

