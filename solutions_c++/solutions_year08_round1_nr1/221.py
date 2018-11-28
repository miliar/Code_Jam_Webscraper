// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
//#include <string>
//#include <set>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int i, j, k, n, t, s;
	vector<int> V1, V2;
	fin>>t;
	for(i=1;i<=t;i++){
		s=0;
		V1.clear();
		V2.clear();
		fin>>n;
		for(j=1;j<=n;j++){
			fin>>k;
			V1.push_back(k);
		}
		for(j=1;j<=n;j++){
			fin>>k;
			V2.push_back(k);
		}
		sort(V1.begin(),V1.end());
		sort(V2.begin(),V2.end());
		for(j=0;j<n;j++){
			s+=V1[j]*V2[n-1-j];
		}
		fout<<"Case #"<<i<<": "<<s<<endl;
	}




	return 0;
}

