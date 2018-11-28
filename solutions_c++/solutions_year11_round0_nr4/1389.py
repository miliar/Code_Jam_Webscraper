#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream fout ("g11qrd.out");
	ifstream fin ("g11qrd.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length, answer=0;
		fin>>length;
		for(int n=0; n<length; n++){
			int i;
			fin>>i;
			if(i-1!=n)
				answer++;
		}
		fout<<"Case #"<<caseNum+1<<": "<<answer<<endl;
	}
	return 0;
}
