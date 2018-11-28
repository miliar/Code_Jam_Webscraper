/*
 * Round1B10_A.cpp
 *
 *  Created on: May 22, 2010
 *      Author: Jad
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <stack>
#include <gmp.h>
using namespace std;

ifstream fin("GCJ2010/in");
ofstream fout("GCJ2010/out");

#define ROOT ""
#define SLASH '/'

int N,M;
map<string,int> existing;
vector<string> desired;


string getParent(string dir) {
	int lastSlash=0;
	for(int i=0; i<(int)dir.size(); i++) {
		if(dir[i]==SLASH)
			lastSlash=i;
	}

	string parent;
	for(int i=0; i<lastSlash; i++)
		parent.push_back(dir[i]);

	return parent;
}


int createDirectory(string dir) {
	if(existing.count(dir)>0)
		return 0;

	string parent = getParent(dir);
	int num = createDirectory(parent);
	existing[dir]=1;
	return num+1;
}


int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		existing.clear();
		desired.clear();
		existing[""]=1;

		fin>>N>>M;
		for(int i=0; i<N; i++) {
			string str; fin>>str;
			existing[str]=1;
		}
		int cnt=0;
		for(int i=0; i<M; i++) {
			string dir; fin>>dir;
			cnt += createDirectory(dir);
		}

		fout<<"Case #"<<t<<": "<<cnt<<endl;
	}

	return 0;
}
