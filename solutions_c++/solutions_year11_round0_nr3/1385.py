#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream fout ("g11qrc.out");
	ifstream fin ("g11qrc.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length, sum=0, xorSum=0, minValue=1000001;
		fin>>length;
		for(int n=0; n<length; n++){
			int i;
			fin>>i;
			sum+=i;
			xorSum^=i;
			if(minValue>i)
				minValue=i;
		}
		fout<<"Case #"<<caseNum+1<<": ";
		if(xorSum==0)
			fout<<sum-minValue<<endl;
		else
			fout<<"NO"<<endl;
	}
	return 0;
}
