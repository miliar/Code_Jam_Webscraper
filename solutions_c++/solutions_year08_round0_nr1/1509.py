// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <set>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{	
	ifstream fin("A.txt");
	ofstream fout("out.txt");
	map<string,int> M;
	int ncases, q, n, i, j, z, ns;
	int* Q;
	string S;
	set<int> searched;
	fin>>ncases;
	for(z=1;z<=ncases;z++){
		M.clear();
		fin>>n;
		fin.ignore();
		for(i=1;i<=n;i++){
			getline(fin, S);
			M[S]=i;
			//fin.ignore();
			//cout<<S<<endl;
		}

		fin>>q;
		fin.ignore();
		Q=new int[q];
		for(i=0;i<q;i++){
			getline(fin,S);
			Q[i]=M[S];
			//cout<<Q[i]<<endl;
		}
		ns=0;
		searched.clear();
		for(i=0;i<q;i++){
			if(Q[i]!=0){
				searched.insert(Q[i]);
				//cout<<searched.size()<<" ";
				if(searched.size()==n){
					//cout<<"yay";
					searched.clear();
					searched.insert(Q[i]);
					ns++;
				}
			}
		}
		fout<<"Case #"<<z<<": "<<ns<<endl;
		
	}
	return 0;
}

