#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
	ifstream fin ("g123a.in");
	ofstream fout ("g123a.out");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length;
		fin>>length;
		for(int n=0; n<length; n++){
			int l;
			fin>>l;
		}
		pair<int, int> levels[20];
		for(int n=0; n<length; n++){
			int p;
			fin>>p;
			levels[n].first=100-p;
			levels[n].second=n;
		}
		sort(levels, levels+length);
		fout<<"Case #"<<caseNum+1<<":";
		for(int n=0; n<length; n++)
			fout<<" "<<levels[n].second;
		fout<<endl;
	}
	return 0;
}
