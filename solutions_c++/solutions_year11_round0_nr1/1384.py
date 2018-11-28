#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ofstream fout ("g11qra.out");
	ifstream fin ("g11qra.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length, pos[2]={1,1}, time[2]={0,0};
		fin>>length;
		for(int n=0; n<length; n++){
			char c;
			int i, j;
			fin>>c>>j;
			i=(c=='B');
			if(pos[i]<j)
				time[i]+=j-pos[i];
			else
				time[i]+=pos[i]-j;
			time[i]=max(time[i], time[(i+1)%2])+1;
			pos[i]=j;
		}
		fout<<"Case #"<<caseNum+1<<": "<<max(time[0], time[1])<<endl;
	}
	return 0;
}
