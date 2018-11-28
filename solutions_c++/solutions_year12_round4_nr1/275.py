#include <iostream>
#include <fstream>

using namespace std;

int main(){
	int numCases;
	ifstream fin("g122a.in");
	ofstream fout("g122a.out");
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int numVines, goal;
		int lengths[10000], distances[10000];
		fin>>numVines;
		for(int n=0; n<numVines; n++)
			fin>>distances[n]>>lengths[n];
		fin>>goal;
		int best[10000];
		for(int n=0; n<numVines; n++)
			best[n]=0;
		best[0]=distances[0];
		bool good=false;
		for(int n=0; n<numVines; n++){
			if(best[n]>lengths[n])
				best[n]=lengths[n];
			for(int i=n+1; i<numVines; i++){
				if(distances[n]+best[n]<distances[i])
					break;
				if(best[i]<distances[i]-distances[n])
					best[i]=distances[i]-distances[n];
			}
			if(distances[n]+best[n]>=goal){
				good=true;
				break;
			}
		}
		fout<<"Case #"<<caseNum+1<<": "<<(good?"YES":"NO")<<endl;;
	}
	return 0;
}
