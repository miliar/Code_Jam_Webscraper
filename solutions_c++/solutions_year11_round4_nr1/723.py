#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
	ofstream fout ("g11r2a.out");
	ifstream fin ("g11r2a.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		double length, walk, run, runTime;
		int numWalkways;
		double answer=0;
		pair<double, double> walkways[1001];
		fin>>length>>walk>>run>>runTime>>numWalkways;
		run-=walk;
		for(int n=0; n<numWalkways; n++){
			int a, b, c;
			fin>>a>>b>>c;
			length-=b-a;
			walkways[n].first=c+walk;
			walkways[n].second=b-a;
		}
		walkways[numWalkways].first=walk;
		walkways[numWalkways].second=length;
		numWalkways++;
		sort(walkways, walkways+numWalkways);
		for(int n=0; n<numWalkways; n++){
			if(runTime==0){
				answer+=walkways[n].second/walkways[n].first;
			}
			else{
				if(runTime*(walkways[n].first+run)>=walkways[n].second){
					answer+=walkways[n].second/(walkways[n].first+run);
					runTime-=walkways[n].second/(walkways[n].first+run);
				}
				else{
					answer+=runTime;
					walkways[n].second-=runTime*(walkways[n].first+run);
					runTime=0;
					answer+=walkways[n].second/walkways[n].first;
				}
			}
		}
		fout.precision(10);
		fout<<"Case #"<<caseNum+1<<": "<<answer<<endl;
	}
	return 0;
}
