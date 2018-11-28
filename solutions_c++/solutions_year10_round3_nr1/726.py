#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int main(){
	ifstream fin;
	fin.open("A-Large.in");
	ofstream fout;
	fout.open("A-Large.out");
	int nCases;
	fin >> nCases;
	for(int testCase = 0;testCase < nCases; testCase++){
		int N;
		fin >> N;
		pair <int,int > pi;
		vector <pair <int, int> > vpi;
		for(int i=0;i<N;i++){
			int x, y;
			fin >> x >> y;
			pi.first = x;
			pi.second = y;
			vpi.push_back(pi);
		}
		int ninter = 0;
		for(int i=0;i<N;i++){
			for(int j=i+1;j<N;j++){
				if ((vpi[i].first-vpi[j].first) * (vpi[i].second-vpi[j].second)<0)
					ninter++;
			}
		}
		fout  <<"Case #" << testCase+1 << ": " << ninter << endl;
	}


	return 0;
}