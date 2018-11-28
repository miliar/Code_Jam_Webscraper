#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("g10qa.out");
	ifstream fin ("g10qa.in");
	int cases;
	fin>>cases;
	for(int caseNum=0; caseNum<cases; caseNum++){
		int lights, snaps;
		fin>>lights>>snaps;
		bool on=true;
		for(int n=0; n<lights; n++){
			on=snaps%2;
			snaps/=2;
			if(!on)
				break;
		}
		fout<<"Case #"<<caseNum+1<<": ";
		if(on)
			fout<<"ON"<<endl;
		else
			fout<<"OFF"<<endl;
	}
	return 0;
}
