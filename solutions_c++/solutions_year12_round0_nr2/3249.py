/*

 *///============================================================================
// Name        : beads.cpp
// Author      :Tizz
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	ofstream fout("B.out");
	ifstream fin("B.in");
	int t;
	int n,s,p;
	int mc=0,mic=0;
	int tj[100];
	fin >> t;
	for(int i=0;i<t;i++){
		mc=0;mic=0;
	fin >> n>>s>>p;
	int min;
	if(p==1)
		 min=1;
	else
	 min=p*3-4;
		int max=p*3-2;
	for(int j=0;j<n;j++)
		fin>>tj[j];


	for(int j=0;j<n;j++){
		if(tj[j]>=max)
			mc++;
		if(tj[j]>=min)
			mic++;

	}

	mic-=mc;
	if(mic>s)
		fout<<"Case #"<<i+1<<": "<<mc+s<<endl;
	else
		fout<<"Case #"<<i+1<<": "<<mc+mic<<endl;

	}

}

